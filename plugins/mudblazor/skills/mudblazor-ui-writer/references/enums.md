# MudBlazor enums (generated from source)

Every public enum with its values. "CSS name" is the string emitted
into CSS classes (the `[Description]` attribute value).

## Adornment

Specifies where an adornment such as an icon, text, or button appears within a form field.

| Value | CSS name | Meaning |
|---|---|---|
| `None` | `none` | No adornment is displayed. |
| `Start` | `start` | The adornment is placed at the start of the field. |
| `End` | `end` | The adornment is placed at the end of the field. |

## AggregateType

Indicates the type of aggregation to perform.

| Value | CSS name | Meaning |
|---|---|---|
| `Avg` | – | Calculates the average of values. |
| `Count` | – | Calculates the number of values. |
| `Custom` | – | Calculates the aggregate using a custom function. |
| `Max` | – | Calculates the maximum value. |
| `Min` | – | Calculates the minimum value. |
| `Sum` | – | Calculates the sum of values. |

## AggregationOption

Specifies how chart data is aggregated before plotting, either not at all, grouped by data set, or grouped by label.

| Value | CSS name | Meaning |
|---|---|---|
| `None` | – | No aggregation is applied; |
| `GroupByDataSet` | – | Aggregate data based on the dataset |
| `GroupByLabel` | – | Aggregate data based on labels |

## Align

The horizontal alignment of text or inline content.

| Value | CSS name | Meaning |
|---|---|---|
| `Inherit` | `inherit` |  |
| `Left` | `left` |  |
| `Center` | `center` |  |
| `Right` | `right` |  |
| `Justify` | `justify` |  |
| `Start` | `start` |  |
| `End` | `end` |  |

## AlignItems

The vertical alignment applied to items in a `MudStack` or `MudDataGrid{T}`.

| Value | CSS name | Meaning |
|---|---|---|
| `Baseline` | `baseline` | Items are aligned to keep text consistently aligned. |
| `Center` | `center` | The center of items is aligned to the center of the container. |
| `Start` | `start` | The top edge of items are aligned to the top of the container. |
| `End` | `end` | The bottom edge of items are aligned to the bottom of the container. |
| `Stretch` | `stretch` | Items will have the same height as the container. |

## Anchor

Indicates the edge of a container that a component will appear.

| Value | CSS name | Meaning |
|---|---|---|
| `Left` | `left` | The component will display on the left edge. |
| `Right` | `right` | The component will display on the right edge. |
| `Start` | `start` | The component will display based on Right-to-Left (RTL) language settings. |
| `End` | `end` | The component will display based on Right-to-Left (RTL) language settings. |
| `Top` | `top` | The component will display on the top of the container. |
| `Bottom` | `bottom` | The component will display on the bottom of the container. |

## Animation

Indicates the type of animation used for a `MudSkeleton` component.

| Value | CSS name | Meaning |
|---|---|---|
| `False` | `false` | No animation occurs. |
| `Pulse` | `pulse` | The animation fades in and out in a pulsing loop. |
| `Wave` | `wave` | A left-to-right wave effect occurs. |

## Breakpoint

Indicates a browser width used to trigger behaviors.

| Value | CSS name | Meaning |
|---|---|---|
| `Xs` | `xs` | A small to large phone. |
| `Sm` | `sm` | A small to medium tablet. |
| `Md` | `md` | A large tablet or laptop. |
| `Lg` | `lg` | A desktop computer. |
| `Xl` | `xl` | A high-definition or 4K desktop computer monitor. |
| `Xxl` | `xxl` | An ultra-wide of 4K+ desktop computer monitor. |
| `SmAndDown` | `smanddown` | A small to medium tablet, or smaller device. |
| `MdAndDown` | `mdanddown` | A large tablet, laptop, tablet, or smaller device. |
| `LgAndDown` | `lganddown` | A desktop computer or smaller device. |
| `XlAndDown` | `xlanddown` | A high-definition or 4K desktop computer monitor, or smaller device. |
| `SmAndUp` | `smandup` | A small to medium-sized tablet, or larger device. |
| `MdAndUp` | `mdandup` | A large tablet, laptop, or larger device. |
| `LgAndUp` | `lgandup` | A desktop computer, or larger device. |
| `XlAndUp` | `xlandup` | A high-definition or 4K desktop computer monitor, or larger device. |
| `None` | `none` | No breakpoint applies. |
| `Always` | `always` | Content will always be visible. |

## ButtonType

Indicates the behavior performed when a button is clicked.

| Value | CSS name | Meaning |
|---|---|---|
| `Button` | `button` | A regular click occurs. |
| `Submit` | `submit` | The button will submit a form. |
| `Reset` | `reset` | The button resets a form. |

## ChartTooltipAnchorPositionX

The horizontal anchor position of a chart tooltip relative to its data point.

| Value | CSS name | Meaning |
|---|---|---|
| `Start` | – |  |
| `Center` | – |  |
| `End` | – |  |

## ChartType

Indicates the type of chart to display.

| Value | CSS name | Meaning |
|---|---|---|
| `Donut` | – | Data is displayed as a hollow circle. |
| `Line` | – | Data is displayed as connecting lines. |
| `Pie` | – | Data is displayed as a portion of a circle. |
| `Bar` | – | Data is displayed as rectangles. |
| `StackedBar` | – | Data is displayed as connected rectangles. |
| `Timeseries` | – | Data is displayed as connecting lines or as areas. |
| `HeatMap` | – | Data is displayed as a heatmap. Similar to how github works. |
| `Rose` | – | Data is displayed as sectors of varying radii on a circular chart. |
| `Radar` | – | Data is displayed on multiple axes originating from a central point. |
| `Sankey` | – | Data is displayed as nodes connected by edges. |
| `ScatterPlot` | – | Data is displayed as individual points plotted by X and Y coordinates. |

## Color

The color themes available in MudBlazor, allowing components to adapt their visual style based on the selected color.

| Value | CSS name | Meaning |
|---|---|---|
| `Default` | `default` | The default color theme. |
| `Primary` | `primary` | The primary color theme, usually the main color used in the application. |
| `Secondary` | `secondary` | The secondary color theme, often used for accents and highlights. |
| `Tertiary` | `tertiary` | The tertiary color theme, typically used for additional accents or highlights. |
| `Info` | `info` | The info color theme, used to indicate informational messages. |
| `Success` | `success` | The success color theme, used to indicate successful operations. |
| `Warning` | `warning` | The warning color theme, used to indicate potential issues or warnings. |
| `Error` | `error` | The error color theme, used to indicate errors or critical issues. |
| `Dark` | `dark` | The dark color theme, usually used for dark mode or dark-themed elements. |
| `Transparent` | `transparent` | The transparent theme, making elements see-through. |
| `Inherit` | `inherit` | Inherits the color from the parent element. |
| `Surface` | `surface` | The surface color theme, typically used for the background or surface elements. |

## ColorPickerMode

Indicates the initial mode used by a `MudColorPicker`.

| Value | CSS name | Meaning |
|---|---|---|
| `RGB` | – | Red, Green, and Blue color values are used. |
| `HSL` | – | Hue, Saturation, and Lightness color values are used. |
| `HEX` | – | Hexadecimal values are used. |

## ColorPickerView

Indicates the color selection view for a `MudColorPicker`.

| Value | CSS name | Meaning |
|---|---|---|
| `Spectrum` | – | Colors are chosen from a gradient of colors. |
| `Palette` | – | Colors are chosen from a pre-defined palette. |
| `Grid` | – | Colors are chosen from a grid of possible values. |
| `GridCompact` | – | Colors are chosen from a smaller grid of possible values. |

## ContentNavigationExpandBehaviour

Controls when a page content navigation expands the links nested under a section.

| Value | CSS name | Meaning |
|---|---|---|
| `Always` | – |  |
| `WhenSectionIsActive` | – |  |

## DataGridDragAndDropColumnReorderMode

Indicates how columns are reordered when dragging column headers in a `MudDataGrid{T}`.

| Value | CSS name | Meaning |
|---|---|---|
| `Swap` | – | Swaps the locations of the dragged column with the target column. |
| `Insert` | – | Inserts the dragged column at the target column's position, shifting all subsequent columns one position. |

## DataGridEditFormAction

Defines how the data grid edit form behaves after an edit operation.

| Value | CSS name | Meaning |
|---|---|---|
| `Close` | – | Close the edit form after `CommittedItemChanges` has completed. |
| `KeepOpen` | – | Keep the edit form open after `CommittedItemChanges` has completed. |

## DataGridEditMode

Indicates how values are edited for `MudDataGrid{T}` cells.

| Value | CSS name | Meaning |
|---|---|---|
| `Cell` | – | Values are edited in the cell. |
| `Form` | – | A dialog is shown to edit values. |
| `Inline` | – | A single row is edited inline when triggered manually. Only the row being edited shows input controls; all other rows display plain text. |

## DataGridEditTrigger

Indicates the behavior which begins editing a cell.

| Value | CSS name | Meaning |
|---|---|---|
| `OnRowClick` | – | Editing begins when the row is clicked. |
| `Manual` | – | Editing begins when the edit button is clicked. |

## DataGridFilterCaseSensitivity

Indicates how string values are compared for a `MudDataGrid{T}` filter.

| Value | CSS name | Meaning |
|---|---|---|
| `Default` | – | Text is compared using `Ordinal`. |
| `CaseInsensitive` | – | Text is compared using `OrdinalIgnoreCase`. |
| `Ignore` | – | Excludes any `StringComparison` value for text comparisons. |

## DataGridFilterMode

Indicates the filtering behavior for `MudDataGrid{T}` rows.

| Value | CSS name | Meaning |
|---|---|---|
| `Simple` | – | All filters are managed in a single popover. |
| `ColumnFilterMenu` | – | Only the current column filter is managed in a popover. |
| `ColumnFilterRow` | – | Filters are shown as a row in the grid. |

## DefaultFocus

Indicates the element which will receive focus.

| Value | CSS name | Meaning |
|---|---|---|
| `None` | – | No focus will occur. |
| `Element` | – | This component will receive focus. |
| `FirstChild` | – | The first child within this component will receive focus. |
| `LastChild` | – | The last child within this component will receive focus. |

## DialogPosition

The location of a `MudDialog` when it is opened.

| Value | CSS name | Meaning |
|---|---|---|
| `Center` | `center` | The dialog will appear in the center of the screen. |
| `CenterLeft` | `centerleft` | The dialog will appear on the left side of the screen, centered vertically. |
| `CenterRight` | `centerright` | The dialog will appear on the left side of the screen, centered vertically. |
| `TopCenter` | `topcenter` | The dialog will appear on the top of the screen, centered horizontally. |
| `TopLeft` | `topleft` | The dialog will appear on the upper-left corner of the screen. |
| `TopRight` | `topright` | The dialog will appear on the upper-right corner of the screen. |
| `BottomCenter` | `bottomcenter` | The dialog will appear on the bottom of the screen, centered horizontally. |
| `BottomLeft` | `bottomleft` | The dialog will appear on the lower-left corner of the screen. |
| `BottomRight` | `bottomright` | The dialog will appear on the lower-right corner of the screen. |
| `Custom` | `custom` | The dialog will appear at a custom position. |

## Direction

A direction used to orient or position an element.

| Value | CSS name | Meaning |
|---|---|---|
| `Bottom` | `bottom` |  |
| `Top` | `top` |  |
| `Left` | `left` |  |
| `Right` | `right` |  |
| `Start` | `start` |  |
| `End` | `end` |  |

## DispatcherRegistrationPolicy

Determines how dispatcher builders handle registrations for the same specific input type.

| Value | CSS name | Meaning |
|---|---|---|
| `LastWins` | – | The newest registration replaces the previous one. |
| `FirstWins` | – | The first registration is kept and later duplicates are ignored. |
| `Throw` | – | Duplicate registrations throw an exception. |

## DividerType

The type of `MudDivider` to display.

| Value | CSS name | Meaning |
|---|---|---|
| `FullWidth` | `fullwidth` | The divider will fill the width of its container. |
| `Inset` | `inset` | The divider has a margin on its left side. |
| `Middle` | `middle` | The divider has a margin on the left and right sides. |

## DrawerClipMode

Indicates the clipping behavior of a `MudDrawer` when inside of a `MudLayout`.

| Value | CSS name | Meaning |
|---|---|---|
| `Never` | `never` | The drawer will display over the `MudAppBar` and other content. |
| `Docked` | `docked` | The drawer will display underneath the `MudAppBar` and push content to the side when opening. |
| `Always` | `always` | The drawer will display underneath the `MudAppBar` and display over content when opened. |

## DrawerVariant

Indicates the behavior of a `MudDrawer`.

| Value | CSS name | Meaning |
|---|---|---|
| `Temporary` | `temporary` | The drawer will open above all other content until a section is selected. |
| `Responsive` | `responsive` | The drawer behaves like `Persistent` in wider screens, but `Temporary` on smaller screens. |
| `Persistent` | `persistent` | The drawer will open outside of its container, shifting other contents when opened. |
| `Mini` | `mini` | The drawer has a small width on larger screens and can expand when hovered, but behaves like `Temporary` below its breakpoint. |

## DropdownWidth

Indicates the behavior of a `MudPopover` drop down relative width.

| Value | CSS name | Meaning |
|---|---|---|
| `Relative` | `relative` | The dropdown will open at the max width of it's activator parent preventing it from growing beyond that width. |
| `Adaptive` | `adaptive` | The dropdown will open at the min width of it's activator parent, preventing it from being less wide but allowing it to grow. |
| `Ignore` | `ignore` | The dropdown width will be ignored. |

## Edge

Specifies where a negative margin is applied within a layout component. This is typically used in conjunction with elements that have leading or trailing adornments.

| Value | CSS name | Meaning |
|---|---|---|
| `False` | `false` | No negative margin is applied to the element. |
| `Start` | `start` | A negative margin is applied to the start of the element. |
| `End` | `end` | A negative margin is applied to the end of the element. |

## HorizontalAlignment

The position of a component relative to its container.

| Value | CSS name | Meaning |
|---|---|---|
| `Center` | `center` | The component is horizontally centered. |
| `Left` | `left` | The component is aligned to the left. |
| `Right` | `right` | The component is aligned to the right. |
| `Start` | `start` | The component is aligned based on Right-to-Left (RTL) settings. |
| `End` | `end` | The component is aligned based on Right-to-Left (RTL) settings. |

## InputMode

The inputmode global attribute is an enumerated attribute that hints at the type of data that might be entered by the user while editing the element or its contents. Not supported by safari. Use Pattern to achieve special mobile keyboards in safari. https://developer.mozilla.org/docs/Web/HTML/Global_attributes/inputmode

| Value | CSS name | Meaning |
|---|---|---|
| `none` | `none` | No virtual keyboard. For when the page implements its own keyboard input control. <a href="https://developer.mozilla.org/docs/Web/HTML/Global_attributes/inputmode#none">Reference</a> |
| `text` | `text` | Default. Standard input keyboard for the user's current locale. <a href="https://developer.mozilla.org/docs/Web/HTML/Global_attributes/inputmode#text">Reference</a> |
| `numeric` | `numeric` | Fractional numeric input keyboard containing the digits and decimal separator for the user's locale (typically . or ,). Devices may or may not show a minus key (-). <a href="https://developer.mozilla.org/docs/Web/HTML/Global_attributes/inputmode#decimal">Reference</a> |
| `tel` | `tel` | A telephone keypad input, including the digits 0–9, the asterisk (*), and the pound (#) key. Inputs that require a telephone number should typically use &lt;input type="tel"&gt;instead. <a href="https://developer.mozilla.org/docs/Web/HTML/Global_attributes/inputmode#tel">Reference</a> |
| `search` | `search` | A virtual keyboard optimized for search input. For instance, the return/submit key may be labeled “Search”, along with possible other optimizations. Inputs that require a search query should typically use &lt;input type="search"&gt; instead. <a href="https://developer.mozilla.org/docs/Web/HTML/Global_attributes/inputmode#search">Reference</a> |
| `email` | `email` | A virtual keyboard optimized for entering email addresses. Typically includes the @ character as well as other optimizations. Inputs that require email addresses should typically use &lt;input type="email"&gt; instead. <a href="https://developer.mozilla.org/docs/Web/HTML/Global_attributes/inputmode#email">Reference</a> |
| `url` | `url` | A keypad optimized for entering URLs. This may have the / key more prominent, for example. Enhanced features could include history access and so on. Inputs that require a URL should typically use &lt;input type="url"&gt; instead. <a href="https://developer.mozilla.org/docs/Web/HTML/Global_attributes/inputmode#url">Reference</a> |

## InputSizing

The strategy for how the input calculates its height.

| Value | CSS name | Meaning |
|---|---|---|
| `Fixed` | `fixed` | The height is fixed based on the Lines property. |
| `Auto` | `auto` | The height grows and shrinks dynamically to fit the text content. Uses Lines as minimum and MaxLines as maximum. |

## InputType

The type of an HTML input element.

| Value | CSS name | Meaning |
|---|---|---|
| `Text` | `text` |  |
| `Password` | `password` |  |
| `Email` | `email` |  |
| `Hidden` | `hidden` |  |
| `Number` | `number` |  |
| `Search` | `search` |  |
| `Telephone` | `tel` |  |
| `Url` | `url` |  |
| `Color` | `color` |  |
| `Date` | `date` |  |
| `DateTimeLocal` | `datetime-local` |  |
| `Month` | `month` |  |
| `Time` | `time` |  |
| `Week` | `week` |  |

## InterpolationOption

Indicates the technique used to smooth lines connecting values in a `MudAxisLineChartBase{T, TOptions}`.

| Value | CSS name | Meaning |
|---|---|---|
| `NaturalSpline` | – | Lines are smoothed to pass through each data point as a natural spline. |
| `EndSlope` | – | Lines are smoothed to pass through each data point as an end-point spline. |
| `Periodic` | – | Lines are smoothed to pass through each data point as a periodic spline. |
| `Straight` | – | Lines are straight from one point to the next. |

## JsKey

Contains all Javascript key code strings (using e.code standard).

| Value | CSS name | Meaning |
|---|---|---|
| `Backspace` | – |  |
| `Tab` | – |  |
| `Enter` | – |  |
| `ShiftLeft` | – |  |
| `ShiftRight` | – |  |
| `ControlLeft` | – |  |
| `ControlRight` | – |  |
| `AltLeft` | – |  |
| `AltRight` | – |  |
| `Pause` | – |  |
| `CapsLock` | – |  |
| `Escape` | – |  |
| `Space` | – |  |
| `PageUp` | – |  |
| `PageDown` | – |  |
| `End` | – |  |
| `Home` | – |  |
| `ArrowLeft` | – |  |
| `ArrowUp` | – |  |
| `ArrowRight` | – |  |
| `ArrowDown` | – |  |
| `PrintScreen` | – |  |
| `Insert` | – |  |
| `Delete` | – |  |
| `Digit0` | – |  |
| `Digit1` | – |  |
| `Digit2` | – |  |
| `Digit3` | – |  |
| `Digit4` | – |  |
| `Digit5` | – |  |
| `Digit6` | – |  |
| `Digit7` | – |  |
| `Digit8` | – |  |
| `Digit9` | – |  |
| `KeyA` | – |  |
| `KeyB` | – |  |
| `KeyC` | – |  |
| `KeyD` | – |  |
| `KeyE` | – |  |
| `KeyF` | – |  |
| `KeyG` | – |  |
| `KeyH` | – |  |
| `KeyI` | – |  |
| `KeyJ` | – |  |
| `KeyK` | – |  |
| `KeyL` | – |  |
| `KeyM` | – |  |
| `KeyN` | – |  |
| `KeyO` | – |  |
| `KeyP` | – |  |
| `KeyQ` | – |  |
| `KeyR` | – |  |
| `KeyS` | – |  |
| `KeyT` | – |  |
| `KeyU` | – |  |
| `KeyV` | – |  |
| `KeyW` | – |  |
| `KeyX` | – |  |
| `KeyY` | – |  |
| `KeyZ` | – |  |
| `MetaLeft` | – |  |
| `MetaRight` | – |  |
| `ContextMenu` | – |  |
| `Numpad0` | – |  |
| `Numpad1` | – |  |
| `Numpad2` | – |  |
| `Numpad3` | – |  |
| `Numpad4` | – |  |
| `Numpad5` | – |  |
| `Numpad6` | – |  |
| `Numpad7` | – |  |
| `Numpad8` | – |  |
| `Numpad9` | – |  |
| `NumpadMultiply` | – |  |
| `NumpadAdd` | – |  |
| `NumpadSubtract` | – |  |
| `NumpadDecimal` | – |  |
| `NumpadDivide` | – |  |
| `F1` | – |  |
| `F2` | – |  |
| `F3` | – |  |
| `F4` | – |  |
| `F5` | – |  |
| `F6` | – |  |
| `F7` | – |  |
| `F8` | – |  |
| `F9` | – |  |
| `F10` | – |  |
| `F11` | – |  |
| `F12` | – |  |
| `NumLock` | – |  |
| `ScrollLock` | – |  |
| `AudioVolumeMute` | – |  |
| `AudioVolumeDown` | – |  |
| `AudioVolumeUp` | – |  |
| `MediaTrackNext` | – |  |
| `MediaTrackPrevious` | – |  |
| `MediaPlayPause` | – |  |
| `Semicolon` | – |  |
| `Equal` | – |  |
| `Comma` | – |  |
| `Minus` | – |  |
| `Period` | – |  |
| `Slash` | – |  |
| `Backquote` | – |  |
| `BracketLeft` | – |  |
| `Backslash` | – |  |
| `BracketRight` | – |  |
| `Quote` | – |  |
| `NumpadEnter` | – |  |
| `NumpadEqual` | – |  |
| `NumpadComma` | – |  |

## JsKeyModifier

Contains all Javascript modifier key code strings (using e.code standard).

| Value | CSS name | Meaning |
|---|---|---|
| `ShiftLeft` | – |  |
| `ShiftRight` | – |  |
| `ControlLeft` | – |  |
| `ControlRight` | – |  |
| `AltLeft` | – |  |
| `AltRight` | – |  |
| `MetaLeft` | – |  |
| `MetaRight` | – |  |

## Justify

The horizontal distribution of child items in a `MudStack` component.

| Value | CSS name | Meaning |
|---|---|---|
| `FlexStart` | `start` | Items are aligned to the start of the `MudStack`. |
| `Center` | `center` | Items are centered horizontally. |
| `FlexEnd` | `end` | Items are aligned to the end of the `MudStack`. |
| `SpaceBetween` | `space-between` | Space is applied between each item, with items aligned against the start and end. |
| `SpaceAround` | `space-around` | Space is applied between each item, with additional spacing for the first and last item. |
| `SpaceEvenly` | `space-evenly` | Space is applied evenly between each item, including the edges of the first and last item. |

## KeyEventKind

Specifies whether a keyboard event is a key-down or key-up event.

| Value | CSS name | Meaning |
|---|---|---|
| `Down` | – | Represents a key down event. |
| `Up` | – | Represents a key up event. |

## LineDisplayType

Specifies whether a series is drawn as a plain line or as a line with the area beneath it filled.

| Value | CSS name | Meaning |
|---|---|---|
| `Line` | – | Display as a plain line. |
| `Area` | – | Display as a line with the area below it filled. |

## Margin

Indicates the amount of spacing to apply.

| Value | CSS name | Meaning |
|---|---|---|
| `None` | `none` | No spacing is applied. |
| `Dense` | `dense` | Compact spacing is applied. |
| `Normal` | `normal` | Normal spacing is applied. |

## MaxWidth

A maximum width based on a responsive breakpoint.

| Value | CSS name | Meaning |
|---|---|---|
| `Large` | `lg` |  |
| `Medium` | `md` |  |
| `Small` | `sm` |  |
| `ExtraLarge` | `xl` |  |
| `ExtraExtraLarge` | `xxl` |  |
| `ExtraSmall` | `xs` |  |
| `False` | `false` |  |

## MouseEvent

Indicates the action which displays a `MudMenu`.

| Value | CSS name | Meaning |
|---|---|---|
| `LeftClick` | – | The left mouse button was clicked. |
| `RightClick` | – | The right mouse button was clicked. |
| `MouseOver` | – | The mouse is hovering over the activator. |

## MudColorComparison

Which color values are compared when testing two `MudColor` values for equality.

| Value | CSS name | Meaning |
|---|---|---|
| `Rgba` | – |  |
| `Hsl` | – |  |
| `RgbaAndHsl` | – |  |

## MudColorOutputFormats

Specifies different output formats for `MudColor`.

| Value | CSS name | Meaning |
|---|---|---|
| `Hex` | – | Output will be starting with a # and include r,g and b but no alpha values. Example #ab2a3d |
| `HexA` | – | Output will be starting with a # and include r,g and b and alpha values. Example #ab2a3dff |
| `RGB` | – | Will output css like output for value. Example rgb(12,15,40) |
| `RGBA` | – | Will output css like output for value with alpha. Example rgba(12,15,40,0.42) |
| `ColorElements` | – | Will output the color elements without any decorator and without alpha. Example 12,15,26 |

## ObjectFit

Indicates how an object is sized relative to its container.

| Value | CSS name | Meaning |
|---|---|---|
| `None` | `none` | The image is cropped to fit within its container. |
| `Cover` | `cover` | The content is sized to maintain its aspect ratio while filling the container. |
| `Contain` | `contain` | The content is scaled to maintain its aspect ratio while filling the container. |
| `Fill` | `fill` | The content is sized to fill the container. |
| `ScaleDown` | `scale-down` | The content is sized as if `None` or `Contain` were specified, whichever would result in a smaller object size. |

## ObjectPosition

Indicates the position of an object relative to its container.

| Value | CSS name | Meaning |
|---|---|---|
| `Center` | `center` | The object is centered vertically and horizontally. |
| `Top` | `top` | The top of the object is aligned with the top of its container. |
| `Bottom` | `bottom` | The bottom of the object is aligned with the bottom of its container. |
| `Left` | `left` | The left of the object is aligned with the left of its container. |
| `LeftTop` | `left-top` | The left and top of the object is aligned with the left and top of its container. |
| `LeftBottom` | `left-bottom` | The left and bottom of the object is aligned with the left and bottom of its container. |
| `Right` | `right` | The right of the object is aligned with the right of its container. |
| `RightTop` | `right-top` | The right and top of the object is aligned with the right and top of its container. |
| `RightBottom` | `right-bottom` | The right and bottom of the object is aligned with the right and bottom of its container. |

## OpenTo

Indicates the initial view of a date or time picker component.

| Value | CSS name | Meaning |
|---|---|---|
| `None` | – | No default view. |
| `Date` | – | The day picker is displayed. |
| `Year` | – | The year picker is displayed. |
| `Month` | – | The month picker is displayed. |
| `Hours` | – | The hours picker is displayed. |
| `Minutes` | – | The minutes picker is displayed. |

## Orientation

Indicates the display orientation of a `MudPicker{T}`.

| Value | CSS name | Meaning |
|---|---|---|
| `Portrait` | `portrait` | The picker is taller than it is wide, with a title on top. |
| `Landscape` | `landscape` | The picker is wider than it is tall, with a title on the left. |

## Origin

Indicates the position or direction a component is displayed relative to its parent container.

| Value | CSS name | Meaning |
|---|---|---|
| `TopLeft` | `top-left` | The component's top-left corner is at the container's top-left corner. |
| `TopCenter` | `top-center` | The component is centered on the container's top center. |
| `TopRight` | `top-right` | The component's top-left corner is at the container's top-right corner. |
| `CenterLeft` | `center-left` | The component's top-left corner is at the left of the container, and its center vertically. |
| `CenterCenter` | `center-center` | The component's top-left corner is at the center of the container. |
| `CenterRight` | `center-right` | The component's top-left corner is at the right of the container, and its center vertically. |
| `BottomLeft` | `bottom-left` | The component's top-left corner is at the container's bottom-left corner. |
| `BottomCenter` | `bottom-center` | The component is centered on the container's bottom center. |
| `BottomRight` | `bottom-right` | The component's top-left corner is at the container's bottom-right corner. |

## OverflowBehavior

Controls how a component behaves when the browser is scrolled.

| Value | CSS name | Meaning |
|---|---|---|
| `FlipNever` | `flip-never` | Prevents any adjustment of the component, even if it would overflow the container. |
| `FlipOnOpen` | `flip-onopen` | Flips the component if it would overflow its container, but only when it first opens. Does not update dynamically if overflow changes afterwards. |
| `FlipAlways` | `flip-always` | Flips the component if it would overflow its container, dynamically adjusting as necessary to prevent overflow. |

## Page

Indicates a pagination behavior.

| Value | CSS name | Meaning |
|---|---|---|
| `First` | – | Navigate to the first page of results. |
| `Previous` | – | Navigate to the previous page of results. |
| `Next` | – | Navigate to the next page of results. |
| `Last` | – | Navigate to the last page of results. |

## PagerPosition

The position of the pager for a `MudTable{T}` component.

| Value | CSS name | Meaning |
|---|---|---|
| `Bottom` | – | Display the pager at the bottom of the table. |
| `Top` | – | Display the pager at the top of the table. |
| `TopAndBottom` | – | Display the pager at both the top and bottom of the table. |

## PickerVariant

Indicates the display behavior of a `MudPicker{T}` component.

| Value | CSS name | Meaning |
|---|---|---|
| `Inline` | `inline` | The picker displays when the input is clicked. |
| `Dialog` | `dialog` | A dialog is displayed to pick a value. |
| `Static` | `static` | The picker is always visible. |

## Placement

The position of an element relative to its anchor.

| Value | CSS name | Meaning |
|---|---|---|
| `Left` | `left` |  |
| `Right` | `right` |  |
| `End` | `end` |  |
| `Start` | `start` |  |
| `Top` | `top` |  |
| `Bottom` | `bottom` |  |

## PopoverHolderOperation

Indicates whether a popover holder is being created, removed, or updated in the `IPopoverService`.

| Value | CSS name | Meaning |
|---|---|---|
| `Create` | – | Specifies the creation operation for a popover holder. |
| `Remove` | – | Specifies the removal operation for a popover holder. |
| `Update` | – | Specifies the update operation for a popover holder. |

## Position

The position of an element relative to its container.

| Value | CSS name | Meaning |
|---|---|---|
| `Bottom` | `bottom` |  |
| `Center` | `center` |  |
| `Top` | `top` |  |
| `Left` | `left` |  |
| `Right` | `right` |  |
| `Start` | `start` |  |
| `End` | `end` |  |

## ResizeMode

Indicates the column resizing behavior for a `MudDataGrid{T}`.

| Value | CSS name | Meaning |
|---|---|---|
| `None` | `none` | Nothing happens when the grid is resized. |
| `Column` | `column` | Columns can be expanded a limited amount, ensuring all columns remain visible. |
| `Container` | `container` | Columns can be expanded any amount; the grid width will be expanded. |

## ScatterSeriesType

Determines how a series is rendered on a `ScatterPlot{T}` chart.

| Value | CSS name | Meaning |
|---|---|---|
| `Points` | – | Renders data as individual scatter point markers (default). |
| `Line` | – | Renders data as a continuous line, useful for regression lines or trend overlays. |

## ScrollBehavior

Specifies whether a scroll animates smoothly or jumps immediately, matching the CSS `scroll-behavior` property.

| Value | CSS name | Meaning |
|---|---|---|
| `Smooth` | `smooth` | Scrolls in a smooth fashion. |
| `Auto` | `auto` | Scrolls immediately. |

## SelectionMode

Indicates the types of selections allowed.

| Value | CSS name | Meaning |
|---|---|---|
| `SingleSelection` | `single-selection` | One selection is allowed at a time. |
| `MultiSelection` | `multi-selection` | More than one selection is allowed. |
| `ToggleSelection` | `toggle-selection` | One selection is toggled. |

## Severity

The severity level of a status or message.

| Value | CSS name | Meaning |
|---|---|---|
| `Normal` | `normal` |  |
| `Info` | `info` |  |
| `Success` | `success` |  |
| `Warning` | `warning` |  |
| `Error` | `error` |  |

## Size

Indicates the size of a component.

| Value | CSS name | Meaning |
|---|---|---|
| `Small` | `small` | The smallest size. |
| `Medium` | `medium` | A medium size. |
| `Large` | `large` | The largest size. |

## SkeletonType

Indicates the shape of a `MudSkeleton` component.

| Value | CSS name | Meaning |
|---|---|---|
| `Text` | `text` | The skeleton is a placeholder for text. |
| `Circle` | `circle` | The skeleton displays a circle shape. |
| `Rectangle` | `rectangle` | The skeleton displays a rectangle shape. |

## SnackbarDuplicatesBehavior

Controls what happens when duplicate snackbars are detected.

| Value | CSS name | Meaning |
|---|---|---|
| `Allow` | – | Duplicate snackbars are allowed. |
| `Prevent` | – | Duplicate snackbars will not be displayed. |
| `GlobalDefault` | – | The global default is used to control duplicate snackbars. |

## SortDirection

Indicates the direction that search results are sorted by.

| Value | CSS name | Meaning |
|---|---|---|
| `None` | `none` | No sort direction. |
| `Ascending` | `ascending` | Results are sorted in ascending order (A-Z). |
| `Descending` | `descending` | Results are sorted in descending order (Z-A). |

## SortMode

Indicates the sorting mode for a `MudDataGrid{T}`.

| Value | CSS name | Meaning |
|---|---|---|
| `None` | `none` | Sorting is not allowed. |
| `Single` | `single` | Sorting can occur for one column at a time. |
| `Multiple` | `multiple` | Sorting can be done for multiple columns. |

## StepAction

Indicates the requested behavior of a button in a `MudStepper` component.

| Value | CSS name | Meaning |
|---|---|---|
| `Activate` | – | A request to activate a step. |
| `Complete` | – | A request to complete the last step. |
| `Skip` | – | A request to skip the current step. |
| `Reset` | – | A request to start over at the first step. |

## StretchItems

Specifies how items in a flex container are stretched along the main axis.

| Value | CSS name | Meaning |
|---|---|---|
| `None` | `none` | No stretching is applied. |
| `Start` | `start` | The first item is stretched. |
| `End` | `end` | The last item is stretched. |
| `StartAndEnd` | `start-and-end` | The first and last items are stretched. |
| `Middle` | `middle` | All items except for the first and last are stretched. |
| `All` | `all` | All items are stretched evenly. |

## SwipeDirection

The direction of a swipe event for a `MudSwipeArea` component.

| Value | CSS name | Meaning |
|---|---|---|
| `None` | – | The swipe direction is unknown. |
| `LeftToRight` | – | The swipe is happening from left to right. |
| `RightToLeft` | – | The swipe is happening from right to left. |
| `TopToBottom` | – | The swipe is happening from top to bottom. |
| `BottomToTop` | – | The swipe is happening from bottom to top. |

## TabHeaderPosition

The location of the `Header`

| Value | CSS name | Meaning |
|---|---|---|
| `After` | `after` | Additional content is placed after the first tab. |
| `Before` | `before` | Additional content is placed before the first tab. |
| `None` | `none` | No additional content is shown. |

## TabInteractionType

The type of user interaction when `OnPreviewInteraction` occurs.

| Value | CSS name | Meaning |
|---|---|---|
| `Activate` | – | An attempt to activate a tab panel. |

## TableApplyButtonPosition

Indicates the position of the commit button during inline edits to a `MudTable{T}`.

| Value | CSS name | Meaning |
|---|---|---|
| `Start` | – | The commit button is at the start of the row. |
| `End` | – | The commit button is at the end of the row. |
| `StartAndEnd` | – | The commit button is at both the start and end of the row. |

## TableEditButtonPosition

Indicates the position of the edit button which starts inline edits for a `MudTable{T}`.

| Value | CSS name | Meaning |
|---|---|---|
| `Start` | – | The edit button is at the start of the row. |
| `End` | – | The edit button is at the end of the row. |
| `StartAndEnd` | – | The edit button is both at the start and end of the row. |

## TableEditTrigger

Indicates the behavior which begins inline editing for a `MudTable{T}`.

| Value | CSS name | Meaning |
|---|---|---|
| `RowClick` | – | Editing begins when a row is clicked. |
| `EditButton` | – | Editing begins when the edit button is clicked. |

## TimeEditMode

Indicates the editable values of a `MudTimePicker`.

| Value | CSS name | Meaning |
|---|---|---|
| `Normal` | – | Hours and minutes can be edited. |
| `OnlyMinutes` | – | Only minutes can be edited. |
| `OnlyHours` | – | Only hours can be edited. |

## TimelineAlign

Specifies whether each item's dot aligns to the start, center, or end of its text in a `MudTimeline`.

| Value | CSS name | Meaning |
|---|---|---|
| `Default` | `default` | The dot is centered relative to its text. |
| `Start` | `start` | The dot is aligned with the start of the text. |
| `End` | `end` | The dot is aligned with the end of the text. |

## TimelineOrientation

Specifies whether items in a `MudTimeline` are arranged vertically or horizontally.

| Value | CSS name | Meaning |
|---|---|---|
| `Vertical` | `vertical` | Items are displayed vertically. |
| `Horizontal` | `horizontal` | Items are displayed horizontally. |

## TimelinePosition

Specifies how items are drawn in a `MudTimeline`.

| Value | CSS name | Meaning |
|---|---|---|
| `Alternate` | `alternate` | Items alternate on either side of centered dots. |
| `Top` | `top` | Dots are displayed above the text of each timeline item. |
| `Bottom` | `bottom` | Dots are displayed below the text of each timeline item. |
| `Left` | `left` | Dots are displayed to the left of text for each timeline item. |
| `Right` | `right` | Dots are displayed to the right of text for each timeline item. |
| `Start` | `start` | Dots are displayed at the start based on the Right-to-Left setting of the `MudRTLProvider`. |
| `End` | `end` | Dots are displayed at the end based on the Right-to-Left setting of the `MudRTLProvider`. |

## Transition

The type of animation used when content transitions.

| Value | CSS name | Meaning |
|---|---|---|
| `None` | `None` |  |
| `Fade` | `Fade` |  |
| `Slide` | `Slide` |  |
| `Custom` | `Custom` |  |

## Typo

Typography controls the text throughout the theme, like font-family, size, and other settings.

| Value | CSS name | Meaning |
|---|---|---|
| `inherit` | `inherit` | Inherits the typography style from the parent element. |
| `h1` | `h1` | Applies the h1 typography style, using the `h1` HTML tag. |
| `h2` | `h2` | Applies the h2 typography style, using the `h2` HTML tag. |
| `h3` | `h3` | Applies the h3 typography style, using the `h3` HTML tag. |
| `h4` | `h4` | Applies the h4 typography style, using the `h4` HTML tag. |
| `h5` | `h5` | Applies the h5 typography style, using the `h5` HTML tag. |
| `h6` | `h6` | Applies the h6 typography style, using the `h6` HTML tag. |
| `subtitle1` | `subtitle1` | Applies the subtitle1 typography style, using the `p` HTML tag. |
| `subtitle2` | `subtitle2` | Applies the subtitle2 typography style, using the `p` HTML tag. |
| `body1` | `body1` | Applies the body1 typography style, using the `p` HTML tag. |
| `body2` | `body2` | Applies the body2 typography style, using the `p` HTML tag. |
| `button` | `button` | Applies the button typography style, using the `span` HTML tag. |
| `caption` | `caption` | Applies the caption typography style, using the `span` HTML tag. |
| `overline` | `overline` | Applies the overline typography style, using the `span` HTML tag. |

## Underline

Indicates how a `MudLink` is decorated.

| Value | CSS name | Meaning |
|---|---|---|
| `None` | `none` | No underline is displayed. |
| `Hover` | `hover` | An underline is displayed when hovering over the link. |
| `Always` | `always` | An underline is always displayed. |

## Variant

Indicates the display variation applied to a component.

| Value | CSS name | Meaning |
|---|---|---|
| `Text` | `text` | The component has no drop shadow, background or border. |
| `Filled` | `filled` | The component interior is filled with a solid color. |
| `Outlined` | `outlined` | The component has an outline around the edge. |

## Width

A width based on a responsive breakpoint.

| Value | CSS name | Meaning |
|---|---|---|
| `xs` | `xs` |  |
| `sm` | `sm` |  |
| `md` | `md` |  |
| `lg` | `lg` |  |
| `xl` | `xl` |  |
| `xxl` | `xxl` |  |
| `False` | `false` |  |

## Wrap

Indicates how items in a `MudStack` are wrapped.

| Value | CSS name | Meaning |
|---|---|---|
| `NoWrap` | `nowrap` | No wrapping occurs. |
| `Wrap` | `wrap` | Items are wrapped to fit the container. |
| `WrapReverse` | `wrap-reverse` | Behaves the same as wrap but cross-start and cross-end are permuted. |

## XAxisLabelPosition

Indicates the position of the X axis labels as either top or bottom in a `HeatMap`

| Value | CSS name | Meaning |
|---|---|---|
| `Top` | – | The X axis labels are displayed at the top of the chart centered horizontally. |
| `Bottom` | – | The X axis labels are displayed at the bottom of the chart centered horizontally. |
| `None` | – | Do not include X axis labels |

## YAxisLabelPosition

Indicates the position of the Y axis labels as either left or right in a `HeatMap`

| Value | CSS name | Meaning |
|---|---|---|
| `Left` | – | The Y axis labels are displayed at the left of the chart |
| `Right` | – | The Y Axis labels are displayed at the right of the chart |
| `None` | – | Do not include Y axis labels |
