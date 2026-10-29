# prompts — API (generated from source)

## `public sealed class ConfirmationPrompt : IPrompt<bool>`

*core* · `src/Spectre.Console/Prompts/ConfirmationPrompt.cs`

A prompt that is answered with a yes or no.

**Constructors**

- `ConfirmationPrompt(string prompt)` — Initializes a new instance of the `ConfirmationPrompt` class.

**Properties**

- `char Yes { get; set; }` = `'y'` — Gets or sets the character that represents "yes".
- `char No { get; set; }` = `'n'` — Gets or sets the character that represents "no".
- `bool DefaultValue { get; set; }` = `true` — Gets or sets a value indicating whether "yes" is the default answer.
- `string InvalidChoiceMessage { get; set; }` = `"[red]Please select one of the available options[/]"` — Gets or sets the message for invalid choices.
- `bool ShowChoices { get; set; }` = `true` — Gets or sets a value indicating whether or not choices should be shown.
- `bool ShowDefaultValue { get; set; }` = `true` — Gets or sets a value indicating whether or not default values should be shown.
- `Style? DefaultValueStyle { get; set; }` — Gets or sets the style in which the default value is displayed. Defaults to green when `null`.
- `Style? ChoicesStyle { get; set; }` — Gets or sets the style in which the list of choices is displayed. Defaults to blue when `null`.
- `bool RequireEnter { get; set; }` = `true` — Gets or sets a value indicating whether or not the enter key is required after input
- `StringComparer Comparer { get; set; }` = `StringComparer.CurrentCultureIgnoreCase` — Gets or sets the string comparer to use when comparing user input against Yes/No choices.

**Methods**

- `bool Show(IAnsiConsole console)` — Shows the prompt.
- `async Task<bool> ShowAsync(IAnsiConsole console, CancellationToken cancellationToken)` — Shows the prompt asynchronously.

**Extension methods on this type** (call as `x.Method(...)`)

- `ShowChoices(bool show) -> ConfirmationPrompt` — Show or hide choices.
- `ShowChoices() -> ConfirmationPrompt` — Shows choices.
- `HideChoices() -> ConfirmationPrompt` — Hides choices.
- `ChoicesStyle(Style? style) -> ConfirmationPrompt` — Sets the style in which the list of choices is displayed.
- `ShowDefaultValue(bool show) -> ConfirmationPrompt` — Show or hide the default value.
- `ShowDefaultValue() -> ConfirmationPrompt` — Shows the default value.
- `HideDefaultValue() -> ConfirmationPrompt` — Hides the default value.
- `DefaultValueStyle(Style? style) -> ConfirmationPrompt` — Sets the style in which the default value is displayed.
- `InvalidChoiceMessage(string message) -> ConfirmationPrompt` — Sets the "invalid choice" message for the prompt.
- `Yes(char character) -> ConfirmationPrompt` — Sets the character to interpret as "yes".
- `No(char character) -> ConfirmationPrompt` — Sets the character to interpret as "no".
- `RequireEnter(bool require = true) -> ConfirmationPrompt` — Sets whether or not the enter key is required after input.

## `public interface IMultiSelectionItem<T> : ISelectionItem<T> where T : notnull`

*core* · `src/Spectre.Console/Prompts/IMultiSelectionItem.cs`

Represent a multi selection prompt item.

**Properties**

- `bool IsSelected { get; }` — Gets a value indicating whether or not this item is selected.

**Methods**

- `IMultiSelectionItem<T> Select()` — Selects the item.

## `public interface IPrompt<T>`

*core* · `src/Spectre.Console/Prompts/IPrompt.cs`

Represents a prompt.

**Methods**

- `T Show(IAnsiConsole console)` — Shows the prompt.
- `Task<T> ShowAsync(IAnsiConsole console, CancellationToken cancellationToken)` — Shows the prompt asynchronously.

## `public interface ISelectionItem<T> where T : notnull`

*core* · `src/Spectre.Console/Prompts/ISelectionItem.cs`

Represent a selection item.

**Methods**

- `ISelectionItem<T> AddChild(T child)` — Adds a child to the item.

## `public sealed class MultiSelectionPrompt<T> : IPrompt<List<T>>, IListPromptStrategy<T> where T : notnull`

*core* · `src/Spectre.Console/Prompts/MultiSelectionPrompt.cs`

Represents a multi selection list prompt.

**Constructors**

- `MultiSelectionPrompt(IEqualityComparer<T>? comparer = null)` — Initializes a new instance of the `MultiSelectionPrompt{T}` class.

**Properties**

- `string? Title { get; set; }` — Gets or sets the title.
- `int PageSize { get; set; }` = `10` — Gets or sets the page size. Defaults to `10`.
- `bool WrapAround { get; set; }` = `false` — Gets or sets a value indicating whether the selection should wrap around when reaching the edge. Defaults to `false`.
- `Style? HighlightStyle { get; set; }` — Gets or sets the highlight style of the selected choice.
- `Func<T, string>? Converter { get; set; }` — Gets or sets the converter to get the display string for a choice. By default the corresponding `TypeConverter` is used.
- `bool Required { get; set; }` = `true` — Gets or sets a value indicating whether or not at least one selection is required.
- `string? MoreChoicesText { get; set; }` — Gets or sets the text that will be displayed if there are more choices to show.
- `string? InstructionsText { get; set; }` — Gets or sets the text that instructs the user of how to select items.
- `SelectionMode Mode { get; set; }` = `SelectionMode.Leaf` — Gets or sets the selection mode. Defaults to `SelectionMode.Leaf`.
- `T? DefaultValue { get; set; }` — Gets or sets the choice to show as selected when the prompt is first displayed. By default the first choice is selected.
- `Func<List<T>>? CancelResult { get; set; }` — Gets or sets a Func that will be triggered if Cancel is triggered by the 'ESC' key.

**Methods**

- `IMultiSelectionItem<T> AddChoice(T item)` — Adds a choice.
- `List<T> Show(IAnsiConsole console)` — Shows the prompt.
- `async Task<List<T>> ShowAsync(IAnsiConsole console, CancellationToken cancellationToken)` — Shows the prompt asynchronously.
- `IEnumerable<T> GetParents(T item)` — Returns all parent items of the given `item`.
- `T? GetParent(T item)` — Returns the parent item of the given `item`.

**Extension methods on this type** (call as `x.Method(...)`)

- `Mode<T>(SelectionMode mode) -> MultiSelectionPrompt<T>` — Sets the selection mode.
- `AddChoices<T>(T choice, Action<IMultiSelectionItem<T>> configurator) -> MultiSelectionPrompt<T>` — Adds a choice.
- `AddChoices<T>(params T[] choices) -> MultiSelectionPrompt<T>` — Adds multiple choices.
- `AddChoices<T>(IEnumerable<T> choices) -> MultiSelectionPrompt<T>` — Adds multiple choices.
- `AddChoiceGroup<T>(T group, IEnumerable<T> choices) -> MultiSelectionPrompt<T>` — Adds multiple grouped choices.
- `AddChoiceGroup<T>(T group, params T[] choices) -> MultiSelectionPrompt<T>` — Adds multiple grouped choices.
- `Select<T>(T item) -> MultiSelectionPrompt<T>` — Marks an item as selected.
- `Title<T>(string? title) -> MultiSelectionPrompt<T>` — Sets the title.
- `PageSize<T>(int pageSize) -> MultiSelectionPrompt<T>` — Sets how many choices that are displayed to the user.
- `WrapAround<T>(bool shouldWrap = true) -> MultiSelectionPrompt<T>` — Sets whether the selection should wrap around when reaching its edges.
- `HighlightStyle<T>(Style highlightStyle) -> MultiSelectionPrompt<T>` — Sets the highlight style of the selected choice.
- `MoreChoicesText<T>(string? text) -> MultiSelectionPrompt<T>` — Sets the text that will be displayed if there are more choices to show.
- `InstructionsText<T>(string? text) -> MultiSelectionPrompt<T>` — Sets the text that instructs the user of how to select items.
- `NotRequired<T>() -> MultiSelectionPrompt<T>` — Requires no choice to be selected.
- `Required<T>() -> MultiSelectionPrompt<T>` — Requires a choice to be selected.
- `Required<T>(bool required) -> MultiSelectionPrompt<T>` — Sets a value indicating whether or not at least one choice must be selected.
- `UseConverter<T>(Func<T, string>? displaySelector) -> MultiSelectionPrompt<T>` — Sets the function to create a display string for a given choice.
- `AddCancelResult<T>(Func<List<T>> cancelResultFunc) -> MultiSelectionPrompt<T>` — Sets the value that will be returned if the prompt is cancelled with 'ESC'.
- `AddCancelResult<T>(List<T> cancelResult) -> MultiSelectionPrompt<T>` — Sets a Func that will be triggered if the prompt is cancelled with 'ESC'. Sets result to the configured List.
- `AddCancelResult<T>(T cancelResult) -> MultiSelectionPrompt<T>` — Sets a Func that will be triggered if the prompt is cancelled with 'ESC'. Sets result to a List containing only the configured item.
- `AddCancelResult<T>() -> MultiSelectionPrompt<T>` — Sets a Func that will be triggered if the prompt is cancelled with 'ESC'. Sets result to an empty List.
- `DefaultValue<T>(T? defaultValue) -> MultiSelectionPrompt<T>` — Sets the choice that will be selected when the prompt is first displayed.

## `public sealed class SelectionPrompt<T> : IPrompt<T>, IListPromptStrategy<T> where T : notnull`

*core* · `src/Spectre.Console/Prompts/SelectionPrompt.cs`

Represents a single list prompt.

**Constructors**

- `SelectionPrompt(IEqualityComparer<T>? comparer = null)` — Initializes a new instance of the `SelectionPrompt{T}` class.

**Properties**

- `string? Title { get; set; }` — Gets or sets the title.
- `int PageSize { get; set; }` = `10` — Gets or sets the page size. Defaults to `10`.
- `bool WrapAround { get; set; }` = `false` — Gets or sets a value indicating whether the selection should wrap around when reaching the edge. Defaults to `false`.
- `Style? HighlightStyle { get; set; }` — Gets or sets the highlight style of the selected choice.
- `Style? DisabledStyle { get; set; }` — Gets or sets the style of a disabled choice.
- `Style? SearchHighlightStyle { get; set; }` — Gets or sets the style of highlighted search matches.
- `string? SearchPlaceholderText { get; set; }` — Gets or sets the text that will be displayed when no search text has been entered.
- `Func<T, string>? Converter { get; set; }` — Gets or sets the converter to get the display string for a choice. By default the corresponding `TypeConverter` is used.
- `string? MoreChoicesText { get; set; }` — Gets or sets the text that will be displayed if there are more choices to show.
- `SelectionMode Mode { get; set; }` = `SelectionMode.Leaf` — Gets or sets the selection mode. Defaults to `SelectionMode.Leaf`.
- `bool SearchEnabled { get; set; }` — Gets or sets a value indicating whether or not search is enabled.
- `T? DefaultValue { get; set; }` — Gets or sets the choice to show as selected when the prompt is first displayed. By default the first choice is selected.
- `Func<T>? CancelResult { get; set; }` — Gets or sets a Func that will be triggered if Cancel is triggered by the 'ESC' key.

**Methods**

- `ISelectionItem<T> AddChoice(T item)` — Adds a choice.
- `T Show(IAnsiConsole console)` — Shows the prompt.
- `async Task<T> ShowAsync(IAnsiConsole console, CancellationToken cancellationToken)` — Shows the prompt asynchronously.

**Extension methods on this type** (call as `x.Method(...)`)

- `Mode<T>(SelectionMode mode) -> SelectionPrompt<T>` — Sets the selection mode.
- `AddChoices<T>(params T[] choices) -> SelectionPrompt<T>` — Adds multiple choices.
- `AddChoices<T>(IEnumerable<T> choices) -> SelectionPrompt<T>` — Adds multiple choices.
- `AddChoiceGroup<T>(T group, IEnumerable<T> choices) -> SelectionPrompt<T>` — Adds multiple grouped choices.
- `AddChoiceGroup<T>(T group, params T[] choices) -> SelectionPrompt<T>` — Adds multiple grouped choices.
- `Title<T>(string? title) -> SelectionPrompt<T>` — Sets the title.
- `PageSize<T>(int pageSize) -> SelectionPrompt<T>` — Sets how many choices that are displayed to the user.
- `WrapAround<T>(bool shouldWrap = true) -> SelectionPrompt<T>` — Sets whether the selection should wrap around when reaching its edges.
- `EnableSearch<T>() -> SelectionPrompt<T>` — Enables search for the prompt.
- `DisableSearch<T>() -> SelectionPrompt<T>` — Disables search for the prompt.
- `SearchPlaceholderText<T>(string? text) -> SelectionPrompt<T>` — Sets the text that will be displayed when no search text has been entered.
- `AddCancelResult<T>(Func<T> cancelResultFunc) -> SelectionPrompt<T>` — Sets the value that will be returned if the prompt is cancelled with 'ESC'.
- `AddCancelResult<T>(T cancelResult) -> SelectionPrompt<T>` — Sets a Func that will be triggered if the prompt is cancelled with 'ESC'.
- `HighlightStyle<T>(Style highlightStyle) -> SelectionPrompt<T>` — Sets the highlight style of the selected choice.
- `MoreChoicesText<T>(string? text) -> SelectionPrompt<T>` — Sets the text that will be displayed if there are more choices to show.
- `UseConverter<T>(Func<T, string>? displaySelector) -> SelectionPrompt<T>` — Sets the function to create a display string for a given choice.
- `DefaultValue<T>(T? defaultValue) -> SelectionPrompt<T>` — Sets the choice that will be selected when the prompt is first displayed.

## `public sealed class TextPrompt<T> : IPrompt<T>, IHasCulture`

*core* · `src/Spectre.Console/Prompts/TextPrompt.cs`

Represents a prompt.

**Constructors**

- `TextPrompt(string prompt, StringComparer? comparer = null)` — Initializes a new instance of the `TextPrompt{T}` class.

**Properties**

- `Style? PromptStyle { get; set; }` — Gets or sets the prompt style.
- `List<T> Choices { get; }` = `[]` — Gets the list of choices.
- `CultureInfo? Culture { get; set; }` — Gets or sets the culture to use when converting input to object.
- `string InvalidChoiceMessage { get; set; }` = `"[red]Please select one of the available options[/]"` — Gets or sets the message for invalid choices.
- `bool IsSecret { get; set; }` — Gets or sets a value indicating whether input should be hidden in the console.
- `char? Mask { get; set; }` = `'*'` — Gets or sets the character to use while masking a secret prompt.
- `string ValidationErrorMessage { get; set; }` = `"[red]Invalid input[/]"` — Gets or sets the validation error message.
- `bool ShowChoices { get; set; }` = `true` — Gets or sets a value indicating whether or not choices should be shown.
- `bool ShowDefaultValue { get; set; }` = `true` — Gets or sets a value indicating whether or not default values should be shown.
- `bool EditableDefaultValue { get; set; }` — Gets or sets the default value editable state that allows the injection of the DefaultValue in the text field. If true this places the DefaultValue in the input buffer which can then be edited by the user.
- `bool AllowEmpty { get; set; }` — Gets or sets a value indicating whether or not an empty result is valid.
- `bool ClearOnFinish { get; set; }` — Gets or sets a value indicating whether the prompt line should be cleared after a successful input.
- `Func<T, string>? Converter { get; set; }` = `TypeConverterHelper.ConvertToString` — Gets or sets the converter to get the display string for a choice. By default the corresponding `TypeConverter` is used.
- `Func<T, ValidationResult>? Validator { get; set; }` — Gets or sets the validator.
- `Style? DefaultValueStyle { get; set; }` — Gets or sets the style in which the default value is displayed. Defaults to green when `null`.
- `Style? ChoicesStyle { get; set; }` — Gets or sets the style in which the list of choices is displayed. Defaults to blue when `null`.

**Methods**

- `T Show(IAnsiConsole console)` — Shows the prompt and requests input from the user.
- `async Task<T> ShowAsync(IAnsiConsole console, CancellationToken cancellationToken)` — Shows the prompt asynchronously.

**Extension methods on this type** (call as `x.Method(...)`)

- `AllowEmpty<T>() -> TextPrompt<T>` — Allow empty input.
- `PromptStyle<T>(Style style) -> TextPrompt<T>` — Sets the prompt style.
- `ShowChoices<T>(bool show) -> TextPrompt<T>` — Show or hide choices.
- `ShowChoices<T>() -> TextPrompt<T>` — Shows choices.
- `HideChoices<T>() -> TextPrompt<T>` — Hides choices.
- `ShowDefaultValue<T>(bool show) -> TextPrompt<T>` — Show or hide the default value.
- `ShowDefaultValue<T>() -> TextPrompt<T>` — Shows the default value.
- `EditableDefaultValue<T>(bool state) -> TextPrompt<T>` — Whether or not to write the default value in the text input field to be modified by the end user.
- `HideDefaultValue<T>() -> TextPrompt<T>` — Hides the default value.
- `ValidationErrorMessage<T>(string message) -> TextPrompt<T>` — Sets the validation error message for the prompt.
- `InvalidChoiceMessage<T>(string message) -> TextPrompt<T>` — Sets the "invalid choice" message for the prompt.
- `DefaultValue<T>(T value) -> TextPrompt<T>` — Sets the default value of the prompt.
- `Validate<T>(Func<T, bool> validator, string? message = null) -> TextPrompt<T>` — Sets the validation criteria for the prompt.
- `Validate<T>(Func<T, ValidationResult> validator) -> TextPrompt<T>` — Sets the validation criteria for the prompt.
- `AddChoice<T>(T choice) -> TextPrompt<T>` — Adds a choice to the prompt.
- `AddChoices<T>(IEnumerable<T> choices) -> TextPrompt<T>` — Adds multiple choices to the prompt.
- `Secret<T>() -> TextPrompt<T>` — Replaces prompt user input with asterisks in the console.
- `Secret<T>(char? mask) -> TextPrompt<T>` — Replaces prompt user input with mask in the console.
- `WithConverter<T>(Func<T, string>? displaySelector) -> TextPrompt<T>` — Sets the function to create a display string for a given choice.
- `DefaultValueStyle<T>(Style? style) -> TextPrompt<T>` — Sets the style in which the default value is displayed.
- `ChoicesStyle<T>(Style? style) -> TextPrompt<T>` — Sets the style in which the list of choices is displayed.
- `ClearOnFinish<T>(bool clear = true) -> TextPrompt<T>` — Clears the prompt line after successful input.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IHasCulture`: `Culture`

## `public enum SelectionMode`

*core* · `src/Spectre.Console/Prompts/SelectionType.cs`

Represents how selections are made in a hierarchical prompt.

**Values**

- `Leaf = 0` — Will only return lead nodes in results.
- `Independent = 1` — Allows selection of parent nodes, but each node is independent of its parent and children.

