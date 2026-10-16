# Hotkey components — API (generated from source)

## MudHotkey : MudComponentBase

Allows registering a hotkey.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The optional content to be displayed when the hotkey is pressed. |
| `Key` | `JsKey` | – | The hotkey to register. If you would like to use a modifier key here, you also have to add it to `KeyModifiers`. |
| `KeyModifiers` | `IEnumerable<JsKeyModifier>` | `[]` | The modifiers the user has to press together with `Key` to trigger the hotkey. If left empty the hotkey will be triggered by pressing `Key` alone. |
| `OnHotkeyPressed` | `EventCallback<HotkeyEventArgs>` | – | Occurs when `Key` and `KeyModifiers` are pressed. |
| `HideChildContentOnRepress` | `bool` | `false` | Whether to hide the child content when the hotkey is pressed again, allowing for a toggle behavior. Defaults to `false`. |
| `PreventEventPropagation` | `bool` | `true` | Whether to prevent the key press event from propagating. Defaults to `true`. |
| `Disabled` | `bool` | `false` | Ignores the hotkey when set to true. Defaults to `false`. |
