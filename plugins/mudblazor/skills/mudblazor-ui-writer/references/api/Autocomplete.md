# Autocomplete components — API (generated from source)

## MudAutocomplete<T> : MudBaseInput<T>

A text input for searching and selecting from a list of options. Unlike `MudSelect{T}`, it doesn't require the complete item list upfront and supports asynchronous search for database queries.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `InputClass` | `string?` | – | Input's classnames, separated by space. |
| `PopoverClass` | `string?` | `null` | The CSS classes applied to the popover. Defaults to `null`. You can use spaces to separate multiple classes. |
| `ListClass` | `string?` | `null` | The CSS classes applied to the internal list. Defaults to `null`. You can use spaces to separate multiple classes. |
| `ListItemClass` | `string?` | `null` | The CSS classes applied to internal list items. Defaults to `null`. You can use spaces to separate multiple classes. |
| `AnchorOrigin` | `Origin` | `Origin.BottomLeft` | The location where the popover will open from. Defaults to `BottomLeft`. |
| `TransformOrigin` | `Origin` | `Origin.TopLeft` | The transform origin point for the popover. Defaults to `TopLeft`. |
| `Dense` | `bool` | `false` | Uses compact padding. Defaults to `false`. |
| `OpenIcon` | `string` | `Icons.Material.Filled.ArrowDropDown` | The "open" Autocomplete icon. Defaults to `ArrowDropDown`. |
| `CloseIcon` | `string` | `Icons.Material.Filled.ArrowDropUp` | The "close" Autocomplete icon. Defaults to `ArrowDropDown`. |
| `MaxHeight` | `int` | `300` | The maximum height, in pixels, of the Autocomplete when it is open. Defaults to `300`. |
| `ToStringFunc` | `Func<T?, string?>?` | `the `ToString()` method of items` | The function used to get the display text for each item. Defaults to the `ToString()` method of items. |
| `ShowProgressIndicator` | `bool` | `false` | Shows the progress indicator during searches. Defaults to `false`. The progress indicator uses the color specified in the `ProgressIndicatorColor` property. |
| `ProgressIndicatorColor` | `Color` | `Color.Default` | The color of the progress indicator. Defaults to `Default`. This property is used when `ShowProgressIndicator` is `true`. |
| `SearchFunc` | `Func<string?, CancellationToken, Task<IEnumerable<T>>?>?` | – | The function used to search for items. This function searches for items containing the specified `string` value, and returns items which match up to the `MaxItems` property. You can use the provided `CancellationToken` which is marked as canceled when the user changes the search text or selects a value from the list. |
| `MaxItems` | `int?` | `10` | The maximum number of items to display. Defaults to `10`. A value of `null` will display all items. |
| `MinCharacters` | `int` | `0` | The minimum number of characters typed to initiate a search. Defaults to `0`. |
| `ResetValueOnEmptyText` | `bool` | `false` | Reset the selected value if the user deletes the text. Defaults to `false`. |
| `SelectOnActivation` | `bool` | `true` | Highlights the text when the component receives focus. Defaults to `true`. Previously known as `SelectOnClick`. |
| `Strict` | `bool` | `true` | Selects items without resetting the `Value`. Defaults to `true`. When `true`, selecting an option will trigger a `SearchFunc` with the current Text. Otherwise, an empty string is passed which can make it easier to view and select other options without resetting the Value. When `false`, `T` must either be a `record` or override the `GetHashCode` and `Equals` methods. |
| `DebounceInterval` | `int` | `100` | The debounce interval, in milliseconds. Defaults to `100`. A higher value can help reduce the number of calls to `SearchFunc`, which can improve responsiveness. |
| `OnDebounceIntervalElapsed` | `EventCallback<string>` | – | Occurs when the `DebounceInterval` has elapsed. The current value of `Text` is included in this event. |
| `ItemTemplate` | `RenderFragment<T>?` | `null` | The custom template used to display unselected items. Defaults to `null`. Use the `ItemSelectedTemplate` property to control the display of selected items. |
| `ItemSelectedTemplate` | `RenderFragment<T>?` | `null` | The custom template used to display selected items. Defaults to `null`. Use the `ItemTemplate` property to control the display of unselected items. |
| `ItemDisabledTemplate` | `RenderFragment<T>?` | `null` | The custom template used to display disabled items. Defaults to `null`. |
| `MoreItemsTemplate` | `RenderFragment?` | `null` | The custom template used when the number of items returned by `SearchFunc` is more than the value of the `MaxItems` property. Defaults to `null`. |
| `NoItemsTemplate` | `RenderFragment?` | `null` | The custom template used when no items are returned by `SearchFunc`. Defaults to `null`. |
| `BeforeItemsTemplate` | `RenderFragment?` | `null` | The custom template shown above the list of items, if `SearchFunc` returns items to display. Otherwise, the fragment is hidden. Defaults to `null`. Use the `AfterItemsTemplate` property to control content displayed below items. |
| `AfterItemsTemplate` | `RenderFragment?` | `null` | The custom template shown below the list of items, if `SearchFunc` returns items to display. Otherwise, the fragment is hidden. Defaults to `null`. Use the `BeforeItemsTemplate` property to control content displayed above items. |
| `ProgressIndicatorTemplate` | `RenderFragment?` | `null` | The custom template used for the progress indicator when `ShowProgressIndicator` is `true`. Defaults to `null`. Use the `ProgressIndicatorInPopoverTemplate` property to control content displayed for the progress indicator inside the popover. |
| `ProgressIndicatorInPopoverTemplate` | `RenderFragment?` | `null` | The custom template used for the progress indicator inside the popover when `ShowProgressIndicator` is `true`. Defaults to `null`. Use the `ProgressIndicatorTemplate` property to control content displayed for the progress indicator. |
| `Modal` | `bool?` | `ModalOverlay` | Prevents interaction with background elements while this list is open. Defaults to `ModalOverlay`. |
| `RelativeWidth` | `DropdownWidth` | `DropdownWidth.Relative` | Determines the width of this Popover dropdown in relation to the parent container. Defaults to `Relative`. When `Relative`, restricts the max-width of the component to the width of the parent container When `Adaptive`, restricts the min-width of the component to the width of the parent container |
| `CoerceText` | `bool` | `true` | Overrides the `Text` property when an item is selected. Defaults to `true`. When `true`, selecting a value will update the Text property. When `false`, incomplete values for Text are allowed. |
| `CoerceValue` | `bool` | `false` | Sets the `Value` property even if no match is found by `SearchFunc`. Defaults to `false`. When `true`, the user input will be applied to the Value property which allows it to be validated and show an error message. |
| `PopoverFixed` | `bool` | `false` | Displays the dropdown popover in a fixed position, even while scrolling. Defaults to `false`. |
| `ItemDisabledFunc` | `Func<T, bool>?` | `null` | The function used to determine if an item should be disabled. Defaults to `null`. |
| `OpenChanged` | `EventCallback<bool>` | – | Occurs when the `Open` property has changed. |
| `SelectValueOnTab` | `bool` | `false` | Updates the Value to the currently selected item when pressing the Tab key. Defaults to `false`. |
| `OpenOnFocus` | `bool` | `true` | Additionally, opens the list when focus is received on the input element; otherwise only opens on click. Defaults to `true`. |
| `Clearable` | `bool` | `false` | Displays the Clear icon button. Defaults to `false`. When `true`, an icon is displayed which, when clicked, clears the Text and Value. Use the `ClearIcon` property to control the Clear button icon. |
| `ClearIcon` | `string` | `Icons.Material.Filled.Clear` | Custom clear icon when `Clearable` is enabled. |
| `OnClearButtonClick` | `EventCallback<MouseEventArgs>` | – | Occurs when the Clear button has been clicked. The Text and Value properties will be blank when this callback occurs. |
| `ReturnedItemsCountChanged` | `EventCallback<int>` | – | Occurs when the number of items returned by `SearchFunc` has changed. The number of items returned determines when custom templates are shown. If the number is `0`, `NoItemsTemplate` will be shown. If the number is beyond `MaxItems`, `MoreItemsTemplate` will be shown. |
| `LockScroll` | `bool` | `false` | Prevents scrolling while the dropdown is open. Defaults to `false`. |
