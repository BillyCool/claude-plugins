# DatePicker components — API (generated from source)

## MudBaseDatePicker : MudPicker<DateTime?>

Base class for MudBlazor date pickers such as `MudDatePicker` and `MudDateRangePicker`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `MaxDate` | `DateTime?` | – | The maximum selectable date. |
| `MinDate` | `DateTime?` | – | The minimum selectable date. |
| `OpenTo` | `OpenTo` | `OpenTo.Date` | The initial view to display. Defaults to `Date`. |
| `DateFormat` | `string?` | – | The format for selected dates. |
| `FirstDayOfWeek` | `DayOfWeek?` | `the current culture's `DateTimeFormat` | The day representing the first day of the week. Defaults to the current culture's `DateTimeFormat.FirstDayOfWeek`. |
| `PickerMonthChanged` | `EventCallback<DateTime?>` | – | Occurs when `PickerMonth` has changed. |
| `ClosingDelay` | `int` | `100` | The delay, in milliseconds, before closing the picker after a value is selected. Defaults to `100`. This delay helps the user see that a date has been selected before the popover disappears. |
| `DisplayMonths` | `int` | `1` | The number of months to display in the calendar. Defaults to `1`. |
| `MaxMonthColumns` | `int?` | `null` | The maximum number of months allowed in one row. Defaults to `null`. When `null`, the `DisplayMonths` is used. |
| `StartMonth` | `DateTime?` | – | The start month when opening the picker. |
| `ShowWeekNumbers` | `bool` | `false` | Shows week numbers at the start of each week. Defaults to `false`. |
| `ShowAdjacentMonthDays` | `bool` | `false` | Shows the days from the previous and next month when they appear in the current calendar grid. Defaults to `false`. |
| `TitleDateFormat` | `string` | `"ddd, dd MMM"` | The format of the selected date in the title. Defaults to `ddd, dd MMM`. Supported date formats can be found here: <see href="https://learn.microsoft.com/dotnet/standard/base-types/standard-date-and-time-format-strings"/>. |
| `AutoClose` | `bool` | `false` | Closes this picker when a value is selected. Defaults to `false`. |
| `IsDateDisabledFunc` | `Func<DateTime, bool>` | `_ => false` | The function used to disable one or more dates. Defaults to `null`. When set, a date will be disabled if the function returns `true`. |
| `AdditionalDateClassesFunc` | `Func<DateTime, string>?` | – | The function which returns CSS classes for a date. Multiple classes must be separated by spaces. |
| `PreviousIcon` | `string` | `Icons.Material.Filled.ChevronLeft` | The icon for the button that navigates to the previous month or year. Defaults to `ChevronLeft`. |
| `NextIcon` | `string` | `Icons.Material.Filled.ChevronRight` | The icon for the button which navigates to the next month or year. Defaults to `ChevronRight`. |
| `FixYear` | `int?` | `null` | The year to use, which cannot be changed. Defaults to `null`. |
| `FixMonth` | `int?` | `null` | The month to use, which cannot be changed. Defaults to `null`. |
| `FixDay` | `int?` | `null` | The day to use, which cannot be changed. Defaults to `null`. |

## MudDatePicker : MudBaseDatePicker

Selects a single date from a calendar shown in a drop-down, dialog, or inline.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `DateChanged` | `EventCallback<DateTime?>` | – | Occurs when the `Date` has changed. |

## MudDateRangePicker : MudBaseDatePicker

Selects a start and end date range from a calendar shown in a drop-down, dialog, or inline.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `MaxDays` | `int?` | – | The maximum number of selectable days. Inclusive of the selected date. |
| `MinDays` | `int?` | – | The minimum number of selectable days. Inclusive of the selected date. |
| `AllowDisabledDatesInCount` | `bool` | `true` | Include disabled dates within the valid min/max days range. Defaults to `true`. Disabled days will be included in the min/max count. This parameter will take effect when `MinDays` or `MaxDays` is set. |
| `PlaceholderStart` | `string?` | – | The text displayed in the start input if no date is specified. This property is typically used to give the user a hint as to what kind of input is expected. |
| `PlaceholderEnd` | `string?` | – | The text displayed in the end input if no date is specified. This property is typically used to give the user a hint as to what kind of input is expected. |
| `SeparatorIcon` | `string` | `Icons.Material.Filled.ArrowRightAlt` | The icon displayed between start and end dates. Defaults to `ArrowRightAlt`. |
| `DateRangeChanged` | `EventCallback<DateRange?>` | – | Occurs when `DateRange` has changed. |
| `AllowDisabledDatesInRange` | `bool` | `false` | The currently selected date range. By default, it will always ignore disabled dates. This parameter will take effect when `IsDateDisabledFunc` is set. |
