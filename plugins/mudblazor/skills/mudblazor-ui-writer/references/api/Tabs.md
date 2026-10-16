# Tabs components — API (generated from source)

## MudDynamicTabs : MudTabs

A tab component where the tabs are controlled dynamically, similar to browser tabs.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `AddTabIcon` | `string` | `Icons.Material.Filled.Add` | The icon for the add button. Defaults to `Add`. |
| `CloseTabIcon` | `string` | `Icons.Material.Filled.Close` | The icon for the close button. Defaults to `Close`. |
| `AddIconClass` | `string` | `string.Empty` | Occurs when the "Add" button has been clicked. Defaults to `""`. Multiple classes must be separated by spaces. |
| `AddIconStyle` | `string` | `string.Empty` | **[Obsolete]** The CSS styles applied to the "Add" button. Defaults to `""`. |
| `CloseIconClass` | `string` | `string.Empty` | The CSS classes applied to the "Close" button. Defaults to `""`. Multiple classes must be separated by spaces. |
| `CloseIconStyle` | `string` | `string.Empty` | **[Obsolete]** The CSS styles applied to the "Close" button. Defaults to `""`. |
| `AddIconToolTip` | `string` | `string.Empty` | The text shown when the user hovers over the "Add" button. Defaults to `""`. When `null` or empty, no tooltip will be shown. |
| `CloseIconToolTip` | `string` | `string.Empty` | The text shown when the user hovers over the "Close" button. Defaults to `""`. When `null` or empty, no tooltip will be shown. |

## MudTabPanel : MudComponentBase

A tab as part of a `MudTabs` or `MudDynamicTabs` component.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Text` | `string?` | `null` | The title of this tab panel. Defaults to `null`. Only applies when `TabContent` is not set. |
| `Icon` | `string?` | `null` | The icon for this tab. Defaults to `null`. |
| `IconColor` | `Color` | `Default` | The color of this tab's icon. Defaults to `Default`. When set, overrides the `IconColor` property. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this panel. Defaults to `false`. |
| `Visible` | `bool` | `true` | Shows the tab. Defaults to `true`. |
| `ShowCloseIcon` | `bool` | `true` | For dynamic tabs, shows a "Close" icon for this tab. Defaults to `true`. Only applies within a `MudDynamicTabs` component. |
| `BadgeData` | `object?` | `null` | The badge shown for this tab. Defaults to `null`. Typically a string such as `"3"` or `"live"`. |
| `BadgeMax` | `int` | `99` | The maximum number allowed in the badge. Defaults to `99`. Applies when `BadgeData` is an `int`. |
| `BadgeIcon` | `string?` | – | Optional icon to be shown in the badge instead of text. |
| `BadgeDot` | `bool` | `false` | Shows a dot instead of text or icon for the badge. Defaults to `false`. When `true`, a dot instead of `BadgeData` is displayed. |
| `BadgeColor` | `Color` | `Color.Primary` | The color of the badge. Defaults to `Primary`. Applies when `BadgeData` is set. |
| `ID` | `object?` | `null` | The unique ID for this panel. Defaults to `null`. Should be unique across tabs. Useful for activating tabs manually via the `ActivatePanel` method of the `MudTabs` and `MudDynamicTabs` components. |
| `OnClick` | `EventCallback<MouseEventArgs>` | – | Occurs when this tab is clicked. |
| `OnMouseDown` | `EventCallback<MouseEventArgs>` | – | Gets or sets the callback that is invoked when a mouse down event occurs. |
| `OnContextMenu` | `EventCallback<MouseEventArgs>` | – | Gets or sets the callback that is invoked when a context menu event occurs. |
| `ChildContent` | `RenderFragment?` | – | The content within this tab. |
| `TabContent` | `RenderFragment?` | `null` | The content within this tab's title. Defaults to `null`. Typically used to display more than just text in the title. For basic text, use the `Text` parameter. |
| `TabWrapperContent` | `RenderFragment<RenderFragment>?` | `null` | The content enclosing this tab. Defaults to `null`. Typically used to wrap the entire tab content in other content, such as a `MudTooltip`, which wraps the content they refer to. |
| `ToolTip` | `string?` | `null` | The tooltip displayed for this tab. Defaults to `null`. Only applies when `TabContent` is not set. |
| `SortKey` | `string?` | `null` | Value to use when ordering tabs lexicographically, in place of `Text`. Defaults to `null`. |
| `PanelClass` | `string?` | `null` | The CSS classes applied to the panel. The `Class` property applies to the tab button only. Defaults to `null`. Multiple classes must be separated by spaces. |

## MudTabs : MudComponentBase

Organizes content across multiple tab pages.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `EnableDragAndDrop` | `bool` | `false` | Enables drag-and-drop re-ordering of tabs. Defaults to `false`. |
| `OnItemDropped` | `EventCallback<MudItemDropInfo<MudTabPanel>>` | – | When `EnableDragAndDrop` is set to true, this event will be raised when an item is dropped. The dropped item is provided in the `MudItemDropInfo{T}` and will have already been moved to its new position. |
| `KeepPanelsAlive` | `bool` | `false` | Persists the content of tabs when they are not visible. Defaults to `false`. When `false`, selecting a tab will initialize its content each time the tab is visited. When `true`, a tab's content is initialized only once and is hidden via `display:none`. |
| `LazyLoadPanels` | `bool` | `false` | Initializes tab panels only once visited. Only has an effect when `KeepPanelsAlive` is `true`. Defaults to `false`. When `false`, all tabs' contents are initialized immediately. When `true`, a tab's content is initialized only once it is visited. |
| `Disabled` | `bool` | `false` | Disables user interaction for all tab panels. Defaults to `false`. |
| `Rounded` | `bool` | `false` | Uses rounded corners on the tab's edges. Defaults to `false`. When `true`, the `border-radius` style is set to the theme's default value. |
| `Border` | `bool` | `false` | Shows a border between the tab content and tab header. Defaults to `false`. |
| `Outlined` | `bool` | `false` | Shows an outline around the tab header. Defaults to `false`. |
| `Centered` | `bool` | `false` | Centers tabs horizontally in the tab header. Defaults to `false`. |
| `HideSlider` | `bool` | `false` | Hides the slider underneath the tab header. Defaults to `false`. |
| `PrevIcon` | `string` | `Icons.Material.Filled.ChevronLeft` | The icon for scrolling to the previous page of tabs. Defaults to `ChevronLeft`. |
| `NextIcon` | `string` | `Icons.Material.Filled.ChevronRight` | The icon for scrolling to the next page of tabs. Defaults to `ChevronRight`. |
| `AlwaysShowScrollButtons` | `bool` | `false` | Shows the scroll buttons even if all tabs are visible. Defaults to `false`. |
| `MaxHeight` | `int?` | `null` | The maximum height for this component, in pixels. Defaults to `null`. |
| `MinimumTabWidth` | `string` | `"160px"` | The minimum width of each tab panel. Defaults to `160px`. Can be a CSS width or a percentage (e.g. `30%`). |
| `Position` | `Position` | `Position.Top` | The location of the tab header. Defaults to `Top`. |
| `Color` | `Color` | `Color.Default` | The color of the tab header. Defaults to `Default`. |
| `SliderColor` | `Color` | `Color.Inherit` | The color of the tab slider. Defaults to `Inherit`. |
| `IconColor` | `Color` | `Color.Inherit` | The color of each tab panel's icon. Defaults to `Inherit`. |
| `ScrollIconColor` | `Color` | `Color.Inherit` | The color of the scroll icon buttons. Defaults to `Inherit`. |
| `Elevation` | `int` | `0` | The size of the drop shadow. Defaults to `0`. Use a higher number for a larger drop shadow. |
| `ApplyEffectsToContainer` | `bool` | `false` | Applies the `Elevation`, `Rounded` and `Outlined` effects to the tab panel. Defaults to `false`. When `false`, effects are only applied to the header. When `true`, effects are applied to both the tab header and panel. |
| `Ripple` | `bool` | `true` | Shows a ripple effect when a tab is clicked. Defaults to `true`. |
| `SliderAnimation` | `bool` | `true` | Shows an animated line which slides to the selected tab. Defaults to `true`. |
| `ChildContent` | `RenderFragment?` | – | The content within this component. Typically a set of `MudTabPanel` components. |
| `PrePanelContent` | `RenderFragment<MudTabPanel>?` | – | This fragment is placed between tabHeader and panels. It can be used to display additional content like an address line in a browser. The active tab will be the content of this RenderFragement |
| `TabButtonsClass` | `string?` | `null` | The CSS classes applied to all tab buttons. Defaults to `null`. Multiple classes must be separated by spaces. |
| `TabHeaderClass` | `string?` | `null` | The CSS classes applied to the tab header. Defaults to `null`. Multiple classes must be separated by spaces. The "header" is the set of tab names which users click on to change the active tab. |
| `ActiveTabClass` | `string?` | `null` | The CSS classes applied to the currently selected tab. Defaults to `null`. Multiple classes must be separated by spaces. |
| `TabPanelsClass` | `string?` | `null` | The CSS classes applied to the element encasing the tab panels. Defaults to `null`. Multiple classes must be separated by spaces. |
| `ActivePanelIndex` | `int` | `0` (the first tab)` | The index of the currently selected tab panel. Defaults to `0` (the first tab). When this value changes, `ActivePanelIndexChanged` occurs. |
| `ActivePanelIndexChanged` | `EventCallback<int>` | – | Occurs when `ActivePanelIndex` has changed. |
| `Header` | `RenderFragment<MudTabs>?` | – | The custom content added before or after the list of tabs. The location of this header is controlled via the `HeaderPosition` parameter. |
| `HeaderPosition` | `TabHeaderPosition` | `TabHeaderPosition.After` | The location of custom header content provided in `Header`. Defaults to `After`. |
| `TabPanelHeader` | `RenderFragment<MudTabPanel>?` | – | Custom content added before or after each tab panel. The location of this header is controlled via the `TabPanelHeaderPosition` parameter. |
| `TabPanelHeaderPosition` | `TabHeaderPosition` | `TabHeaderPosition.After` | The location of custom tab panel content provided in `TabPanelHeader`. |
| `OnPreviewInteraction` | `Func<TabInteractionEventArgs, Task>?` | – | Occurs before a panel is activated. Set `Cancel` to `true` to prevent the tab from being activated. The returned `Task` will be awaited. |
| `SortDirection` | `SortDirection` | `SortDirection.None` | Sort tab labels lexicographically by `Text` or `SortKey`. Ignored if `SortComparer` is set. Defaults to `None`. |
| `SortComparer` | `IComparer<MudTabPanel>?` | `null` | Specify a custom Comparer to sort tabs. When set, `SortDirection` is not used. Defaults to `null`. |
