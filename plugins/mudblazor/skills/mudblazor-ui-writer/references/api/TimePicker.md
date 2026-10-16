# TimePicker components — API (generated from source)

## MudTimePicker : MudPicker<TimeSpan?>

Selects a time of day from a clock shown in a drop-down, dialog, or inline.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `OpenTo` | `OpenTo` | `OpenTo.Hours` | The initial view for this picker. Defaults to `Hours`. |
| `TimeEditMode` | `TimeEditMode` | `TimeEditMode.Normal` | Controls which values can be edited. Defaults to `Normal`. |
| `ClosingDelay` | `int` | `200` | The amount of time, in milliseconds, to wait before closing the picker. Defaults to `200`. The delay gives users a moment to see the selected time before the popover disappears. |
| `AutoClose` | `bool` | `false` | Closes this picker when the value is set or cleared. Defaults to `false`. When `true` and `PickerActions` are defined, the hour and the minutes can be selected and the drop-down will close without having to click any of the action buttons. |
| `MinuteSelectionStep` | `int` | `1` | The step interval when selecting minutes. Defaults to `1`. For example: a value of `15` would allow minutes `0`, `15`, `30`, and `45` be selected. |
| `AmPm` | `bool` | `false` | Shows a 12-hour selection clock. Defaults to `false`. When `true`, hours 1-12 are displayed with an AM or PM marker. When `false`, hours 0-23 are displayed. |
| `TimeFormat` | `string` | `string.Empty` | The format applied to time values. Defaults to `hh:mm tt` when `AmPm` is `true`, otherwise `HH:mm`. Format strings are typically a combination of these characters: * `h` (lowercase) for hours in 12-hour time, * `H` (uppercase) for hours in 24-hour time, * `m` for minutes, * `tt` for AM/PM markers. For example: `h:mm tt` would display `6:32 PM`, and `HH:mm` would display `18:32`. |
| `TimeChanged` | `EventCallback<TimeSpan?>` | – | The currently selected time. When this value changes, `TimeChanged` occurs. |
