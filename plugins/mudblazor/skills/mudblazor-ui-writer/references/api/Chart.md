# Chart components — API (generated from source)

## BaseAxisChart<T, TChartOptions> : MudComponentBase

Renders the SVG axes, grid lines, series paths, and tooltips shared by axis-based chart types.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `YAxisLabelSize` | `ElementSize?` | – | The size of the Y-axis labels. |
| `YAxisLabelSizeChanged` | `EventCallback<ElementSize?>` | – | The event callback for when the Y-axis label size changes. |
| `XAxisLabelSize` | `ElementSize?` | – | The size of the X-axis labels. |
| `XAxisLabelSizeChanged` | `EventCallback<ElementSize?>` | – | The event callback for when the X-axis label size changes. |
| `Width` | `string` | – | The width of the chart. |
| `Height` | `string` | – | The height of the chart. |
| `ChartType` | `ChartType?` | – | The type of the chart. |
| `ChartClass` | `string` | `string.Empty` | The CSS class of the chart. |
| `ChartSeries` | `List<ChartSeries<T>>` | `[]` | The series of data for the chart. |
| `ChartOptions` | `TChartOptions` | – | The options for the chart. |
| `ChartLabels` | `string[]` | `[]` | The labels for the chart. |
| `ViewBoxWidth` | `double` | – | The width of the view box. |
| `ViewBoxHeight` | `double` | – | The height of the view box. |
| `MatchBoundsToSize` | `bool` | – | Make the chart fill the parent |
| `ChildContent` | `RenderFragment?` | – | The child content of the component. |
| `SeriesContent` | `RenderFragment?` | – | The content for the series. |
| `TooltipContent` | `RenderFragment?` | – | The content for the tooltip. |
| `CustomGraphics` | `RenderFragment?` | – | The custom graphics for the chart. |
| `HoveredSegment` | `SvgPath?` | – | The currently hovered segment. |
| `HorizontalLines` | `IList<SvgPath>` | `[]` | The horizontal lines of the grid. |
| `VerticalLines` | `IList<SvgPath>` | `[]` | The vertical lines of the grid. |
| `HorizontalValues` | `IList<SvgText>` | `[]` | The horizontal values of the grid. |
| `VerticalValues` | `IList<SvgText>` | `[]` | The vertical values of the grid. |
| `XAxisTitle` | `string?` | – | The title of the X-axis. |
| `YAxisTitle` | `string?` | – | The title of the Y-axis. |
| `AxisChanged` | `EventCallback` | – | The event callback for when the axis changes. |
| `ElementRefChanged` | `EventCallback<ElementReference>` | – | The event callback for when the element reference changes. |

## BaseRadialChart<T, TChartOptions> : MudComponentBase

Renders the SVG segments, labels, and tooltips shared by radial chart types such as pie, donut, radar, and rose.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Width` | `string` | `string.Empty` | The width of the chart. |
| `Height` | `string` | `string.Empty` | The height of the chart. |
| `Radius` | `double` | – | The radius of the chart. |
| `Paths` | `List<SvgPath>` | `[]` | The SVG paths for the chart segments. |
| `ChartOptions` | `TChartOptions` | `new()` | The options for the chart. |
| `ChartClass` | `string` | `string.Empty` | The CSS class of the chart. |
| `ChartSeries` | `List<ChartSeries<T>>` | `[]` | The series of data for the chart. |
| `ChartLabels` | `string[]` | `[]` | The labels for the chart. |
| `HoveredSegment` | `SvgPath?` | – | The currently hovered segment. |
| `OnMouseOut` | `EventCallback` | – | The event callback for when the mouse leaves a segment. |
| `OnPathClick` | `EventCallback<int>` | – | The event callback for when a path is clicked. |
| `OnMouseOver` | `EventCallback<(MouseEventArgs Args, SvgPath Segment)>` | – | The event callback for when the mouse enters a segment. |
| `ElementRefChanged` | `EventCallback<ElementReference>` | – | The event callback for when the element reference changes. |
| `CustomGraphics` | `RenderFragment?` | – | The custom graphics for the chart. |
| `ChartGrid` | `RenderFragment?` | – | The grid area for the chart. |
| `ChartAxisLabels` | `RenderFragment?` | – | The labels overlaying the grid area. |
| `ChartDataPoints` | `RenderFragment<SvgPolygon>?` | – | The data points for the chart. |
| `TooltipTemplate` | `RenderFragment<(SvgPath Segment, string Color)>?` | – | The template for the tooltip. |
| `TooltipPositionFunc` | `Func<SvgPath, (double X, double Y)>?` | – | The function to determine the position of the tooltip. |

## MudAxisChartBase<T, TOptions> : MudChartBase<T, TOptions>

Serves as the base class for axis-based charts, providing core functionality for rendering and managing chart elements such as axes, grids, and legends.

*Provides foundational features for axis-based charts, including support for shared data regions, overlay charts, and dynamic resizing.*

_No own parameters — see base class `MudChartBase<T, TOptions>`._

## MudAxisLineChartBase<T, TOptions> : MudAxisChartBase<T, TOptions>

Base class for line-based charts such as `Line{T}`, `ScatterPlot{T}`, and `TimeSeries{T}`. Generates the SVG line paths, area fills, and data-point markers, with optional interpolation.

_No own parameters — see base class `MudAxisChartBase<T, TOptions>`._

## MudChartBase<T, TOptions> : MudComponentBase

Base class for MudBlazor chart components, providing the data series, options, legend, and selection shared by every chart type.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChartLabels` | `string[]` | `[]` | The labels describing data values. The number of labels in this array is typically the same as the number of values in the `Data` property. |
| `ChartSeries` | `List<ChartSeries<T>>` | `[]` | The series of values to display. |
| `ChartOptions` | `TOptions?` | – | The display options applied to the chart. |
| `CustomGraphics` | `RenderFragment?` | – | The custom graphics within this chart. |
| `TooltipTemplate` | `RenderFragment<(SvgPath Segment, string Color)>?` | – | Optional template for custom tooltip rendering. If provided, this will be used instead of the default ChartTooltip. |
| `TooltipPositionFunc` | `Func<SvgPath, (double X, double Y)>?` | – | Optional callback function to determine the position of the tooltip. If not provided, the default tooltip positioning logic will be used. |
| `ChildContent` | `RenderFragment?` | – | ChildContent for this component |
| `ChartType` | `ChartType` | – | The type of chart to display. |
| `Width` | `string` | `"80%"` | The width of the chart, as a CSS style. Defaults to `80%`. Values can be a percentage or pixel width such as `200px`. |
| `Height` | `string` | `"80%"` | The height of the chart, as a CSS style. Defaults to `80%`. Values can be a percentage or pixel width such as `200px`. |
| `MatchBoundsToSize` | `bool` | – | Make the chart fill the parent |
| `LegendPosition` | `Position` | `Position.Bottom` | The location of series labels. Defaults to `Bottom`. |
| `SelectedIndex` | `int` | – | The currently selected data point. When this property changes, the `SelectedIndexChanged` event occurs. |
| `SelectedIndexChanged` | `EventCallback<int>` | – | Occurs when the `SelectedIndex` has changed. |
| `CanHideSeries` | `bool` | – | Allows series to be hidden When `true`, checkboxes are displayed which can toggle visibility of each data set |

## MudRadialChartBase<T, TOptions> : MudChartBase<T, TOptions>

Base class for radial charts such as `Pie{T}`, `Donut{T}`, `Radar{T}`, and `Rose{T}`. Aggregates and normalizes series data into circular segments and legends.

_No own parameters — see base class `MudChartBase<T, TOptions>`._

## HeatMap<T> : MudChartBase<T, HeatMapChartOptions>

_No own parameters — see base class `MudChartBase<T, HeatMapChartOptions>`._

## Sankey<T> : MudChartBase<T, SankeyChartOptions>

Represents a chart which displays data as nodes connected by weighted edges.

_No own parameters — see base class `MudChartBase<T, SankeyChartOptions>`._

## MudHeatMapCell<T> : MudComponentBase

Overrides a single cell in a `HeatMap{T}` chart, replacing the value from the `ChartSeries{T}` or rendering custom SVG content inside the cell.

*Provide a width and height for custom content so the heat map can resize it dynamically.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Row` | `int` | – | The row of the cell you want to modify. Rows use a 0 based index. |
| `Column` | `int` | – | The column of the cell you want to modify. Columns use a 0 based index. |
| `Value` | `T?` | – | If supplied this will overwrite the value in ChartSeries |
| `MudColor` | `MudColor?` | – | Optional, Override the color of the cell |
| `Width` | `int?` | – | Optional, The width of the custom svg element you want to include. Please note the custom svg elements you provide are resized according to this value if supplied. |
| `Height` | `int?` | – | Optional, The height of the custom svg element you want to include. Please note the custom svg elements you provide are resized according to this value if supplied. |
| `MinValue` | `T?` | – | Optional, setting this will set the minimum value for the heatmap range, by default the range is calculated from the data. This only needs to be set on one `MudHeatMapCell{T}` in the `HeatMap{T}`."/> Only the last value set will be used. |
| `MaxValue` | `T?` | – | Optional, setting this will set the maximum value for the heatmap range, by default the range is calculated from the data. This only needs to be set on one `MudHeatMapCell{T}` in the `HeatMap{T}`."/> Only the last value set will be used. |
| `ChildContent` | `RenderFragment?` | – | Optional, The custom svg element you want to include |

## MudChart<T>

Charts plot numeric data as line, bar, stacked bar, pie, donut, radar, rose, heat map, time series, scatter, or Sankey graphics. Choose the graphic with the `ChartType` parameter.

_No own parameters._

## ChartTooltip : ComponentBase

Renders the floating tooltip shown when hovering data points in MudBlazor's charts.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Title` | `string` | `string.Empty` | The title of the tooltip. |
| `Subtitle` | `string` | `string.Empty` | The subtitle of the tooltip. When empty, the subtitle is not displayed. |
| `X` | `double` | – | The X coordinate of the tooltip anchor. |
| `Y` | `double` | – | The Y coordinate of the tooltip anchor. |
| `Color` | `string` | `"darkgrey"` | The color of the tooltip. Defaults to `"darkgrey"`. |
| `FontSize` | `string` | `"12px"` | The font size of the `Title` and `Subtitle`. Defaults to `"12px"`. |
| `PaddingSize` | `int` | `5` | The padding size of the tooltip background in px. Defaults to `5`. |
| `FontColor` | `string` | `"white"` | The color of the `Title` and `Subtitle`. Defaults to `"unset"`. |
| `StrokeWidth` | `int` | `1` | The width of the border. Defaults to `1`. |
| `ShowTriangle` | `bool` | `true` | Whether to show the triangle pointing down. Defaults to `true`. |
| `AnchorPositionX` | `ChartTooltipAnchorPositionX` | `ChartTooltipAnchorPositionX.Center` | How to align the tooltip in respect to the given x coordinates. Defaults to `ChartTooltipRelativePositionX.Center`. |

## Legend<T> : MudChartBase<T, IChartOptions>

Legend that lists text labels identifying each data series shown in a `MudChart{T}`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Data` | `List<SvgLegend>` | `[]` | The data labels for this legend. |
| `ShowLegend` | `bool?` | – | Whether the chart legend should be displayed. |
| `ChartPalette` | `string[]?` | – | The palette of colors to use for the chart series. |
| `OnLegendSelected` | `EventCallback<int>` | – | Raised when a legend item is clicked. |
