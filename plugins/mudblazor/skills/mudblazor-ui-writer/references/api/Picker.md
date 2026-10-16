# Picker components — API (generated from source)

## MudPicker<T> : MudFormComponent<T, string>

Base class for MudBlazor pickers such as `MudDatePicker`, `MudTimePicker`, and `MudColorPicker`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `AdornmentColor` | `Color` | `Color.Default` | The color of the `AdornmentIcon`. Defaults to `Default`. |
| `AdornmentIcon` | `string` | `Icons.Material.Filled.Event` | The icon shown next to the text input. Defaults to `Event`. |
| `AdornmentAriaLabel` | `string?` | `null` | The `aria-label` for the adornment. Defaults to `null`. |
| `Placeholder` | `string?` | – | The text displayed in the input if no value is specified. This property is typically used to give the user a hint as to what kind of input is expected. |
| `PopupAriaLabel` | `string?` | `null`, which names the popup after `Label`, or `Placeholder` when there is no label` | The accessible name announced for the popup. Defaults to `null`, which names the popup after `Label`, or `Placeholder` when there is no label. Without any of these the popup is not announced as a dialog. |
| `PopupAriaLabelledBy` | `string?` | `null` | The id of the element that names the popup. Defaults to `null`. Takes precedence over `PopupAriaLabel` and the field text. |
| `PickerOpened` | `EventCallback` | – | Occurs when this picker has opened. |
| `PickerClosed` | `EventCallback` | – | Occurs when this picker has closed. |
| `Elevation` | `int?` | `8` for inline pickers; otherwise `0` | The size of the drop shadow. Defaults to `8` for inline pickers; otherwise `0`. A higher number creates a heavier drop shadow. Use a value of `0` for no shadow. |
| `Square` | `bool` | `false` | Disables rounded corners. Defaults to `false`. |
| `Rounded` | `bool` | `false` | Shows rounded corners. Defaults to `false`. When `true`, the `border-radius` style is set to the theme's default value. |
| `HelperText` | `string?` | – | The text displayed below the text field. This property is typically used to help the user understand what kind of input is allowed. The `HelperTextOnFocus` property controls when this text is visible. |
| `HelperTextOnFocus` | `bool` | `false` | Displays the `HelperText` only when this input has focus. Defaults to `false`. |
| `Label` | `string?` | – | The label for this input. If no value is specified, the label will be displayed in the input. Otherwise, it will be scaled down to the top of the input. |
| `Clearable` | `bool` | `false` | Displays the Clear icon button. Defaults to `false`. When `true`, an icon is displayed which, when clicked, clears the Text and Value. Use the `ClearIcon` property to control the Clear button icon. |
| `ClearIcon` | `string` | `Icons.Material.Filled.Clear` | Custom clear icon when `Clearable` is enabled. Defaults to `Clear`. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this button. Defaults to `false`. |
| `Underline` | `bool` | `true` | Shows an underline under the input text. Defaults to `true`. |
| `ReadOnly` | `bool` | `false` | Prevents the input from being changed by the user. Defaults to `false`. When `true`, the user can copy text in the control, but cannot change the value. |
| `Editable` | `bool` | `false` | Allows the value to be edited. Defaults to `false`. |
| `InputId` | `string?` | – | The ID of the input element. When set takes precedence over any internally generated IDs. When used with a range picker, the ID is suffixed with `-start` for the start input and `-end` for the end input. |
| `ShowToolbar` | `bool` | `true` | Shows the toolbar. Defaults to `true`. |
| `ToolbarClass` | `string?` | – | The CSS classes for the toolbar when `ShowToolbar` is `true`. Multiple classes must be separated by spaces. |
| `PickerVariant` | `PickerVariant` | `PickerVariant.Inline` | The display variant for this picker. Defaults to `Inline`. Other values are `Dialog` and `Static`. |
| `Variant` | `Variant` | `Variant.Text` | The display variant of the text input. Defaults to `Text`. |
| `Adornment` | `Adornment` | `Adornment.End` | The location of the `AdornmentIcon` for the input. Defaults to `End`. |
| `Orientation` | `Orientation` | `Orientation.Portrait` | The orientation of the picker when `PickerVariant` is `Static`. Defaults to `Portrait`. |
| `IconSize` | `Size` | `Size.Medium` | The size of the icon in the input field. Defaults to `Medium`. |
| `Color` | `Color` | `Color.Primary` | The color of the toolbar, selected, and active values. Defaults to `Primary`. |
| `TextChanged` | `EventCallback<string?>` | – | Occurs when `Text` has changed. |
| `ImmediateText` | `bool` | `false` | Updates `Text` immediately upon typing when `Editable` is `true`. Defaults to `false`. When `false`, `Text` is only updated when pressing `Enter` or upon loss of focus. |
| `OnClick` | `EventCallback<MouseEventArgs>` | – | Occurs when the text input has been clicked. |
| `ActionsClass` | `string?` | – | The currently selected value, as a string. Multiple classes must be separated by a space. |
| `PickerActions` | `RenderFragment<MudPicker<T>>?` | – | The custom action buttons to display. |
| `Margin` | `Margin` | `Margin.None` | The amount of vertical spacing for the text input. Defaults to `None`. |
| `ShrinkLabel` | `bool` | `false` | Shows the label inside the text input if no `Text` is specified. Defaults to `false`. When `true`, the label will not move into the input when the input is empty. |
| `Modal` | `bool?` | `ModalOverlay` | The mask to apply to input values when `Editable` is `true`. Defaults to `ModalOverlay`. Only possible to set to `false` when `PickerVariant` is `Inline`. |
| `AnchorOrigin` | `Origin` | `Origin.BottomLeft` | The location the popover opens, relative to its container. Defaults to `BottomLeft`. |
| `TransformOrigin` | `Origin` | `Origin.TopLeft` | The direction the popover opens, relative to its container. Defaults to `TopLeft`. |
| `RelativeWidth` | `DropdownWidth` | `DropdownWidth.Ignore` | Determines the width of the Popover dropdown in relation the parent container. Defaults to `Ignore`. When `Relative`, restricts the max-width of the component to the width of the parent container When `Adaptive`, restricts the min-width of the component to the width of the parent container |

## MudPickerContent : MudComponentBase

The content within a `MudPicker{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content to display. |

## MudPickerToolbar : MudComponentBase

The toolbar content of a `MudPicker{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ShowToolbar` | `bool` | `true` | Shows the toolbar. Defaults to `true`. |
| `Orientation` | `Orientation` | – | The display orientation of this toolbar. |
| `PickerVariant` | `PickerVariant` | – | The display variant for this toolbar. |
| `Color` | `Color` | – | The color of the toolbar, selected, and active values. |
| `ChildContent` | `RenderFragment?` | – | The content within this toolbar. |
