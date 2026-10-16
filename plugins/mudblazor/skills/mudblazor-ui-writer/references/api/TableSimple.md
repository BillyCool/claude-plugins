# TableSimple components — API (generated from source)

## MudSimpleTable : MudComponentBase

A table similar to `MudTable{T}` but with basic styling features.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Elevation` | `int` | `1` | The size of the drop shadow. Defaults to `1`. A higher number creates a heavier drop shadow. Use a value of `0` for no shadow. |
| `Hover` | `bool` | `false` | Highlights rows when hovering over them. Defaults to `false`. |
| `Square` | `bool` | `false` | Uses square corners for the table. Defaults to `false`. |
| `Dense` | `bool` | `false` | Uses compact padding for all rows. Defaults to `false`. |
| `Outlined` | `bool` | `false` | Shows borders around the table. Defaults to `false`. |
| `Bordered` | `bool` | `false` | Shows left and right borders for each table cell. Defaults to `false`. |
| `Striped` | `bool` | `false` | Uses alternating colors for table rows. Defaults to `false`. |
| `FixedHeader` | `bool` | `false` | Fixes the table header in place while the table is scrolled. Defaults to `false`. When `true`, the CSS `Height` must also be set. Example: `Style="height:300px;"` |
| `ChildContent` | `RenderFragment?` | – | The content within this table. Use table HTML tags such as `&lt;thead&gt;`, `&lt;tbody&gt;`, `&lt;tr&gt;`, `&lt;th&gt;` or `&lt;td&gt;`. |
