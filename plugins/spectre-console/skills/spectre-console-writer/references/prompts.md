# Prompts

Verified against `src/Spectre.Console/Prompts/**` and `Extensions/AnsiConsoleExtensions.Prompt.cs`
(0.57.2). Exact members: `api/prompts.md`.

All prompts implement `IPrompt<T>` (`Show(console)`, `ShowAsync(console, ct)`). Convenience on
`IAnsiConsole`/`AnsiConsole`: `Ask<T>`, `AskAsync<T>`, `Confirm`, `ConfirmAsync`, `Prompt(p)`,
`PromptAsync(p)`. **Overload asymmetry:** the static `AnsiConsole.Ask<T>(prompt, T defaultValue)` exists
only on the static class; the `IAnsiConsole` extension offers `Ask<T>(prompt)` and
`Ask<T>(prompt, CultureInfo?)` instead (use `new TextPrompt<T>(p).DefaultValue(x)` on an instance).

**Prompts need an interactive console.** On redirected stdin/stdout/stderr the real console
throws `InvalidOperationException("Failed to read input in non-interactive mode.")` (text/confirm
prompts) or `NotSupportedException("Cannot show selection prompt since the current terminal isn't
interactive.")` (selection prompts). Guard with `console.Profile.Capabilities.Interactive` or
catch and use defaults. They also take the exclusivity lock (don't prompt inside
`Progress`/`Status`/`Live`).

| Need | Prompt |
|---|---|
| free text / typed value (int, DateTime, enum, Guid…) | `TextPrompt<T>` / `Ask<T>` |
| password / secret | `TextPrompt<string>().Secret()` |
| yes/no | `ConfirmationPrompt` / `Confirm` |
| pick one | `SelectionPrompt<T>` |
| pick many | `MultiSelectionPrompt<T>` |

## Text / typed input

```csharp
var name = AnsiConsole.Ask<string>("What's your [green]name[/]?");
var age  = AnsiConsole.Ask<int>("Age?", 30);                      // static AnsiConsole only: Ask<T>(prompt, T defaultValue)
var when = AnsiConsole.Console.Ask<DateTime>("When?", System.Globalization.CultureInfo.InvariantCulture); // IAnsiConsole ext: Ask<T>(prompt, CultureInfo?)

var port = AnsiConsole.Prompt(
    new TextPrompt<int>("Port?")
        .DefaultValue(8080)
        .ValidationErrorMessage("[red]Not a valid port[/]")
        .Validate(p => p is > 0 and < 65536
            ? ValidationResult.Success()
            : ValidationResult.Error("[red]Port must be 1–65535[/]")));

var password = AnsiConsole.Prompt(
    new TextPrompt<string>("Password:")
        .PromptStyle("red")
        .Secret());                  // Secret('•') for a custom mask, Secret(null) = show nothing

var env = AnsiConsole.Prompt(
    new TextPrompt<string>("Environment?")
        .AddChoices(["dev", "staging", "prod"])
        .DefaultValue("dev")
        .HideDefaultValue()
        .AllowEmpty());
```

Behaviour:
- Re-prompts until the input converts to `T` (via `TypeConverter`/culture) and passes the validator.
  `ValidationErrorMessage` is printed when **conversion fails** and when a validator fails without
  its own message; `InvalidChoiceMessage` when the input isn't in `Choices`. Several `.Validate(...)`
  calls chain (all must pass, in order).
- Prompt text, default value display and error messages are **markup** (escape dynamic text).
- Default value is accepted with Enter. `EditableDefaultValue(true)` pre-fills the input line.
- Choices are matched against their display strings with the prompt's `StringComparer`
  (ctor arg; default **`OrdinalIgnoreCase`**); with `AddChoices` the user must type one of them
  (use `SelectionPrompt` for arrow-key UX).
- `ClearOnFinish()` removes the prompt line after a successful answer.
- `Culture` / `Ask<T>(prompt, culture)` controls parsing of numbers and dates.
- An empty answer: returns the `DefaultValue` if one is set; otherwise re-prompts unless
  `AllowEmpty()` (then empty input goes through conversion/validation — fine for `string`, a
  conversion error for `int` etc.).

## Confirmation

```csharp
if (AnsiConsole.Confirm("Delete everything?", defaultValue: false)) { /* … */ }

var ok = AnsiConsole.Prompt(
    new ConfirmationPrompt("Continue?") { DefaultValue = true, ShowChoices = true }
        .Yes('j').No('n'));   // custom characters (e.g. localisation)
```

Enter-less answers: `RequireEnter(false)`.

## SelectionPrompt (single choice, arrow keys)

```csharp
var fruit = AnsiConsole.Prompt(
    new SelectionPrompt<string>()
        .Title("What's your [green]favorite fruit[/]?")
        .PageSize(8)
        .WrapAround()
        .MoreChoicesText("[grey](Move up and down to reveal more)[/]")
        .EnableSearch()
        .SearchPlaceholderText("type to filter")
        .AddChoices("Apple", "Banana", "Cherry"));
```

- Items can be any `T : notnull`; display text comes from `UseConverter(x => "…")`
  (markup allowed) — **return the object, show a string**:

```csharp
public record Project(string Name, int Id);
```

```csharp
var project = AnsiConsole.Prompt(
    new SelectionPrompt<Project>()
        .Title("Pick a project")
        .UseConverter(p => $"{p.Name} [grey]#{p.Id}[/]")
        .AddChoices(new Project("Alpha", 1), new Project("Beta", 2)));
```
  Choice strings are parsed as markup: wrap user data in `Markup.Escape`.
- Groups: `AddChoiceGroup(parent, children)` or `AddChoice(x).AddChild(y)`. `Mode(SelectionMode.Leaf)`
  (default) means only leaves are selectable; `SelectionMode.Independent` makes parents
  selectable too. (There is no per-item "disabled" API — `DisabledStyle` styles the non-selectable
  group headers.)
- `DefaultValue(x)` pre-highlights an item (otherwise the first). Comparer for custom
  equality: `new SelectionPrompt<T>(IEqualityComparer<T>)`.
- `AddCancelResult(value)` makes **Esc** return `value` instead of being ignored.
- `HighlightStyle`, `SearchHighlightStyle`, `DisabledStyle` for look & feel.
- Long lists: always set `PageSize` and `EnableSearch()`.
- `ShowAsync(console, ct)` supports cancellation.

## MultiSelectionPrompt

```csharp
var toppings = AnsiConsole.Prompt(
    new MultiSelectionPrompt<string>()
        .Title("Pick [green]toppings[/]")
        .NotRequired()                      // default is Required()
        .PageSize(10)
        .InstructionsText("[grey](Space = toggle, Enter = accept)[/]")
        .AddChoiceGroup("Veg", ["Onion", "Pepper"])
        .AddChoices("Cheese", "Ham"));      // returns List<string>

var preselected = new MultiSelectionPrompt<string>()
    .AddChoices("a", "b", "c")
    .Select("b");                           // pre-tick "b"
```

Returns `List<T>`. `Required` (default) forces ≥1 selection. `AddChoices(item, configure)` lets
you `item.Select()` or add children per item. Space toggles, Enter accepts. In `Leaf` mode
(default) toggling a group header selects/deselects all its leaves and a parent shows as
selected when all its children are; the **result contains leaves only**. In `Independent`
mode every node toggles on its own and parents can be returned.

## Patterns

- **Wizard flow**: sequential prompts; wrap in a `Rule`/`Panel` per step; keep the answers in a record.
- **Re-prompting on domain errors**: use `Validate` (returns message) rather than looping yourself.
- **Menus**: loop `SelectionPrompt<MenuItem>` until `Exit`; use `Console.Clear()`/`AnsiConsole.Clear()`
  between screens.
- **Scripting/CI**: take values from CLI args/env, and only prompt when
  `AnsiConsole.Profile.Capabilities.Interactive`.
- **Testing**: queue keystrokes on `TestConsole.Input` (see `testing.md`) — e.g.
  `console.Input.PushTextWithEnter("42")`, `PushKey(ConsoleKey.DownArrow)`, `PushKey(ConsoleKey.Enter)`.
