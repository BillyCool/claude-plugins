# Shared base classes — API (generated from source)

Every `Mud*` component ultimately inherits `MudComponentBase`, so all
components accept these parameters in addition to their own.

## ComponentBaseWithState : ComponentBase

Base class for Blazor components that track parameter changes and manage state through MudBlazor's parameter framework, such as `MudComponentBase`.

_No own parameters._

## MudBaseBindableItemsControl<TChildComponent, TData> : MudBaseItemsControl<TChildComponent>

Base class for item container components that bind to a data source and render each item through a template, such as `MudCarousel{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ItemsSource` | `IEnumerable<TData>?` | – | The alternate source of items if `Items` is not set. |
| `ItemTemplate` | `RenderFragment<TData>?` | – | The template used to display each item. |

## MudBaseButton : MudComponentBase

Base class for clickable button components such as `MudButton`, `MudFab`, and `MudIconButton`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `HtmlTag` | `string` | `"button"` | The HTML tag rendered for this component. Defaults to button, or a if `Href` is set. |
| `ButtonType` | `ButtonType` | `Button` | The type of button. Defaults to `Button`. Other values are `Submit` to submit a form, and `Reset` to clear a form. |
| `Href` | `string?` | `null` | The URL to navigate to when the button is clicked. Defaults to `null`. When clicked, the browser will navigate to this URL. Use the `Target` property to target a specific tab. |
| `Target` | `string?` | `null` | The browser tab/window opened when a click occurs and `Href` is set. Defaults to `null`. This property allows navigation to open a new tab/window or to reuse a specific tab. Possible values are `_blank`, `_self`, `_parent`, `_top`, `noopener`, or the name of an `iframe` element. |
| `Rel` | `string?` | – | The relationship between the current document and the linked document when `Href` is set. This property is typically used by web crawlers to get more information about a link. Common values can be found here: <see href="https://www.w3schools.com/tags/att_a_rel.asp" /> |
| `Disabled` | `bool` | `false` | Allows the user to interact with this button. Defaults to `false`. |
| `ClickPropagation` | `bool` | `false` | Allows the click event to bubble up to the parent component. Defaults to `false`. |
| `DropShadow` | `bool` | `true` | Displays a shadow. Defaults to `true`. |
| `Ripple` | `bool` | `true` | Shows a ripple effect when the user clicks the button. Defaults to `true`. |
| `OnClick` | `EventCallback<MouseEventArgs>` | – | Occurs when this button has been clicked. |

## MudBaseInput<T> : MudFormComponent<T, string>

Base class for MudBlazor form input components such as `MudTextField{T}`, `MudNumericField{T}`, and `MudSelect{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Disabled` | `bool` | `false` | Allows the component to receive input. Defaults to `false`. |
| `ReadOnly` | `bool` | `false` | Prevents the input from being changed by the user. Defaults to `false`. When `true`, the user can copy text in the control, but cannot change the `Value`. |
| `FullWidth` | `bool` | `false` | Fills the full width of the parent container. Defaults to `false`. |
| `Immediate` | `bool` | `false` | Changes the `Value` as soon as input is received. Defaults to `false`. When `true`, the `Value` property will be updated any time user input occurs. Otherwise, `Value` is updated when the user presses `Enter` or the input loses focus. |
| `Underline` | `bool` | `true` | Displays an underline for the input. Defaults to `true`. |
| `HelperId` | `string?` | `null` | The ID of the helper element, for use by `aria-describedby`. Defaults to `null`. When set it is appended to the `aria-describedby` attribute to improve accessibility for users. This ID takes precedence over the helper element rendered when `HelperText` is provided. |
| `HelperText` | `string?` | – | The text displayed below the text field. This property is typically used to help the user understand what kind of input is allowed. The `HelperTextOnFocus` property controls when this text is visible. |
| `HelperTextOnFocus` | `bool` | `false` | Displays the `HelperText` only when this input has focus. Defaults to `false`. |
| `AdornmentIcon` | `string?` | `null` | The icon displayed for the adornment. Defaults to `null`. This icon will be displayed when `Adornment` is `Start` or `End`, and no value for `AdornmentText` is set. |
| `AdornmentText` | `string?` | `null` | The text displayed for the adornment. Defaults to `null`. This text will be displayed when `Adornment` is `Start` or `End`. The `AdornmentIcon` property will be ignored if this property is set. |
| `Adornment` | `Adornment` | `Adornment.None` | The location of the adornment icon or text. Defaults to `None`. When set to `Start` or `End`, the `AdornmentText` will be displayed, or `AdornmentIcon` if no adornment text is specified. |
| `OnlyValidateIfDirty` | `bool` | `false` | Limits validation to when the user changes the `Value`. Defaults to `false`. When `true`, validation only occurs if the user has changed the input value at least once. |
| `AdornmentColor` | `Color` | `Color.Default` | The color of `AdornmentText` or `AdornmentIcon`. Defaults to `Default`. Theme colors are supported. |
| `AdornmentAriaLabel` | `string?` | `null` | The `aria-label` for the adornment. Defaults to `null`. |
| `IconSize` | `Size` | `Size.Medium` | The size of the icon. Defaults to `Medium`. |
| `OnAdornmentClick` | `EventCallback<MouseEventArgs>` | – | Occurs when the adornment icon (but not the text) has been clicked. |
| `Variant` | `Variant` | `Variant.Text` | The appearance variation to use. Defaults to `Text`. |
| `Margin` | `Margin` | `Margin.None` | The amount of vertical spacing for this input. Defaults to `None`. |
| `Typo` | `Typo` | `Typo.subtitle1` | Typography for the input text. |
| `Placeholder` | `string?` | – | The text displayed in the input if no `Value` is specified. This property is typically used to give the user a hint as to what kind of input is expected. |
| `Counter` | `int?` | `null` | The optional character count and stop count. Defaults to `null`. When `0`, the current character count is displayed. When `1` or greater, the character count and this count are displayed. |
| `MaxLength` | `int` | `524288` | The maximum number of characters allowed. Defaults to `524288`. This value is typically set to a maximum length such as the size of a database column the value will be persisted to. |
| `Label` | `string?` | – | The label for this input. If no `Value` is specified, the label will be displayed in the input. Otherwise, it will be scaled down to the top of the input. |
| `AutoFocus` | `bool` | `false` | Automatically receives focus. Defaults to `false`. When `true`, the input will receive focus automatically. |
| `Lines` | `int` | `1` | A multiline input (textarea) will be shown, if set to more than one line. |
| `Text` | `string?` | – | The text displayed in the input. |
| `InputMode` | `InputMode` | `InputMode.text` | The type of input expected. Defaults to `text`. |
| `Pattern` | `string?` | `null` | The regular expression used to validate the `Value` property. Defaults to `null`. This property is used to validate the input against a regular expression. Not supported if `Lines` is `2` or greater. Must be a valid JavaScript regular expression. |
| `ShrinkLabel` | `bool` | `false` | Shows the label inside the input if no `Value` is specified. Defaults to `false`. When `true`, the label will not move into the input when the input is empty. |
| `TextChanged` | `EventCallback<string?>` | – | Occurs when the `Text` property has changed. |
| `OnBlur` | `EventCallback<FocusEventArgs>` | – | Occurs when the input loses focus. |
| `OnInternalInputChanged` | `EventCallback<string?>` | – | Occurs when the internal text value has changed. |
| `OnKeyDown` | `EventCallback<KeyboardEventArgs>` | – | Occurs when a key has been pressed down. |
| `KeyDownPreventDefault` | `bool` | – | Allows the default key-down action to occur. When `true`, the browser will not perform its default behavior when a key-down occurs. This is typically used when a key-down needs to override a browser's default behavior. |
| `OnKeyUp` | `EventCallback<KeyboardEventArgs>` | – | Occurs when a pressed key has been released. |
| `KeyUpPreventDefault` | `bool` | – | Prevents the default key-up action. When `true`, the browser will not perform its default behavior when a key-up occurs. This is typically used when a key-up needs to override the browser's default behavior. |
| `ValueChanged` | `EventCallback<T?>` | – | Occurs when the `Value` property has changed. |
| `Value` | `T?` | – | The value for this input. This property represents the strongly typed value for the input. It is typically the result of parsing raw input via the `Text` property. |
| `Format` | `string?` | – | The format applied to values. This property is passed into the `ToString()` method of the `Value` property, such as formatting `int`, `float`, `DateTime` and `TimeSpan` values. |
| `InputId` | `string?` | – | The ID of the input element. When set takes precedence over any internally generated IDs. |

## MudBaseItemsControl<TChildComponent> : MudComponentBase

Base class for components that manage a collection of child items with a selected index, such as `MudCarousel{T}` and `MudTimeline`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this component. |
| `SelectedIndexChanged` | `EventCallback<int>` | – | The index of the currently selected item. When this property changes, the `SelectedIndexChanged` event occurs. |

## MudBooleanInput<T> : MudFormComponent<T?, bool?>

Base class for form inputs backed by a boolean value, such as `MudCheckBox{T}`, `MudSwitch{T}`, and `MudRadio{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this input. Defaults to `false`. |
| `ReadOnly` | `bool` | `false` | Prevents the user from changing the input. Defaults to `false`. When `true`, the user can copy the input but cannot change it. |
| `Value` | `T?` | – | The currently selected value. |
| `StopClickPropagation` | `bool` | `true` | Prevents the parent component from receiving click events. Defaults to `true`. When `true`, the click will not bubble up to parent components. |
| `LabelPlacement` | `Placement` | `Placement.End` | The location of the label relative to the input icon. |
| `Label` | `string?` | – | The text/label will be displayed next to the switch if set. |
| `Ripple` | `bool` | `true` | Shows a ripple effect when button is clicked. Default is `true`. |
| `Size` | `Size` | `Size.Medium` | The Size of the component. |
| `Color` | `Color` | `Color.Default` | The color of the component. It supports the theme colors. |
| `ChildContent` | `RenderFragment?` | – | The content within this component. |
| `ValueChanged` | `EventCallback<T?>` | – | Occurs when the `Value` has changed. |

## MudComponentBase : ComponentBaseWithState

Base class for every MudBlazor component, supplying the shared `Class`, `Style`, `Tag`, and `UserAttributes` parameters.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Class` | `string?` | `null` | The CSS classes applied to this component. Defaults to `null`. You can use spaces to separate multiple classes. Use the `Style` property to apply custom CSS styles. |
| `Style` | `string?` | `null` | The CSS styles applied to this component. Defaults to `null`. Use the `Class` property to apply CSS classes. |
| `Tag` | `object?` | – | The arbitrary object to link to this component. This property is typically used to associate additional information with this component, such as a model containing data for this component. |
| `UserAttributes` | `Dictionary<string, object?>` | `new Dictionary<string, object?>()` | The additional HTML attributes to apply to this component. This property is typically used to provide additional HTML attributes during rendering such as ARIA accessibility tags or a custom ID. |

## MudFormComponent<T, U> : MudComponentBase

Base class for form components that support validation, error messages, and value conversion, such as `MudBaseInput{T}` and `MudBooleanInput{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Required` | `bool` | `false` | Requires an input value. Defaults to `false`. When `true`, an error with the text in `RequiredError` will be shown during validation if no input was given. |
| `RequiredError` | `string` | `string.Empty` | The error text displayed during validation when `Required` is `true` and no input was given. If left empty, a localized default message is used instead. See `ResolvedRequiredErrorText` for the logic that resolves the effective text to display. |
| `ErrorText` | `string?` | – | The text displayed if the `Error` property is `true`. |
| `ErrorTextChanged` | `EventCallback<string?>` | – | Raised when the `ErrorText` parameter value changes. This callback is triggered to support two-way binding of the `ErrorText` parameter. The callback receives the updated `ErrorText` value. |
| `Error` | `bool` | `false` | Displays an error. Defaults to `false`. When `true`, the text in `ErrorText` is displayed. |
| `ErrorChanged` | `EventCallback<bool>` | – | Raised when the `Error` parameter value changes. This callback is triggered to support two-way binding of the `Error` parameter. The callback receives the updated `Error` value. |
| `ErrorId` | `string?` | `null` | The ID of the error description element, for use by `aria-describedby` when `Error` is `true`. Defaults to `null`. When set and the `Error` property is `true`, an `aria-describedby` attribute is rendered to improve accessibility for users. |
| `ErrorIdChanged` | `EventCallback<string?>` | – | Raised when the `ErrorId` parameter value changes. This callback is triggered to support two-way binding of the `ErrorId` parameter. The callback receives the updated `ErrorId` value. |
| `Converter` | `IConverter<T?, U?>?` | – | The type converter for this input. This property provides a way to customize conversions between <typeparamref name="T"/> objects and <typeparamref name="U"/> values. You can assign `null` to this property; in that case, the component will use the default converter returned by `GetDefaultConverter`. |
| `Culture` | `CultureInfo` | `CultureInfo.CurrentUICulture` | The culture used to format and interpret values such as dates and currency. Defaults to `InvariantCulture`. |
| `Validation` | `object?` | – | The function used to detect problems with the input. When using a `MudForm`, this property can be any of several kinds of functions: 1. A `Func&lt;T,bool&gt;` or `Func&lt;T,Task&lt;bool&gt;&gt;` function. Returns `true` if valid. When `false`, a standard `"Invalid"` message is shown. 2. A `Func&lt;T,string&gt;` or `Func&lt;T,Task&lt;string&gt;&gt;` function. Returns `null` if valid, or a string explaining the error. 3. A `Func&lt;T,IEnumerable&lt;string&gt;&gt;` or `Func&lt;T,Task&lt;IEnumerable&lt;string&gt;&gt;&gt;` function. Returns an empty list if valid, or a list of validation errors. 3. A `Func&lt;object,string,IEnumerable&lt;string&gt;&gt;` or `Func&lt;object,string,Task&lt;IEnumerable&lt;string&gt;&gt;&gt;` function. Given the form model and path to the member, returns an empty list if valid, or a list of validation errors. 4. A `ValidationAttribute` object. |
| `For` | `Expression<Func<T>>?` | – | The model field containing validation attributes. When using an `EditForm`, this property is used to find data annotation validation attributes such as `MaxLengthAttribute` used to perform validation. |
