# Pagination components — API (generated from source)

## MudPagination : MudComponentBase

A list of clickable page numbers along with navigation buttons.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Count` | `int` | `1` | The total number of pages. |
| `BoundaryCount` | `int` | `2` | The number of pages shown before and after the ellipsis. Defaults to `2`. A value of `0` would hide the page numbers at the edge: `&lt; ... 4 5 6 ... &gt;` A value of `1` would show one-page number at the edge: `&lt; 1 ... 4 5 6 ... 9 &gt;` A value of `2` would show two-page numbers at the edge: `&lt; 1 2 ... 4 5 6 ... 8 9 &gt;` |
| `MiddleCount` | `int` | `3` | The number of pages shown between the ellipsis. Defaults to `3`. A value of `1` would show one-page number in the middle: `&lt; 1 ... 5 ... 9 &gt;` A value of `3` would show three-page numbers in the middle: `&lt; 1 ... 4 5 6 ... 9 &gt;` |
| `Selected` | `int` | `1` | The selected page number. |
| `Variant` | `Variant` | `Variant.Text` | The display variant to use. Defaults to `Text`. |
| `Color` | `Color` | `Color.Primary` | The color of the selected page button. Defaults to `Primary`. |
| `Rectangular` | `bool` | `false` | Shows rectangular-shaped page buttons. Defaults to `false`. |
| `Size` | `Size` | `Size.Medium` | The size of the page buttons. Defaults to `Medium`. |
| `DropShadow` | `bool` | `true` | Shows a drop shadow under each page button. Defaults to `true`. |
| `Disabled` | `bool` | `false` | Prevents the user from clicking page buttons. Defaults to `false`. |
| `ShowFirstButton` | `bool` | `false` | Shows the button which selects the first page. Defaults to `false`. |
| `ShowLastButton` | `bool` | `false` | Shows the button which selects the last page. Defaults to `false`. |
| `ShowPreviousButton` | `bool` | `true` | Shows the button which selects the previous page. Defaults to `true`. |
| `ShowNextButton` | `bool` | `true` | Shows the button which selects the next page. Defaults to `true`. |
| `ShowPageButtons` | `bool` | `true` | Shows numeric buttons for pages. |
| `ControlButtonClicked` | `EventCallback<Page>` | – | Occurs when the First, Previous, Next, or Last button is clicked. |
| `SelectedChanged` | `EventCallback<int>` | – | Occurs when `Selected` has changed. |
| `FirstIcon` | `string` | `Icons.Material.Filled.FirstPage` | The icon for the First button. Defaults to `FirstPage`. Only shows if `ShowFirstButton` is `true`. |
| `BeforeIcon` | `string` | `Icons.Material.Filled.NavigateBefore` | The icon for the Before button. Defaults to `NavigateBefore`. Only shows if `ShowPreviousButton` is `true`. |
| `NextIcon` | `string` | `Icons.Material.Filled.NavigateNext` | The icon for the Next button. Defaults to `NavigateNext`. Only shows if `ShowNextButton` is `true`. |
| `LastIcon` | `string` | `Icons.Material.Filled.LastPage` | The icon for the Last button. Defaults to `LastPage`. Only shows if `ShowLastButton` is `true`. |
