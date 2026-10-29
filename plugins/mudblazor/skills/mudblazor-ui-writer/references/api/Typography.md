# Typography components — API (generated from source)

## MudText : MudComponentBase

A customizable piece of text.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Typo` | `Typo` | `Typo.body1` | The theme style of the text. Defaults to `body1`. Uses the theme HTML tag unless `HtmlTag` is set. |
| `Align` | `Align` | `Align.Inherit` | The horizontal alignment of this text. Defaults to `Inherit`. Controls which `text-align` will be used. Has no effect on inline displays. |
| `Color` | `Color` | `Color.Inherit` | The color of this text. Defaults to `Inherit`. |
| `GutterBottom` | `bool` | `false` | Adds a bottom margin. Defaults to `false`. Has no effect on inline displays. |
| `Inline` | `bool` | `false` | Whether this text continues on the same line. Defaults to `false`. When `false`, text will start on a new line. |
| `ChildContent` | `RenderFragment?` | – | The child content to display. |
| `HtmlTag` | `string?` | `null`, meaning the tag is automatically decided based on `Typo` | The HTML element used for this text. that will be rendered (Example: `span`, `p`, `h1`). Defaults to `null`, meaning the tag is automatically decided based on `Typo`. A custom tag such as `span`, `p`, `h1` can be used to specify the type of content for accessibility and SEO more accurately. The tag affects the display type and the applicability of properties like `Align` and `GutterBottom`. |
| `Truncate` | `bool` | – | Truncates the text with an ellipsis if it overflows its container. |
