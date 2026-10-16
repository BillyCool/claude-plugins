# Input components — API (generated from source)

## MudDebouncedInput<T> : MudBaseInput<T>

Base class for MudBlazor inputs that wait for typing to pause before updating their value, such as `MudTextField{T}` and `MudNumericField{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `DebounceInterval` | `double` | – | The number of milliseconds to wait before updating the `Text` value. |
| `OnDebounceIntervalElapsed` | `EventCallback<string>` | – | Occurs when the `DebounceInterval` has elapsed. The value in `Text` is included in this event. |

## MudInput<T> : MudBaseInput<T>

Renders the underlying HTML input element used by text-based components such as `MudTextField{T}` and `MudNumericField{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `InputType` | `InputType` | `InputType.Text` | The type of input collected by this component. Defaults to `Text`. Represents a valid HTML5 input type. |
| `ChildContent` | `RenderFragment?` | – | The content within this input component. Will only display if `InputType` is `Hidden`. |
| `OnIncrement` | `EventCallback` | – | Occurs when the `Up` arrow button is clicked. Only occurs when `InputType` is `Number`. For numeric inputs, use the `MudNumericField{T}` component. |
| `OnDecrement` | `EventCallback` | – | Occurs when the `Down` arrow button is clicked. Only occurs when `InputType` is `Number`. For numeric inputs, use the `MudNumericField{T}` component. |
| `HideSpinButtons` | `bool` | `true` | For `MudNumericField{T}`, hides the spin buttons. Defaults to `true`. |
| `Clearable` | `bool` | `false` | Shows a button to clear this input's value. Defaults to `false`. |
| `OnClearButtonClick` | `EventCallback<MouseEventArgs>` | – | Occurs when the clear button is clicked. When clicked, the `Text` and `Value` properties are reset. |
| `ClearIcon` | `string` | `Icons.Material.Filled.Clear` | The icon to display when `Clearable` is `true`. Defaults to `Clear`. |
| `NumericUpIcon` | `string` | `Icons.Material.Filled.KeyboardArrowUp` | The icon to display for the `Up` arrow button. Defaults to `KeyboardArrowUp`. |
| `NumericDownIcon` | `string` | `Icons.Material.Filled.KeyboardArrowDown` | The icon to display for the `Down` arrow button. Defaults to `KeyboardArrowDown`. |
| `Sizing` | `InputSizing` | `InputSizing.Fixed` | Defines the resizing behavior of this input. Defaults to `Fixed`. |
| `MaxLines` | `int` | `0` | The maximum vertical lines to display when `Sizing` is `Auto`. Defaults to `0`. When `0`. this property is ignored. |

## MudInputString : MudInput<string>

An input component for collecting alphanumeric values.

_No own parameters — see base class `MudInput<string>`._

## MudInputAdornment

An icon displayed within an input component.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Class` | `string?` | – | The CSS classes for this adornment. Multiple classes must be separate by spaces. |
| `Text` | `string?` | – | The text for this adornment. |
| `Icon` | `string?` | – | The icon for this adornment. |
| `Placement` | `Adornment` | `None` | Specifies the position of the adornment within the field. Defaults to `None`. |
| `Size` | `Size` | `Size.Medium` | The size of the icon. Defaults to `Medium`. |
| `Color` | `Color` | `Color.Default` | The color of the icon button. Defaults to `Default`. |
| `AriaLabel` | `string?` | – | The accessible name for this adornment. More information on accessible names can be found here. |
| `AdornmentClick` | `EventCallback<MouseEventArgs>` | – | Occurs when this adornment is clicked. |

## MudInputLabel : MudComponentBase

A label which describes a `MudInput{T}` component.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this label. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this label. Defaults to `false`. |
| `Error` | `bool` | `false` | Displays this label in an error state. Defaults to `false`. |
| `Variant` | `Variant` | `Variant.Text` | The display variant of this label. Defaults to `Text`. |
| `Margin` | `Margin` | `Margin.None` | The amount of vertical spacing to apply. Defaults to `None`. |
| `ForId` | `string` | `string.Empty` | For WCAG accessibility, the ID of the input component related to this label. Defaults to an empty string. |

## MudRangeInput<T> : MudBaseInput<Range<T>>

Collects start and end values that define a range using two input fields, as used by the `MudDateRangePicker`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `InputType` | `InputType` | `InputType.Text` | The type of input collected by this component. Defaults to `Text`. Represents a valid HTML5 input type. |
| `PlaceholderStart` | `string?` | – | The hint displayed before the user enters a starting value. |
| `PlaceholderEnd` | `string?` | – | The hint displayed before the user enters an ending value. |
| `StartInputAriaLabel` | `string?` | `a localized `Start` label when `null` | The accessible name for the starting input field. Defaults to a localized `Start` label when `null`. |
| `EndInputAriaLabel` | `string?` | `a localized `End` label when `null` | The accessible name for the ending input field. Defaults to a localized `End` label when `null`. |
| `OnClearButtonClick` | `EventCallback<MouseEventArgs>` | – | Occurs when the Clear button is clicked. When clicked, the `Text` and `Value` properties are reset. |
| `Clearable` | `bool` | `false` | Shows a button at the end of the input to clear the value. Defaults to `false`. When `true`, an icon is displayed which, when clicked, clears the Text and Value. Use the `ClearIcon` property to control the Clear button icon. |
| `ClearIcon` | `string` | `Icons.Material.Filled.Clear` | Custom clear icon when `Clearable` is enabled. Defaults to `Clear`. |
| `ChildContent` | `RenderFragment?` | – | The content within this input component. Will only display if `InputType` is `Hidden`. |
| `SeparatorIcon` | `string` | `Icons.Material.Filled.ArrowRightAlt` | The icon shown in between start and end values. Defaults to `ArrowRightAlt`. |
