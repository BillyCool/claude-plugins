# ExitPrompt components — API (generated from source)

## MudExitPrompt : MudComponentBase

Shows a confirmation dialog when the user tries to navigate away.

*Due to browser restrictions the native browser exit prompt has to be used on browser navigation.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Title` | `string?` | `the localized version of "Confirm navigation"` | The title shown in the confirmation dialog. Defaults to the localized version of "Confirm navigation" . |
| `Text` | `string?` | `the localized version of "Leave site? Changes you made may not be saved` | The message shown in the confirmation dialog. Defaults to the localized version of "Leave site? Changes you made may not be saved." . |
| `Disabled` | `bool` | `false` | Disables exit prompt protection. When set to `true`, navigation proceeds without confirmation and JS unload protection is removed. Defaults to `false`. |
| `UseNativePrompt` | `bool` | `false` | Uses the browser's native confirmation prompt for in-app navigation. When `false`, navigation inside the app uses a MudBlazor message box with `Title` and `Text`. When `true`, in-app navigation uses the browser `confirm` dialog and `Title` is ignored. Tab close, refresh, and direct URL navigation always use the browser's native unload prompt. Defaults to `false`. |
