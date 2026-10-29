// Behaviour probes for claims in the writer skill that cannot be read off a signature.
// Compare each printed block with the statement it backs (listed below). If a result changes
// between versions, update the writer reference (and references/version.md).
using System.ComponentModel;
using Spectre.Console;
using Spectre.Console.Cli;
using Spectre.Console.Cli.Testing;
using Spectre.Console.Testing;

Console.WriteLine("CLAIMS UNDER TEST");
Console.WriteLine(" cli.md     : unknown cmd / missing arg / validation error / exception -> exit -1; --help -> 0; branch alone -> 1; no args + no default -> 0");
Console.WriteLine(" cli.md     : Dictionary<,> option fails, IDictionary<,> works; FlagValue<T> '--level' alone -> IsSet=true");
Console.WriteLine(" cli.md     : array argument must be last; ctor-bound settings work; Remaining.Parsed keys keep dashes");
Console.WriteLine(" cli.md     : first arg --version prints version; 'run -v' still binds to the user's -v");
Console.WriteLine(" testing.md : TestConsole is 80x24 and non-interactive; Ask works with queued input; SelectionPrompt needs Interactive()");
Console.WriteLine(" testing.md : empty input queue -> InvalidOperationException 'No input available.'");
Console.WriteLine(" ansi doc   : AnsiWriter(Ansi=false) emits plain text; EightBit red -> ESC[38;5;9m");
Console.WriteLine();

CliProbe.Run();
ConsoleProbe.Run();

public sealed class AddSettings : CommandSettings
{
    [CommandArgument(0, "<name>")] public string Name { get; init; } = "";
    [CommandOption("-c|--count")] [DefaultValue(1)] public int Count { get; init; } = 1;
    [CommandOption("-t|--tag <TAG>")] public string[] Tags { get; init; } = [];
    [CommandOption("-D|--define <KEY=VALUE>")] public IDictionary<string, string> Defines { get; init; } = new Dictionary<string, string>();
    [CommandOption("--level [LEVEL]")] public FlagValue<int> Level { get; init; } = new();
    public override ValidationResult Validate() => Count < 0 ? ValidationResult.Error("Count must be >= 0") : ValidationResult.Success();
}

public sealed class AddCommand : Command<AddSettings>
{
    public override int Execute(CommandContext c, AddSettings s, CancellationToken ct)
    {
        Console.WriteLine($"add {s.Name} count={s.Count} tags={string.Join("|", s.Tags)} defs={string.Join("|", s.Defines.Select(kv => kv.Key + "=" + kv.Value))} level.set={s.Level.IsSet}");
        return 0;
    }
}

public sealed class BoomCommand : Command
{
    public override int Execute(CommandContext c, CancellationToken ct) => throw new InvalidOperationException("bang");
}

public sealed class DictBad : CommandSettings
{
    [CommandOption("-D <KEY=VALUE>")] public Dictionary<string, string> D { get; init; } = new();
}

public sealed class DictBadCommand : Command<DictBad>
{
    public override int Execute(CommandContext c, DictBad s, CancellationToken ct) => 0;
}

public sealed class ArrFirst : CommandSettings
{
    [CommandArgument(0, "<files>")] public string[] Files { get; init; } = [];
    [CommandArgument(1, "<other>")] public string Other { get; init; } = "";
}

public sealed class ArrCommand : Command<ArrFirst>
{
    public override int Execute(CommandContext c, ArrFirst s, CancellationToken ct) => 0;
}

public sealed class RecSettings : CommandSettings
{
    public RecSettings(string name, int count) { Name = name; Count = count; }
    [CommandArgument(0, "<name>")] public string Name { get; }
    [CommandOption("-c|--count")] public int Count { get; }
}

public sealed class RecCommand : Command<RecSettings>
{
    public override int Execute(CommandContext c, RecSettings s, CancellationToken ct)
    {
        Console.WriteLine($"rec {s.Name} {s.Count} raw=[{string.Join(",", c.Remaining.Raw)}] parsed=[{string.Join(",", c.Remaining.Parsed.Select(g => g.Key + "=" + string.Join("/", g)))}]");
        return 0;
    }
}

public sealed class VSettings : CommandSettings
{
    [CommandOption("-v|--verbose")] public bool V { get; init; }
}

public sealed class VCommand : Command<VSettings>
{
    public override int Execute(CommandContext c, VSettings s, CancellationToken ct) { Console.WriteLine("v=" + s.V); return 0; }
}

public static class CliProbe
{
    static void Run(string title, Action<IConfigurator> cfg, params string[] args)
    {
        var app = new CommandAppTester();
        app.Configure(cfg);
        try
        {
            var r = app.Run(args);
            Console.WriteLine($"--- CLI {title}: exit={r.ExitCode}\n{r.Output}\n");
        }
        catch (Exception e)
        {
            Console.WriteLine($"--- CLI {title}: THROW {e.GetType().Name}: {e.Message}\n");
        }
    }

    public static void Run()
    {
        void Full(IConfigurator c)
        {
            c.SetApplicationName("demo");
            c.SetApplicationVersion("1.2.3");
            c.AddBranch("pkg", b => b.AddCommand<AddCommand>("add"));
            c.AddCommand<AddCommand>("add");
            c.AddCommand<BoomCommand>("boom");
            c.AddCommand<VCommand>("run");
        }

        Run("ok", Full, "add", "x", "-c", "3", "-t", "a", "-t", "b", "-D", "k=v", "--level", "5");
        Run("flagvalue alone", Full, "add", "x", "--level");
        Run("validation", Full, "add", "x", "-c", "-1");
        Run("missing arg", Full, "add");
        Run("unknown", Full, "nope");
        Run("exception", Full, "boom");
        Run("branch alone", Full, "pkg");
        Run("help", Full, "add", "--help");
        Run("--version", Full, "--version");
        Run("root no args", Full);
        Run("run -v", Full, "run", "-v");
        Run("Dictionary<,> option", c => c.AddCommand<DictBadCommand>("d"), "d", "-D", "k=v");
        Run("array not last", c => c.AddCommand<ArrCommand>("arr"), "arr", "a", "b");
        Run("ctor binding + remaining", c => c.AddCommand<RecCommand>("rec").WithAlias("r"), "r", "Ada", "-c", "2", "--unknown", "foo", "--", "x", "y");
    }
}

public static class ConsoleProbe
{
    public static void Run()
    {
        var tc = new TestConsole();
        tc.Write(new Panel("x"));
        Console.WriteLine($"--- TestConsole defaults: {tc.Profile.Width}x{tc.Profile.Height} interactive={tc.Profile.Capabilities.Interactive} out=[{tc.Output.Replace("\n", "|")}]");

        var t1 = new TestConsole();
        t1.Input.PushTextWithEnter("Ada");
        Console.WriteLine("--- Ask on non-interactive TestConsole: " + t1.Ask<string>("Name?"));

        var t2 = new TestConsole();
        t2.Input.PushKey(ConsoleKey.DownArrow);
        t2.Input.PushKey(ConsoleKey.Enter);
        try { Console.WriteLine("--- Selection non-interactive: " + t2.Prompt(new SelectionPrompt<string>().AddChoices("a", "b", "c"))); }
        catch (Exception e) { Console.WriteLine($"--- Selection non-interactive: {e.GetType().Name}: {e.Message}"); }

        var t3 = new TestConsole().Interactive();
        t3.Input.PushKey(ConsoleKey.DownArrow);
        t3.Input.PushKey(ConsoleKey.Enter);
        Console.WriteLine("--- Selection interactive: " + t3.Prompt(new SelectionPrompt<string>().AddChoices("a", "b", "c")));

        var t4 = new TestConsole().Interactive();
        t4.Input.PushKey(ConsoleKey.Spacebar);
        t4.Input.PushKey(ConsoleKey.DownArrow);
        t4.Input.PushKey(ConsoleKey.Spacebar);
        t4.Input.PushKey(ConsoleKey.Enter);
        Console.WriteLine("--- Multi interactive: " + string.Join(",", t4.Prompt(new MultiSelectionPrompt<string>().AddChoices("a", "b", "c"))));

        try { new TestConsole().Ask<string>("q"); }
        catch (Exception e) { Console.WriteLine($"--- Empty queue: {e.GetType().Name}: {e.Message}"); }

        var plain = new StringWriter();
        new AnsiWriter(plain, new AnsiCapabilities { Ansi = false }).Foreground(Color.Red).Write("x");
        var eight = new StringWriter();
        new AnsiWriter(eight, new AnsiCapabilities { Ansi = true, ColorSystem = ColorSystem.EightBit }).Foreground(new Color(255, 0, 0)).Write("x").ResetStyle();
        Console.WriteLine($"--- AnsiWriter ansi=false: [{plain}]  8bit: [{eight.ToString().Replace("\u001b", "<ESC>")}]");
    }
}
