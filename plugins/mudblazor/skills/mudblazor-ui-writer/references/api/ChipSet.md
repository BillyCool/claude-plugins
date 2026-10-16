# ChipSet components — API (generated from source)

## MudChipSet<T> : MudComponentBase

A collection of multiple `MudChip{T}` components that allows single or multi-selection.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this chipset. |
| `SelectionMode` | `SelectionMode` | `SelectionMode.SingleSelection` | The mode controlling how many selections are allowed. Defaults to `SingleSelection`. Other values include `MultiSelection` and `ToggleSelection`. |
| `AllClosable` | `bool` | `false` | Allows all chips in this set to be closed. Defaults to `false`. |
| `Variant` | `Variant` | `Variant.Filled` | The default variant for all chips in this set. Defaults to `Filled`. Can be overridden by setting `Variant`. |
| `Color` | `Color` | `Color.Default` | The default color for all chips in this set. Defaults to `Default`. Can be overridden by setting `Color`. |
| `SelectedColor` | `Color` | `Color.Inherit` | The default color for all selected chips in this set. Defaults to `Inherit`. Can be overridden by setting `SelectedColor`. |
| `IconColor` | `Color` | `Color.Inherit` | The default icon color for all chips in this set. Defaults to `Inherit`. Can be overridden by setting `IconColor`. |
| `Size` | `Size` | `Size.Medium` | The default size for all chips in this set. Defaults to `Medium`. Can be overridden by setting `Size`. |
| `CheckMark` | `bool` | – | Shows checkmarks for selected chips. |
| `CheckedIcon` | `string` | `Icons.Material.Filled.Check` | The default icon shown for selected chips in this set. Defaults to `Check`. Can be overridden by setting `CheckedIcon`. |
| `CloseIcon` | `string` | `Icons.Material.Filled.Cancel` | The default close icon shown for closeable chips in this set. Defaults to `Cancel`. Can be overridden by setting `CloseIcon`. |
| `Ripple` | `bool` | `true` | Shows a ripple effect when a chip is clicked. Defaults to `true`. Can be overridden by setting `Ripple`. |
| `Label` | `bool` | `false` | Uses the theme border radius for chips in this set. Defaults to `false`. When `true`, the `DefaultBorderRadius` is used for chip edges. Can be overridden by setting `Label`. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with chips in this set. Defaults to `false`. When `true`, the all chips are visibly disabled and interaction is not allowed. Overrides any value set for `Disabled`. |
| `ReadOnly` | `bool` | `false` | Prevents chips in this set from being clicked. Defaults to `false`. When `true`, chips cannot be clicked even if `OnClick` is set. |
| `Comparer` | `IEqualityComparer<T?>` | `EqualityComparer<T?>.Default` | The comparer used to determine when a selection has changed. Defaults to `Default`. |
| `SelectedValue` | `T?` | – | The currently selected value. This property is used when `SelectionMode` is `SingleSelection` or `ToggleSelection`. |
| `SelectedValueChanged` | `EventCallback<T?>` | – | Occurs when `SelectedValue` has changed. This property is used when `SelectionMode` is `SingleSelection` or `ToggleSelection`. |
| `SelectedValues` | `IReadOnlyCollection<T>?` | – | The currently selected chips in this set. This event occurs when `SelectionMode` is `MultiSelection`. |
| `SelectedValuesChanged` | `EventCallback<IReadOnlyCollection<T>?>` | – | Occurs when `SelectedValues` has changed. This event occurs when `SelectionMode` is `MultiSelection`. |
| `OnClose` | `EventCallback<MudChip<T>>` | – | Occurs when any chip has been closed. |
