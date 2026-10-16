# Grid components — API (generated from source)

## MudFlexBreak : MudComponentBase

Forces a line break in a flexbox layout so the items that follow wrap onto a new line.

_No own parameters — see base class `MudComponentBase`._

## MudGrid : MudComponentBase

A 12-point grid system for organizing content with responsive breakpoints for different screen sizes.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Spacing` | `int` | `6` | The gap between items, measured in increments of `4px`. Defaults to 6. Maximum is 20. The increment was halved in v7, so the default is now 6 instead of 3. |
| `Justify` | `Justify` | `Justify.FlexStart` | Defines the distribution of children along the main axis within a `MudStack` component. |
| `ChildContent` | `RenderFragment?` | – | Child content of the component. |

## MudItem : MudComponentBase

A portion of a `MudGrid`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `xs` | `int` | – | Sets the number of columns to occupy at the 'extra small' breakpoint. |
| `sm` | `int` | – | Sets the number of columns to occupy at the 'small' breakpoint. |
| `md` | `int` | – | Sets the number of columns to occupy at the 'medium' breakpoint. |
| `lg` | `int` | – | Sets the number of columns to occupy at the 'large' breakpoint. |
| `xl` | `int` | – | Sets the number of columns to occupy at the 'extra large' breakpoint. |
| `xxl` | `int` | – | Sets the number of columns to occupy at the 'extra extra large' breakpoint. |
| `ChildContent` | `RenderFragment?` | – | Child content of the component. |
