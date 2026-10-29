# Spectre.Console.Cli (command-line apps)

Separate package/repo (`spectreconsole/spectre.console.cli`). Verified against source at tag
0.57.2 and by running small apps through `CommandAppTester`. Members: `api/cli.md`,
`api/cli-testing.md`. **Known docs/source drift (source wins):** the docs site's samples show
`protected override … Execute(...)` — the released base classes declare `public abstract`, so the
override must be `public override` (compiler error CS0507 otherwise). Older tutorials show
`Execute(context, settings)` without a `CancellationToken`; 0.57 requires the 3-parameter form.
Not trim/AOT compatible. 1.0 is in alpha with more breaking changes — pin the version.

## Shape of an app

```csharp
using System.ComponentModel;

public sealed class GreetSettings : CommandSettings
{
    [CommandArgument(0, "<name>")]                 // <required>  [optional]
    [Description("Who to greet")]
    public string Name { get; init; } = "";

    [CommandOption("-c|--count")]                  // short|long; bool => flag
    [Description("Times to greet")]
    [DefaultValue(1)]                              // shown in help; applied when absent
    public int Count { get; init; } = 1;

    [CommandOption("--shout")]
    public bool Shout { get; init; }

    public override ValidationResult Validate()    // after binding; use for cross-field rules
        => Count < 1 ? ValidationResult.Error("Count must be at least 1") : ValidationResult.Success();
}

public sealed class GreetCommand : Command<GreetSettings>
{
    public override int Execute(CommandContext context, GreetSettings settings, CancellationToken cancellationToken)
    {
        for (var i = 0; i < settings.Count; i++)
            AnsiConsole.MarkupLineInterpolated($"Hello, [green]{settings.Name}[/]{(settings.Shout ? "!" : "")}");
        return 0;                                  // process exit code
    }
}

public static class Program
{
    public static int Main(string[] args)
    {
        var app = new CommandApp<GreetCommand>();  // single-command app (default command)
        return app.Run(args);
    }
}
```

Base classes: `Command<TSettings>` (`int Execute(ctx, settings, ct)`), `AsyncCommand<TSettings>`
(`Task<int> ExecuteAsync(ctx, settings, ct)`), and settings-less `Command` /`AsyncCommand`
(`Execute(ctx, ct)`). Optionally override `Validate(CommandContext, TSettings)` (sees the context).

Multi-command app:

```csharp
public static class MultiProgram
{
    public static async Task<int> Main(string[] args)
    {
var app = new CommandApp();                         // no default command
app.Configure(config =>
{
    config.SetApplicationName("tool");
    config.SetApplicationVersion("1.4.0");          // enables -v/--version
    config.AddExample("add", "file.txt");

    config.AddCommand<GreetCommand>("greet")
          .WithDescription("Say hello")
          .WithAlias("hi")
          .WithExample("greet", "Ada", "-c", "2");

    config.AddBranch("remote", remote =>             // `tool remote add …`
    {
        remote.SetDescription("Manage remotes");
        remote.AddCommand<GreetCommand>("add");
        remote.AddDelegate("list", (ctx, ct) => { AnsiConsole.WriteLine("origin"); return 0; });
    });

    config.AddAsyncDelegate<GreetSettings>("later", async (ctx, s, ct) => { await Task.Delay(10, ct); return 0; });
});
return await app.RunAsync(args);
    }
}
```

`new CommandApp<TDefault>()` / `app.SetDefaultCommand<T>()` run `T` when no command word is given.
`config.AddBranch<TSettings>(name, b => …)` lets branch-level options be shared by children
(children's settings derive from `TSettings`).

## Parameter rules (from the binder)

| Declaration | Meaning |
|---|---|
| `[CommandArgument(0, "<x>")]` / `"[x]"` | positional, required/optional. Position numbers must be unique; an **array** argument must be the last positional |
| `[CommandOption("-v\|--verbose")]` on `bool` | flag |
| `[CommandOption("-o\|--output <FILE>")]` | option with value (`<V>` required value, `[V]` optional value) |
| `[CommandOption("--level [LEVEL]")]` + `FlagValue<int>` | flag that *may* carry a value: `.IsSet`, `.Value` (`--level` → `IsSet=true, Value=default`) |
| `string[]` / `int[]` option | repeatable: `-t a -t b` |
| `IDictionary<K,V>` / `ILookup<K,V>` option `<KEY=VALUE>` | `-D k=v -D k2=v2`. **Declare the property as `IDictionary<,>` (or `IReadOnlyDictionary`/`ILookup`), not `Dictionary<,>`** — a concrete `Dictionary` fails with `Failed to convert 'k=v' to Dictionary`2` (verified). Custom splitting: `[PairDeconstructor(typeof(X))]` |
| enum | accepted case-insensitively; allowed values listed in help |
| `[CommandOption("--x", IsHidden = true)]` | hidden from help |
| `[CommandOption("--n", isRequired: true)]` | required option |
| `[DefaultValue(x)]` | default (also shown in help's DEFAULT column; hide with `config.HideOptionDefaultValues()`) |
| `[Description("…")]` | help text (markup allowed) |
| `[TypeConverter(typeof(Conv))]` on the **property** | custom string→T conversion (a `TypeConverter` subclass) |
| your own `ParameterValidationAttribute` subclass (none ship in the box) | per-parameter validation: ctor takes the error message; override `Validate(CommandParameterContext)` |
| `ParameterValueProviderAttribute` subclass | supply value from elsewhere (env var, config) when not on the command line |

Settings can also be bound through a **constructor** (parameter names match option/argument
properties; other parameters are resolved from the type registrar), so positional records work.
`context.Remaining` (`IRemainingArguments`) holds what didn't bind: `.Raw` = everything after a bare
`--`, `.Parsed` = unknown `--key value` pairs as an `ILookup<string,string?>` whose keys **keep the
leading dashes** (`Parsed["--unknown"]`; verified). `config.UseStrictParsing()` turns unknown
options into errors instead.

## Lifecycle and exit codes (observed)

parse → help? → bind settings → `settings.Validate()` → interceptors `Intercept` → `command.Validate`
→ `Execute` → interceptors `InterceptResult` → exit code.

| Situation | Output | Exit code |
|---|---|---|
| success | whatever you return | your value |
| `-h` / `--help` anywhere | help | 0 |
| no args, no default command | root help | 0 |
| branch name only (`tool remote`) | branch help | **1** |
| parse error / unknown command / missing required arg / validation error | `Error: …` (+ pointer to the bad token) | **-1** |
| unhandled exception in command | `Error: <message>` (rendered) | **-1** |
| cancelled (`OperationCanceledException`) | – | `CancellationExitCode` (130) |
| `--version` / `-v` | application version | 0 (requires `SetApplicationVersion`/`UseAssemblyInformationalVersion`) |

Customize: `config.SetExceptionHandler((ex, resolver) => { …; return 2; })` (not called if
`PropagateExceptions()`); `config.PropagateExceptions()` rethrows from `Run`/`RunAsync` (also
what tests normally want; in a debugger, exceptions marked `AlwaysPropagateWhenDebugging` rethrow);
`config.CancellationExitCode(n)`; `config.UseStrictParsing()`; `config.CaseSensitivity(CaseSensitivity.None)`;
`config.ValidateExamples()` (fails fast if `AddExample` args don't parse).

`ValidationResult.Error("message")` messages are **markup** and printed as `Error: message`.
Return non-zero from `Execute` for domain failures instead of throwing.

Built-in hidden commands (under the `cli` branch): `tool cli version`, `cli explain [command]
[--detailed] [--hidden]`, `cli xmldoc`, `cli opencli` (also `--help-dump-opencli`).

## Async and cancellation

```csharp
using System.Net.Http;

public sealed class DownloadCommand : AsyncCommand<DownloadCommand.Settings>
{
    public sealed class Settings : CommandSettings
    {
        [CommandArgument(0, "<url>")] public string Url { get; init; } = "";
    }

    public override async Task<int> ExecuteAsync(CommandContext context, Settings settings, CancellationToken cancellationToken)
    {
        using var http = new HttpClient();
        var bytes = await http.GetByteArrayAsync(settings.Url, cancellationToken);
        AnsiConsole.MarkupLineInterpolated($"[green]{bytes.Length}[/] bytes");
        return 0;
    }
}
```

`app.Run(args, cts.Token)` / `RunAsync(args, token)` pass the token to commands; Ctrl+C handling
is yours (`Console.CancelKeyPress` → `cts.Cancel()`), and the cancel exit code is returned.

## Dependency injection

Implement `ITypeRegistrar` (`Register(service, impl)`, `RegisterInstance`, `RegisterLazy`, `Build()`
→ `ITypeResolver.Resolve(Type)`) over your container and pass it to `new CommandApp(registrar)` /
`new CommandApp<T>(registrar)`. The CLI registers every command type, every settings type,
`IConfiguration`, `CommandModel` and a lazy `IAnsiConsole` into it, and resolves commands (and
settings, and `ICommandInterceptor`s as `IEnumerable<ICommandInterceptor>`) from it, so
constructor injection works. With no registrar the built-in one is used: it also supports
constructor injection of the services registered *with the CLI* (e.g. `IAnsiConsole`), but not
your own services.

```csharp-fragment
public sealed class MsDiRegistrar(IServiceCollection services) : ITypeRegistrar
{
    public void Register(Type service, Type implementation) => services.AddSingleton(service, implementation);
    public void RegisterInstance(Type service, object implementation) => services.AddSingleton(service, implementation);
    public void RegisterLazy(Type service, Func<object> factory) => services.AddSingleton(service, _ => factory());
    public ITypeResolver Build() => new MsDiResolver(services.BuildServiceProvider());
}

public sealed class MsDiResolver(IServiceProvider provider) : ITypeResolver, IDisposable
{
    public object? Resolve(Type? type) => type == null ? null : provider.GetService(type);
    public void Dispose() => (provider as IDisposable)?.Dispose();
}
```

Wire-up: `var services = new ServiceCollection(); services.AddSingleton<IMyService, MyService>();
var app = new CommandApp<MyCommand>(new MsDiRegistrar(services));`. (Microsoft.Extensions.* is *not*
a dependency of Spectre; the registrar above is the whole integration.) Make sure the resolver
returns `null` rather than throwing for unknown types.

## Interceptors

```csharp
public sealed class TimingInterceptor : ICommandInterceptor
{
    public void Intercept(CommandContext context, CommandSettings settings) { /* before Execute */ }
    public void InterceptResult(CommandContext context, CommandSettings settings, ref int result) { /* after */ }
}
// config.SetInterceptor(new TimingInterceptor());   or register ICommandInterceptor in your container
```

Typical uses: set up logging verbosity from a shared `--verbose` option in a base settings class,
start/stop timers, translate result codes.

## Help customization

`config.SetHelpProvider(new MyHelpProvider(config.Settings))` — subclass `HelpProvider` and override
`GetHeader/GetDescription/GetUsage/...`, or just style it:
`config.Settings.HelpProviderStyles = new HelpProviderStyle { Options = new OptionStyle { … } }`
(`HelpProviderStyle.Default`). `config.TrimTrailingPeriods(false)`, `config.SetApplicationCulture(...)`.
Examples: `AddExample(params string[])` at app, branch or command level.

## Settings inheritance pattern

```csharp
public class BaseSettings : CommandSettings
{
    [CommandOption("-v|--verbose")] public bool Verbose { get; init; }
}
public sealed class BuildSettings : BaseSettings
{
    [CommandArgument(0, "[project]")] public string? Project { get; init; }
}
```

## Output inside commands

Inject `IAnsiConsole` through the constructor (works even with the default registrar) and write
through it instead of static `AnsiConsole` — that is what makes `CommandAppTester` capture output
(`testing.md`). `config.ConfigureConsole(console)` swaps the console the app uses for help/errors
and the injected `IAnsiConsole`.

## Pitfalls checklist

- `public override int Execute(..., CancellationToken)` — `public`, three parameters.
- An array (vector) argument that isn't the last positional fails when that command runs:
  `Error: The command 'x' specifies an argument vector that is not the last argument.` (exit -1).
- `Dictionary<,>` option property → use `IDictionary<,>`.
- `-h`/`--help` are reserved. When an application version is set, a **first** argument of `-v` or
  `--version` prints the version; `tool run -v` still binds to your own `-v|--verbose` option
  (verified), but a bare `tool -v` will not reach it.
- Required info in `Validate()` runs *after* binding; parse-level errors (types, missing
  required) never reach it.
- Output through `Console.WriteLine` is fine, but styled output + tests should use the injected console.
- Unit-test with `Spectre.Console.Cli.Testing` rather than spawning processes.
