# Testing console output and prompts

Packages: `Spectre.Console.Testing` (core), `Spectre.Console.Cli.Testing` (CLI). Verified
against `src/Spectre.Console.Testing/**` and the CLI repo's `Spectre.Console.Cli.Testing/**`
(0.57.2). Members: `api/testing.md`, `api/cli-testing.md`.

## Make code testable

Accept `IAnsiConsole` (constructor/parameter) instead of calling `AnsiConsole.*`:

```csharp
public sealed class Greeter(IAnsiConsole console)
{
    public string Run()
    {
        var name = console.Ask<string>("Name?");
        console.MarkupLine($"Hello, [green]{Markup.Escape(name)}[/]!");
        return name;
    }
}
```

## TestConsole

```csharp
using var console = new TestConsole()
    .Width(60)                       // default is 80x24; set it explicitly for wrapping tests
    .Colors(ColorSystem.TrueColor)   // default TrueColor; ColorSystem.NoColors to mimic NO_COLOR
    .Interactive();                  // needed for SelectionPrompt/MultiSelectionPrompt (see below)

console.Input.PushTextWithEnter("Ada");           // answers the Ask<string>
var result = new Greeter(console).Run();

// result == "Ada"
// console.Output contains "Hello, Ada!"
// console.Lines[0].Trim() == "Name? Ada"
```

How it behaves (from `TestConsole.cs`):
- Defaults: 80×24, TrueColor, `Capabilities.Ansi = true`, Unicode on, **Interactive off** (see
  prompts note below), no CI
  enrichers, exclusivity checks disabled (`NoopExclusivityMode`), no-op cursor.
- `Output` is the **plain text** of everything written (segment text only, control codes
  skipped) — no ANSI escapes, even though `Capabilities.Ansi` is true. Call `.EmitAnsiSequences()`
  (or set the property) when you need to assert on the actual escape codes / styling.
- `SupportsAnsi(bool)`, `SupportsUnicode(bool)` change *capabilities* (affecting borders, spinners,
  link support), not whether escapes are emitted.
- `Lines` = `Output` split on newlines (trailing newline trimmed).
- Members: `Output`, `Lines`, `Width(n)`, `Height(n)`, `Size(...)`, `Colors(...)`, `SupportsAnsi`,
  `SupportsUnicode`, `Interactive()`, `EmitAnsiSequences()`, `Profile`, `Input`.

`TestConsole.Input` (`TestConsoleInput`): `PushText(s)`, `PushTextWithEnter(s)`,
`PushCharacter(c)`, `PushKey(ConsoleKey)`, `PushKey(ConsoleKeyInfo)`. When the queue is empty a
read throws `InvalidOperationException("No input available.")` — which is how a test notices a
prompt asking more questions than you scripted.

**Interactive vs prompts** (verified by running them): `Ask<T>`/`TextPrompt`/`Confirm` read from
`console.Input` and work on a default (non-interactive) `TestConsole`. `SelectionPrompt` and
`MultiSelectionPrompt` throw `NotSupportedException("Cannot show selection prompt since the current
terminal isn't interactive.")` unless you call `.Interactive()`.

Driving selection prompts:

```csharp
using var console = new TestConsole().Interactive();
console.Input.PushKey(ConsoleKey.DownArrow);   // move to 2nd item
console.Input.PushKey(ConsoleKey.Enter);       // accept

var choice = console.Prompt(new SelectionPrompt<string>().AddChoices("a", "b", "c"));
// choice == "b"
```

Multi-selection: `PushKey(ConsoleKey.Spacebar)` toggles, `PushKey(ConsoleKey.Enter)` accepts.
(`main` after 0.57.2 stops `TestConsoleInput` producing characters for navigation keys; on 0.57.2
arrow-key pushes work for prompts as shown.)

Widget snapshot tests:

```csharp
var console = new TestConsole().Width(40);
console.Write(new Panel("hello").RoundedBorder());
var text = console.Output;       // includes the box-drawing characters
```

Notes:
- Live displays/progress under `TestConsole` use their non-interactive fallbacks unless you make
  the console interactive *and* ANSI-capable; test your logic, not the animation.
- This is the package Spectre's own tests use (with Verify snapshots).

## Testing Spectre.Console.Cli apps

```csharp
public sealed class HelloCommand(IAnsiConsole console) : Command<HelloCommand.Settings>
{
    public sealed class Settings : CommandSettings
    {
        [CommandArgument(0, "<name>")] public string Name { get; init; } = "";
    }

    public override int Execute(CommandContext context, Settings settings, CancellationToken cancellationToken)
    {
        console.MarkupLine($"Hello {Markup.Escape(settings.Name)}");
        return 0;
    }
}

public static class HelloTests
{
    public static void Run()
    {
        var app = new CommandAppTester();                 // default registrar: commands need a parameterless ctor!
        app.SetDefaultCommand<HelloCommand>();
        app.Configure(c => c.PropagateExceptions());
        var result = app.Run("Ada");
        // result.ExitCode == 0; result.Output == "Hello Ada"
    }
}
```

`CommandAppTester` (members in `api/cli-testing.md`):
- `SetDefaultCommand<T>()`, `Configure(Action<IConfigurator>)` (**once only** — second call throws).
- `Run(params string[] args)` → `CommandAppResult { ExitCode, Output, Context, Settings }`;
  `RunAsync(string[]? args, CancellationToken)` (**takes an array, not params**).
- `RunAndCatch<TException>(params string[] args)` → `CommandAppFailure { Exception, Output }`
  for asserting on expected failures (throws if no exception occurs).
- `Console` property: the `TestConsole` the app is configured with (default width is
  `int.MaxValue`, so output is never wrapped). `Output` is normalized and trimmed per line
  unless `new CommandAppTesterSettings { TrimConsoleOutput = false }`.
- Constructor `CommandAppTester(ITypeRegistrar? registrar = null, CommandAppTesterSettings? = null, TestConsole? = null)`.
  The default registrar constructor-injects registered services into commands, and the CLI itself
  registers `IAnsiConsole` (the console configured via `ConfigureConsole`, i.e. the tester's
  `TestConsole`) — so `HelloCommand(IAnsiConsole console)` above works with no custom registrar
  (verified). Pass your own `ITypeRegistrar` only for your other dependencies (`cli.md`, DI).
- Output only reaches `Output` if the command writes through that injected `IAnsiConsole`.
  Writes via static `AnsiConsole.*` go to the real console.
