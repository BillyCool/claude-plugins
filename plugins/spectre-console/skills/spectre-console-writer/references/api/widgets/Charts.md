# widgets/Charts — API (generated from source)

## `public sealed class BarChart : Renderable, IHasCulture`

*core* · `src/Spectre.Console/Widgets/Charts/BarChart.cs`

A renderable (horizontal) bar chart.

**Constructors**

- `BarChart()` — Initializes a new instance of the `BarChart` class.

**Properties**

- `List<IBarChartItem> Data { get; }` — Gets the bar chart data.
- `int? Width { get; set; }` — Gets or sets the width of the bar chart.
- `string? Label { get; set; }` — Gets or sets the bar chart label.
- `Justify? LabelAlignment { get; set; }` = `Justify.Center` — Gets or sets the bar chart label alignment.
- `bool ShowValues { get; set; }` = `true` — Gets or sets a value indicating whether or not values should be shown next to each bar.
- `CultureInfo? Culture { get; set; }` — Gets or sets the culture that's used to format values.
- `double? MaxValue { get; set; }` — Gets or sets the fixed max value for a bar chart.
- `Func<double, CultureInfo, string>? ValueFormatter { get; set; }` — Gets or sets the function used to format the values of the bar chart.

**Methods**

- `protected override Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods on this type** (call as `x.Method(...)`)

- `AddItem(string label, double value, Color? color = null) -> BarChart` — Adds an item to the bar chart.
- `AddItem<T>(T item) -> BarChart` — Adds an item to the bar chart.
- `AddItems<T>(IEnumerable<T> items) -> BarChart` — Adds multiple items to the bar chart.
- `AddItems<T>(IEnumerable<T> items, Func<T, BarChartItem> converter) -> BarChart` — Adds multiple items to the bar chart.
- `UseValueFormatter(Func<double, CultureInfo, string>? func) -> BarChart` — Sets the value formatter for the bar chart using culture info.
- `UseValueFormatter(Func<double, string>? func) -> BarChart` — Sets the value formatter for the bar chart.
- `Width(int? width) -> BarChart` — Sets the width of the bar chart.
- `Label(string? label) -> BarChart` — Sets the label of the bar chart.
- `ShowValues() -> BarChart` — Shows values next to each bar in the bar chart.
- `HideValues() -> BarChart` — Hides values next to each bar in the bar chart.
- `ShowValues(bool show) -> BarChart` — Sets whether or not values should be shown next to each bar.
- `LeftAlignLabel() -> BarChart` — Aligns the label to the left.
- `CenterLabel() -> BarChart` — Centers the label.
- `RightAlignLabel() -> BarChart` — Aligns the label to the right.
- `WithMaxValue(double maxValue) -> BarChart` — Sets the max fixed value for the chart.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IHasCulture`: `Culture`
- via `IRenderable`: `GetSegments`

## `public sealed class BarChartItem : IBarChartItem`

*core* · `src/Spectre.Console/Widgets/Charts/BarChartItem.cs`

An item that's shown in a bar chart.

**Constructors**

- `BarChartItem(string label, double value, Color? color = null)` — Initializes a new instance of the `BarChartItem` class.

**Properties**

- `string Label { get; }` — Gets the item label.
- `double Value { get; }` — Gets the item value.
- `Color? Color { get; }` — Gets the item color.

## `public sealed class BreakdownChart : Renderable, IHasCulture, IExpandable`

*core* · `src/Spectre.Console/Widgets/Charts/BreakdownChart.cs`

A renderable breakdown chart.

**Constructors**

- `BreakdownChart()` — Initializes a new instance of the `BreakdownChart` class.

**Properties**

- `List<IBreakdownChartItem> Data { get; }` — Gets the breakdown chart data.
- `int? Width { get; set; }` — Gets or sets the width of the breakdown chart.
- `bool ShowTags { get; set; }` = `true` — Gets or sets a value indicating whether or not to show tags.
- `bool ShowTagValues { get; set; }` = `true` — Gets or sets a value indicating whether or not to show tag values.
- `Func<double, CultureInfo, string>? ValueFormatter { get; set; }` — Gets or sets the tag value formatter.
- `Color ValueColor { get; set; }` = `Color.Grey` — Gets or sets the Color in which the values will be shown.
- `bool Compact { get; set; }` = `true` — Gets or sets a value indicating whether or not the chart and tags should be rendered in compact mode.
- `CultureInfo? Culture { get; set; }` — Gets or sets the `CultureInfo` to use when rendering values.
- `bool Expand { get; set; }` = `true` — Gets or sets a value indicating whether or not the object should expand to the available space. If `false`, the object's width will be auto calculated.

**Methods**

- `protected override Measurement Measure(RenderOptions options, int maxWidth)` — Measures the renderable object.
- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods on this type** (call as `x.Method(...)`)

- `AddItem(string label, double value, Color color) -> BreakdownChart` — Adds an item to the breakdown chart.
- `AddItem<T>(T item) -> BreakdownChart` — Adds an item to the breakdown chart.
- `AddItems<T>(IEnumerable<T> items) -> BreakdownChart` — Adds multiple items to the breakdown chart.
- `AddItems<T>(IEnumerable<T> items, Func<T, IBreakdownChartItem> converter) -> BreakdownChart` — Adds multiple items to the breakdown chart.
- `Width(int? width) -> BreakdownChart` — Sets the width of the breakdown chart.
- `UseValueFormatter(Func<double, CultureInfo, string>? func) -> BreakdownChart` — Tags will be shown.
- `UseValueFormatter(Func<double, string>? func) -> BreakdownChart` — Tags will be shown.
- `ShowPercentage() -> BreakdownChart` — Tags will be shown.
- `ShowTags() -> BreakdownChart` — Tags will be shown.
- `HideTags() -> BreakdownChart` — Tags will be not be shown.
- `ShowTags(bool show) -> BreakdownChart` — Sets whether or not tags will be shown.
- `ShowTagValues() -> BreakdownChart` — Tag values will be shown.
- `HideTagValues() -> BreakdownChart` — Tag values will be not be shown.
- `ShowTagValues(bool show) -> BreakdownChart` — Sets whether or not tag values will be shown.
- `Compact() -> BreakdownChart` — Chart and tags is rendered in compact mode.
- `FullSize() -> BreakdownChart` — Chart and tags is rendered in full size mode.
- `Compact(bool compact) -> BreakdownChart` — Sets whether or not the chart and tags should be rendered in compact mode.
- `WithValueColor(Color color) -> BreakdownChart` — Sets the `BreakdownChart.ValueColor`.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IExpandable`: `Collapse`, `Expand`
- via `IHasCulture`: `Culture`
- via `IRenderable`: `GetSegments`

## `public sealed class BreakdownChartItem : IBreakdownChartItem`

*core* · `src/Spectre.Console/Widgets/Charts/BreakdownChartItem.cs`

An item that's shown in a breakdown chart.

**Constructors**

- `BreakdownChartItem(string label, double value, Color color)` — Initializes a new instance of the `BreakdownChartItem` class.

**Properties**

- `string Label { get; }` — Gets the item label.
- `double Value { get; }` — Gets the item value.
- `Color Color { get; }` — Gets the item color.

## `public interface IBarChartItem`

*core* · `src/Spectre.Console/Widgets/Charts/IBarChartItem.cs`

Represents a bar chart item.

**Properties**

- `string Label { get; }` — Gets the item label.
- `double Value { get; }` — Gets the item value.
- `Color? Color { get; }` — Gets the item color.

## `public interface IBreakdownChartItem`

*core* · `src/Spectre.Console/Widgets/Charts/IBreakdownChartItem.cs`

Represents a breakdown chart item.

**Properties**

- `string Label { get; }` — Gets the item label.
- `double Value { get; }` — Gets the item value.
- `Color Color { get; }` — Gets the item color.

