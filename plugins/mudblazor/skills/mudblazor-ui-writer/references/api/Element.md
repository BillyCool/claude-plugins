# Element components — API (generated from source)

## MudElement : MudComponentBase

A primitive component which allows dynamically changing the HTML element rendered under the hood.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this element. |
| `HtmlTag` | `string` | `"span"` | The HTML tag rendered for this element. Defaults to `span`. |
| `Ref` | `ElementReference?` | – | The `ElementReference` to bind to. This is typically bound via `@bind-Ref="myRef"`. When this property changes, the `RefChanged` event occurs. |
| `RefChanged` | `EventCallback<ElementReference>` | – | Occurs when `Ref` has changed. |
| `ClickPropagation` | `bool` | `true` | Propagates click events beyond this element. Defaults to `true`. |
| `PreventDefault` | `bool` | `false`, allowing default actions` | Prevents the default action when this element is clicked. Defaults to `false`, allowing default actions. |
