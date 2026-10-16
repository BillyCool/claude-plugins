# Form components — API (generated from source)

## MudForm : MudComponentBase

Collects and validates user input, monitoring and validating every input derived from MudFormComponent within it.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this form. |
| `IsTouched` | `bool` | `true` | Whether all inputs and child forms passed validation. Defaults to `true`. When this value changes, `IsValidChanged` occurs. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this form. Defaults to `false`. |
| `ReadOnly` | `bool` | `false` | Prevents the user from changing any inputs. Defaults to `false`. |
| `ValidationDelay` | `int` | `300` | The delay, in milliseconds, before performing validation. Defaults to `300` (300 milliseconds). This delay can improve rendering performance for larger forms with inputs which set `Immediate` to `true`. |
| `SuppressRenderingOnValidation` | `bool` | `false` | Prevents child components from rendering when `IsValid` changes. Defaults to `false`. When `true`, rendering performance may improve for larger forms and older devices. |
| `SuppressImplicitSubmission` | `bool` | `true` | Prevents `Enter` from triggering the browser's implicit submission of this form. Defaults to `true`, which adds a hidden disabled submit button so that pressing `Enter` in an input does nothing. This is also what stops a parent dialog from closing when `Enter` is pressed. Setting this to `false` only removes that suppression; it does not add a submit-on-`Enter` feature, and `MudForm` has no submit handler. Whether `Enter` then submits is decided by the browser's implicit submission rules: a form with a single text field submits, but a form with two or more text fields and no enabled submit button does nothing. To run logic when `Enter` is pressed, use `OnEnterPressed`. For standard submit semantics such as an `OnValidSubmit` handler, wrap your inputs in an `EditForm` rather than placing a submit button inside `MudForm`. |
| `Spacing` | `int` | `0` | The amount of spacing between input components, in increments of `4px`. Defaults to `0`. A spacing of `1` means `4px`, `2` means `8px`, and so on. |
| `IsValidChanged` | `EventCallback<bool>` | – | Occurs when `IsValid` has changed. |
| `IsTouchedChanged` | `EventCallback<bool>` | – | Occurs when `IsTouched` has changed. |
| `FieldChanged` | `EventCallback<FormFieldChangedEventArgs>` | – | Occurs when an `IFormComponent` within this form has changed. |
| `OnEnterPressed` | `EventCallback` | – | Occurs when `Enter` is pressed on any child input of this form. |
| `Validation` | `object?` | – | The default function or attribute used to validate form components which cannot validate themselves. Supported values are: 1. A `Func&lt;T,bool&gt;` or `Func&lt;T,Task&lt;bool&gt;&gt;` function. Returns `true` if valid. When `false`, a standard `"Invalid"` message is shown. 2. A `Func&lt;T,string&gt;` or `Func&lt;T,Task&lt;string&gt;&gt;` function. Returns `null` if valid, or a string explaining the error. 3. A `Func&lt;T,IEnumerable&lt;string&gt;&gt;` or `Func&lt;T,Task&lt;IEnumerable&lt;string&gt;&gt;&gt;` function. Returns an empty list if valid, or a list of validation errors. 3. A `Func&lt;object,string,IEnumerable&lt;string&gt;&gt;` or `Func&lt;object,string,Task&lt;IEnumerable&lt;string&gt;&gt;&gt;` function. Given the form model and path to the member, returns an empty list if valid, or a list of validation errors. 4. A `ValidationAttribute` object. |
| `OverrideFieldValidation` | `bool?` | – | Overrides input validation with the function or attribute in `Validation`. |
| `ErrorsChanged` | `EventCallback<string[]>` | – | The validation errors for inputs within this form. When this property changes, `ErrorsChanged` occurs. |
| `Model` | `object?` | – | The model populated by this form. Properties of this model are typically linked to form input components via their `For`. |
