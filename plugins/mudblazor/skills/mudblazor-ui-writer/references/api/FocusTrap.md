# FocusTrap components — API (generated from source)

## MudFocusTrap : IDisposable

Prevents the keyboard focus from cycling out of its child content. Typically used within dropdown selectors and modal dialogs.

*Typically used within dialogs and other overlays.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this focus trap. |
| `DefaultFocus` | `DefaultFocus` | `DefaultFocus.FirstChild` | Prevents the user from interacting with this focus trap. Defaults to `false`. |
