# MudBlazor component index (generated from source)

Component → API reference file `references/api/<Folder>.md`.

| Component | Folder | Purpose |
|---|---|---|
| `MudAlert` | Alert | Displays an important message which is statically embedded in the page content. |
| `MudAppBar` | AppBar | Displays actions, branding, navigation and screen titles. Keep the app bar persistent while browsing different pages to ease navigation and access to actions for users. |
| `MudAutocomplete<T>` | Autocomplete | A text input for searching and selecting from a list of options. Unlike `MudSelect{T}`, it doesn't require the complete item list upfront and supports asynchronous search for database queries. |
| `MudAvatar` | Avatar | Represents a component which displays circular user profile pictures, icons or text. |
| `MudAvatarGroup` | Avatar | Represents a grouping of multiple `MudAvatar` components. |
| `MudAxisChartBase<T, TOptions>` | Chart | Serves as the base class for axis-based charts, providing core functionality for rendering and managing chart elements such as axes, grids, and legends. |
| `MudAxisLineChartBase<T, TOptions>` | Chart | Base class for line-based charts such as `Line{T}`, `ScatterPlot{T}`, and `TimeSeries{T}`. Generates the SVG line paths, area fills, and data-point markers, with optional interpolation. |
| `MudBadge` | Badge | Badges show notifications, counts, or status information on navigation items and icons. |
| `MudBaseDatePicker` | DatePicker | Base class for MudBlazor date pickers such as `MudDatePicker` and `MudDateRangePicker`. |
| `MudBreadcrumbs` | Breadcrumbs | Breadcrumbs show a navigation trail of links marking the user's current location within a page hierarchy. |
| `MudBreakpointProvider` | BreakpointProvider | Exposes the current breakpoint (xs, sm, md, lg, xl) to child components via a cascading parameter. |
| `MudButton` | Button | Buttons trigger actions, submit forms, or navigate to a link. |
| `MudButtonGroup` | ButtonGroup | Groups related `MudButton` components together visually. |
| `MudCard` | Card | Cards contain actions, text, or media like images or graphics. Keeping a card to a single subject keeps the design clean. |
| `MudCardActions` | Card | The action bar of a `MudCard`, typically holding buttons that trigger the card's related actions. |
| `MudCardContent` | Card | The primary content area of a `MudCard`, holding its text and body elements. |
| `MudCardHeader` | Card | The header area of a `MudCard`, typically holding an avatar, title, and action buttons. |
| `MudCardMedia` | Card | The media area of a `MudCard`, displaying an image or graphic sized to a set height. |
| `MudCarousel<TData>` | Carousel | Carousels cycle through a set of slides or images, transitioning automatically or when the user swipes, clicks arrows, or selects a bullet. |
| `MudCarouselItem` | Carousel | A single slide within a `MudCarousel{TData}`, holding the content shown while it is the selected item. |
| `MudChart<T>` | Chart | Charts plot numeric data as line, bar, stacked bar, pie, donut, radar, rose, heat map, time series, scatter, or Sankey graphics. Choose the graphic with the `ChartType` parameter. |
| `MudChartBase<T, TOptions>` | Chart | Base class for MudBlazor chart components, providing the data series, options, legend, and selection shared by every chart type. |
| `MudCheckBox<T>` | CheckBox | A form input for boolean values or selecting multiple items in a list. Use checkboxes (instead of switches or radio buttons) if multiple options can be selected from a list. |
| `MudChip<T>` | Chip | Compact elements used to enter information, select a choice, filter content, or trigger an action. |
| `MudChipSet<T>` | ChipSet | A collection of multiple `MudChip{T}` components that allows single or multi-selection. |
| `MudCollapse` | Collapse | A container for content which can be collapsed and expanded. |
| `MudColorPicker` | ColorPicker | Picks a color from a spectrum, palette, or predefined grid, with RGB, HSL, and hexadecimal inputs and optional alpha transparency. |
| `MudContainer` | Container |  |
| `MudContextualActionBar` | AppBar | A contextual app bar. |
| `MudDataGrid<T>` | DataGrid | Displays rows of data in a sortable, filterable grid with multiselection, pagination, inline editing, grouping, and aggregation. |
| `MudDataGridPager<T>` | DataGrid | Pagination controls for navigating pages of a `MudDataGrid{T}`, with page-size selection and next and previous buttons. |
| `MudDatePicker` | DatePicker | Selects a single date from a calendar shown in a drop-down, dialog, or inline. |
| `MudDateRangePicker` | DatePicker | Selects a start and end date range from a calendar shown in a drop-down, dialog, or inline. |
| `MudDebouncedInput<T>` | Input | Base class for MudBlazor inputs that wait for typing to pause before updating their value, such as `MudTextField{T}` and `MudNumericField{T}`. |
| `MudDialog` | Dialog | Displays an overlay that prompts users to confirm an action or provide additional information. |
| `MudDialogContainer` | Dialog | An instance of a `MudDialog`. |
| `MudDialogProvider` | Dialog | A manager for `MudDialog` instances. |
| `MudDivider` | Divider | A thin line that groups content in lists and layouts. Only use dividers if items can't be grouped with open space. Use dividers to group things, not separate individual items. |
| `MudDragAndDropIndexChangedEventArgs` | DropZone | The information related to a `MudDropZone{T}` index change event. |
| `MudDragAndDropItemTransaction<T>` | DropZone | The information related to a `MudDropZone{T}` drag-and-drop transaction. |
| `MudDragAndDropTransactionFinishedEventArgs<T>` | DropZone | The information related to a `MudDropZone{T}` completed drag-and-drop transaction. |
| `MudDragHandle<T>` | DropZone | A drag handle that restricts drag-and-drop initiation to a specific child element inside a `MudDynamicDropItem{T}`. |
| `MudDrawer` | Drawer | Navigation drawers, or sidebars, dock to the side of the page to hold navigation links, menus, or other content. |
| `MudDrawerContainer` | Drawer | A container for a `MudDrawer` component. |
| `MudDrawerHeader` | Drawer | Represents content at the top of a `MudDrawer`. |
| `MudDropContainer<T>` | DropZone | A container of `MudDropZone{T}` components for drag-and-drop operations. |
| `MudDropZone<T>` | DropZone | A location which can participate in a drag-and-drop operation. |
| `MudDynamicDropItem<T>` | DropZone | Wraps a single item inside a `MudDropZone{T}` so it can be dragged and dropped between zones using mouse or touch gestures. |
| `MudDynamicTabs` | Tabs | A tab component where the tabs are controlled dynamically, similar to browser tabs. |
| `MudElement` | Element | A primitive component which allows dynamically changing the HTML element rendered under the hood. |
| `MudExitPrompt` | ExitPrompt | Shows a confirmation dialog when the user tries to navigate away. |
| `MudExpansionPanel` | ExpansionPanel | Accordion-style collapsible panel within a `MudExpansionPanels` group that expands to reveal content or collapses to show only its header. |
| `MudExpansionPanels` | ExpansionPanel | A container which manages `MudExpansionPanel` components such that when one panel is expanded the others are collapsed automatically. |
| `MudFab` | Button | Floating action buttons (FABs) trigger the primary action on a page and float above content in a circular or extended shape. |
| `MudFabMenu` | Button | A menu appearing from a `MudFab` that displays a list of items. |
| `MudFabMenuItem` | Button | A floating action button shown as one of the selectable options within a `MudFabMenu`. |
| `MudField` | Field | Displays custom content inside a form field with the same label, adornment, and border styling as a `MudTextField{T}`. |
| `MudFileUpload<T>` | FileUpload | A form component that lets users upload one or more files. |
| `MudFlexBreak` | Grid | Forces a line break in a flexbox layout so the items that follow wrap onto a new line. |
| `MudFocusTrap` | FocusTrap | Prevents the keyboard focus from cycling out of its child content. Typically used within dropdown selectors and modal dialogs. |
| `MudForm` | Form | Collects and validates user input, monitoring and validating every input derived from MudFormComponent within it. |
| `MudGrid` | Grid | A 12-point grid system for organizing content with responsive breakpoints for different screen sizes. |
| `MudHeatMapCell<T>` | Chart | Overrides a single cell in a `HeatMap{T}` chart, replacing the value from the `ChartSeries{T}` or rendering custom SVG content inside the cell. |
| `MudHidden` | Hidden | Conditionally renders its content based on the current screen-size breakpoint, showing or hiding it as the viewport changes. |
| `MudHighlighter` | Highlighter | Highlights occurrences of one or more search terms within a block of text, wrapping each match in a `mark` element. |
| `MudHotkey` | Hotkey | Allows registering a hotkey. |
| `MudIcon` | Icon | A picture displayed via an SVG path or font. |
| `MudIconButton` | Button | A clickable icon for actions and commands. |
| `MudImage` | Image | A simple component that displays an image. |
| `MudInput<T>` | Input | Renders the underlying HTML input element used by text-based components such as `MudTextField{T}` and `MudNumericField{T}`. |
| `MudInputAdornment` | Input | An icon displayed within an input component. |
| `MudInputControl` | InputControl | Wraps a form input with its label, helper text, and validation message. |
| `MudInputLabel` | Input | A label which describes a `MudInput{T}` component. |
| `MudInputString` | Input | An input component for collecting alphanumeric values. |
| `MudItem` | Grid | A portion of a `MudGrid`. |
| `MudLayout` | Layout | Arranges the top-level page structure of an app with an app bar, navigation drawer, and main content area. |
| `MudLink` | Link | A clickable link which can navigate to a URL. |
| `MudList<T>` | List | A scrollable list for displaying text, avatars, and icons. Use lists to help users find a specific item and act on it. |
| `MudListItem<T>` | List | An item within a `MudList{T}` component. |
| `MudListSubheader` | List | A header displayed as part of a `MudList{T}`. |
| `MudMainContent` | Main | The main content region of a `MudLayout` where each page's content is rendered. |
| `MudMask` | Mask | A text input which conforms user input to a specific format while typing. Note that MudMask is recommended to be used in WASM projects only because it has known problems in BSS, especially with high network latency. |
| `MudMenu` | Menu | Displays a list of options that users can select from. Make menus easy to open, close, and select. Menus can open from a variety of components. |
| `MudMenuItem` | Menu | A choice displayed as part of a list within a `MudMenu` component. |
| `MudMessageBox` | MessageBox | A pop-up dialog with a simple message and button choices. |
| `MudNavGroup` | NavMenu | A deeper level of navigation links as part of a `MudNavMenu`. |
| `MudNavLink` | NavMenu | A navigation link as part of a `MudNavMenu`. |
| `MudNavMenu` | NavMenu | A list of navigation links with support for groups. |
| `MudNumericField<T>` | NumericField | A field for numeric values from users. |
| `MudOverlay` | Overlay | Renders a translucent layer over content, typically used for modals, popovers, progress bars, or blocking interactions. |
| `MudPageContentNavigation` | PageContentNavigation | A drawer used to navigate sections on a page. |
| `MudPageContentSection` | PageContentNavigation | A section (nav link) inside the MudPageContentNavigation |
| `MudPagination` | Pagination | A list of clickable page numbers along with navigation buttons. |
| `MudPaper` | Paper | A surface for grouping other components, generally used for foregrounds and can be combined with Flex for layout. |
| `MudPicker<T>` | Picker | Base class for MudBlazor pickers such as `MudDatePicker`, `MudTimePicker`, and `MudColorPicker`. |
| `MudPickerContent` | Picker | The content within a `MudPicker{T}`. |
| `MudPickerToolbar` | Picker | The toolbar content of a `MudPicker{T}`. |
| `MudPopover` | Popover | Displays content as a window over other content. |
| `MudPopoverBase` | Popover | Base class for popover components such as `MudPopover`, handling creation and lifecycle through the `IPopoverService`. |
| `MudPopoverProvider` | Popover | A required component which manages all MudBlazor popovers. |
| `MudProgressCircular` | Progress | Informs users about the status of ongoing processes, such as loading an app, submitting a form, or saving updates. Shows either the length of a process or unspecified wait time. |
| `MudProgressLinear` | Progress | A line-shaped indicator of progress for an ongoing operation. |
| `MudRTLProvider` | RTLProvider | A language support provider for Right-to-Left (RTL) languages such as Arabic, Hebrew, and Persian. |
| `MudRadialChartBase<T, TOptions>` | Chart | Base class for radial charts such as `Pie{T}`, `Donut{T}`, `Radar{T}`, and `Rose{T}`. Aggregates and normalizes series data into circular segments and legends. |
| `MudRadio<T>` | Radio | Allows the user to select a single choice from a group of options. Use radio buttons (not switches) when only one item can be selected from a list. |
| `MudRadioGroup<T>` | Radio | A group of `MudRadio{T}` components. |
| `MudRangeInput<T>` | Input | Collects start and end values that define a range using two input fields, as used by the `MudDateRangePicker`. |
| `MudRating` | Rating | Ratings provide insight regarding other's opinions and experiences with a product. Collecting user feedback via ratings is a simple analytic that can provide a lot of feedback to your product or application. |
| `MudRatingItem` | Rating | A clickable item as part of a `MudRating`. |
| `MudRender` | Render |  |
| `MudScrollToTop` | ScrollToTop | A button to quickly return to the top of the page. |
| `MudSelect<T>` | Select | A dropdown input for selecting an item from a list of options. |
| `MudSelectItem<T>` | Select | A selectable option displayed within a `MudSelect{T}` component. |
| `MudSimpleTable` | TableSimple | A table similar to `MudTable{T}` but with basic styling features. |
| `MudSkeleton` | Skeleton | Displays a placeholder preview of content before the data gets loaded, reducing load-time frustration. |
| `MudSlider<T>` | Slider | Allows users to select a value within a specified range. Sliders should present the full range of available values and the value should take effect immediately. |
| `MudSnackbarElement` | Snackbar | Renders a single snackbar notification within a `MudSnackbarProvider`. |
| `MudSnackbarProvider` | Snackbar | Displays snackbar notifications queued through the `ISnackbar` service, positioning and stacking them on the page. |
| `MudSpacer` | Spacer |  |
| `MudSplitPanel` | SplitPanel | Allows users to dynamically resize content with a draggable splitter. |
| `MudStack` | Stack | Manages layout of its child items along the vertical or horizontal axis with optional spacing. |
| `MudStep` | Stepper | A individual step as part of a `MudStepper`. |
| `MudStepContext` | Stepper | Provides contextual information about a `MudStep` within a `MudStepper`. |
| `MudStepper` | Stepper | Guides users through a series of steps to complete a transaction, such as forms or wizards. |
| `MudSwipeArea` | SwipeArea | Detects and responds to swipe gestures for navigation or actions. |
| `MudSwitch<T>` | Switch | Toggles between two values with the tap of a button, visually distinct from checkboxes. Use switches (not radio buttons) if the items in a list can be independently controlled. |
| `MudTFootRow` | Table | A footer row displayed at the bottom of a `MudTable{T}` and each group. |
| `MudTHeadRow` | Table | A header row displayed at the top of a `MudTable{T}` and each group. |
| `MudTabPanel` | Tabs | A tab as part of a `MudTabs` or `MudDynamicTabs` component. |
| `MudTable<T>` | Table | A sortable, filterable table with multiselection, pagination, responsive layout, and child rows. |
| `MudTableBase` | Table | Base class for `MudTable{T}` holding the type-independent table members such as paging, layout, and editing options. |
| `MudTableGroupRow<T>` | Table | A grouping of values for a column in a `MudTable{T}`. |
| `MudTablePager` | Table | Pagination controls for a `MudTable{T}` that navigate between pages and change the number of rows shown per page. |
| `MudTableSortLabel<T>` | Table | A clickable column which toggles the sort column and direction for a `MudTable{T}`. |
| `MudTabs` | Tabs | Organizes content across multiple tab pages. |
| `MudTd` | Table | A cell within a `MudTr`, `MudTHeadRow`, or `MudTFootRow` row component. |
| `MudText` | Typography | A customizable piece of text. |
| `MudTextField<T>` | TextField | An input for collecting text values. |
| `MudTh` | Table | A header cell which labels a column of data for a `MudTable{T}`. |
| `MudThemeProvider` | ThemeProvider | Provides a standard set of colors, shapes, sizes and shadows to a layout. |
| `MudTimePicker` | TimePicker | Selects a time of day from a clock shown in a drop-down, dialog, or inline. |
| `MudTimeline` | Timeline | Displays items in chronological order. |
| `MudTimelineItem` | Timeline | A chronological item displayed as part of a `MudTimeline` |
| `MudToggleGroup<T>` | Toggle | Toggle buttons grouped to select one or multiple values. |
| `MudToggleIconButton` | Button | An icon button that toggles between two distinct states, useful for on/off or favorite/unfavorite scenarios. |
| `MudToggleItem<T>` | Toggle | An item as part of a `MudToggleGroup{T}` |
| `MudToolBar` | ToolBar | A set of action buttons. |
| `MudTooltip` | Tooltip | Displays additional context when users hover over or focus on an element. |
| `MudTooltipChildContainer` | Tooltip | Renders its child content only when `UpdateCount` changes, so a host's internal state changes do not rebuild that content. |
| `MudTr` | Table | A row of data within a `MudTable{T}`. |
| `MudTreeView<T>` | TreeView | An extensively customizable tree view component for displaying hierarchical data, featuring item selection, lazy-loading, and templating support. |
| `MudTreeViewItem<T>` | TreeView | An expandable branch of a `MudTreeView{T}`. |
| `MudTreeViewItemToggleButton` | TreeView | Toggles the expansion state of a `MudTreeViewItem{T}`. |
| `MudVirtualize<T>` | Virtualize | Renders a large list of items efficiently by creating DOM elements only for the rows currently in view. Wraps Blazor's `Virtualize{T}`. |