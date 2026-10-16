# DropZone components — API (generated from source)

## MudDragAndDropIndexChangedEventArgs : EventArgs

The information related to a `MudDropZone{T}` index change event.

_No own parameters — see base class `EventArgs`._

## MudDragAndDropItemTransaction<T>

The information related to a `MudDropZone{T}` drag-and-drop transaction.

_No own parameters._

## MudDragAndDropTransactionFinishedEventArgs<T> : EventArgs

The information related to a `MudDropZone{T}` completed drag-and-drop transaction.

_No own parameters — see base class `EventArgs`._

## MudDragHandle<T> : MudComponentBase

A drag handle that restricts drag-and-drop initiation to a specific child element inside a `MudDynamicDropItem{T}`.

*Place this component anywhere inside a `ItemRenderer`. Once registered, the parent item's full-element draggable behavior is suppressed so that only interactions with the handle element start a drag-and-drop transaction. Example — make only the card header draggable: <code lang="razor"> &lt;MudDropZone T="MyItem" ...&gt; &lt;ItemRenderer&gt; &lt;MudCard&gt; &lt;MudCardHeader&gt; &lt;MudDragHandle T="MyItem"&gt; &lt;MudIcon Icon="@Icons.Material.Filled.DragIndicator" /&gt; &lt;/MudDragHandle&gt; &lt;MudText&gt;@context.Title&lt;/MudText&gt; &lt;/MudCardHeader&gt; &lt;MudCardContent&gt;...&lt;/MudCardContent&gt; &lt;/MudCard&gt; &lt;/ItemRenderer&gt; &lt;/MudDropZone&gt; </code>*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content displayed inside the drag handle. |

## MudDropContainer<T> : MudComponentBase

A container of `MudDropZone{T}` components for drag-and-drop operations.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The content within this container. The content should include at least two `MudDropZone{T}` components. |
| `Items` | `IEnumerable<T>` | `Enumerable.Empty<T>()` | The items that can be dragged and dropped within this container. |
| `ItemRenderer` | `RenderFragment<T>?` | – | The template used to render items within a drop zone. |
| `ItemsSelector` | `Func<T, string, bool>?` | – | The function which determines whether an item is within a `MudDropZone{T}`. Can be overridden by child `MudDropZone{T}`'s with their owm implementation of `ItemsSelector` |
| `ItemDropped` | `EventCallback<MudItemDropInfo<T>>` | – | Occurs when an item has been dropped into a `MudDropZone{T}`. |
| `ItemPicked` | `EventCallback<MudDragAndDropItemTransaction<T>>` | – | Occurs when an item starts being dragged. A new `MudDragAndDropItemTransaction{T}` is started which tracks the drag-and-drop operation until it is completed or canceled. |
| `CanDrop` | `Func<T, string, bool>?` | – | The function which determines whether an item can be dropped within a drop zone. When a drop zone is allowed, the `CanDropClass` is applied, otherwise `NoDropClass` is applied. |
| `CanDropClass` | `string?` | – | The CSS classes applied to valid drop zones. This class is applied when `CanDrop` returns `true` for an item. Multiple classes must be separated by spaces. |
| `NoDropClass` | `string?` | – | The CSS classes applied to invalid drop zones. This class is applied when `CanDrop` returns `false` for an item. Multiple classes must be separated by spaces. |
| `ApplyDropClassesOnDragStarted` | `bool` | `false` | Applies either `CanDropClass` or `NoDropClass` to drop zones during a drag-and-drop transaction. Defaults to `false`. The `CanDrop` function determines which classes are applied. |
| `ItemDisabled` | `Func<T, bool>?` | – | The function which determines whether an item cannot be dragged. If no value is given, all items can be dragged by default. When an item is disabled, the `DisabledClass` is applied. |
| `DisabledClass` | `string` | `"disabled"` | The CSS classes applied to disabled drop items. This class is applied when `ItemDisabled` returns `true` for an item. Multiple classes must be separated by spaces. |
| `DraggingClass` | `string?` | – | The CSS classes applied to drop zones during a drag-and-drop operation. Multiple classes must be separated by spaces. |
| `ItemDraggingClass` | `string?` | – | The CSS classes applied to items during a drag-and-drop operation. Multiple classes must be separated by spaces. |
| `ItemsClassSelector` | `Func<T, string, string>?` | – | The function which determines the CSS classes for each item. |

## MudDropZone<T> : MudComponentBase

A location which can participate in a drag-and-drop operation.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | – | The custom content within this drop zone. |
| `Identifier` | `string` | `string.Empty` | The unique identifier for this drop zone. Drag-and-drop zones each have a unique identifier to differentiate them during drag-and-drop operations. |
| `ItemRenderer` | `RenderFragment<T>?` | – | The template used to render items within this drop zone. When set, overrides the `ItemRenderer`. |
| `ItemsSelector` | `Func<T, bool>?` | – | The function which determines whether an item is within this `MudDropZone{T}` . When set, overrides the `ItemsSelector` function. |
| `CanDrop` | `Func<T, bool>?` | – | The function which determines whether an item can be dropped within a drop zone. When a drop zone is allowed, the `CanDropClass` is applied, otherwise `NoDropClass` is applied. When set, overrides `CanDrop`. |
| `CanDropClass` | `string?` | – | The CSS classes applied to valid drop zones. This class is applied when `CanDrop` returns `true` for an item. Multiple classes must be separated by spaces. When set, overrides `CanDropClass`. |
| `NoDropClass` | `string?` | – | The CSS classes applied to invalid drop zones. This class is applied when `CanDrop` returns `false` for an item. Multiple classes must be separated by spaces. When set, overrides `NoDropClass`. |
| `ApplyDropClassesOnDragStarted` | `bool?` | `false` | Applies either `CanDropClass` or `NoDropClass` to drop zones during a drag-and-drop transaction. Defaults to `false`. The `CanDrop` function determines which classes are applied. When set, overrides `ApplyDropClassesOnDragStarted`. |
| `ItemDisabled` | `Func<T, bool>?` | – | The function which determines whether an item cannot be dragged. If no value is given, all items can be dragged by default. When an item is disabled, the `DisabledClass` is applied. When set, overrides `ItemDisabled`. |
| `DisabledClass` | `string?` | – | The CSS classes applied to disabled drop items. This class is applied when `ItemDisabled` returns `true` for an item. Multiple classes must be separated by spaces. When set, overrides `DisabledClass`. |
| `DraggingClass` | `string?` | – | The CSS classes applied to drop zones during a drag-and-drop operation. Multiple classes must be separated by spaces. When set, overrides `DraggingClass`. |
| `ItemDraggingClass` | `string?` | – | The CSS classes applied to items during a drag-and-drop operation. Multiple classes must be separated by spaces. When set, overrides `ItemDraggingClass`. |
| `ItemsClassSelector` | `Func<T, string>?` | – | The function which determines the CSS classes for each item. When set, overrides `ItemsClassSelector`. |
| `AllowReorder` | `bool` | `false` | Allows items to be reordered within a zone. Defaults to `false`. |
| `OnlyZone` | `bool` | `false` | Allows this zone to only receive dropped items. Defaults to `false`. |

## MudDynamicDropItem<T> : MudComponentBase

Wraps a single item inside a `MudDropZone{T}` so it can be dragged and dropped between zones using mouse or touch gestures.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ZoneIdentifier` | `string?` | – | The zone identifier of the corresponding drop zone |
| `Item` | `T?` | – | the data item that is represented by this item |
| `ChildContent` | `RenderFragment?` | – | Child content of component |
| `DraggingClass` | `string?` | – | An additional class that is applied to this element when a drag operation is in progress |
| `OnDragStarted` | `EventCallback<T>` | – | An event callback set fires, when a drag operation has been started |
| `OnDragEnded` | `EventCallback<T>` | – | An event callback set fires, when a drag operation has been ended. This included also a canceled transaction |
| `Disabled` | `bool` | `false` | When true, the item can't be dragged. defaults to false |
| `DisabledClass` | `string?` | – | The class that is applied when disabled `Disabled` is set to true |
| `Index` | `int` | `-1` | The index of this item within its drop zone. |
| `HideContent` | `bool` | – | Hides this item's content. |
