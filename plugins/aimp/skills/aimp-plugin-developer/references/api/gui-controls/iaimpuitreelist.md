# IAIMPUITreeList

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUITreeList

## Properties

### AIMPUI_TL_PROPID_ALLOW_DELETING

Allows to user delete nodes.
0 - disallow.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_ALLOW_EDITING

Allows to user in-place editing.
0 - disallow.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_ALLOW_FOCUS_CELLS

Allows to user focus cell.
0 - disallow, in this case entire row will be focused.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_ALLOW_MULTISELECT

Enables multi selection.
0 - disabled, if this case user can select only one node.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_ALLOW_REORDER_COLUMNS

Allows to user reorder the columns.
0 - disallow.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_ALLOW_SHOWWHIDE_COLUMNS

Allows to user change visibility of the columns
0 - disallow.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_AUTOCHECK_SUBNODES

Enables mode when state of parent check mark is depended from children check marks.
0 - switched off.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_BORDERS

0 or combination of following flags:
`+ AIMPUI_FLAGS_BORDER_LEFT
+ AIMPUI_FLAGS_BORDER_TOP
+ AIMPUI_FLAGS_BORDER_RIGHT
+ AIMPUI_FLAGS_BORDER_BOTTOM`

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_CELL_HINTS

Enables hints for the cells values.
0 - switched off.

Default value: 1

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_CHECKBOXES

Enables check boxes for nodes, groups and columns
0 - switched off.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_COLUMN_AUTOWIDTH

Enables auto width mode for columns. Width of columns calculates automatically to prevent from showing of horizontal scroll bar.
0 - switched off.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_COLUMN_HEIGHT

Height of column bar in pixels.
Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

Default value: 0 (auto height)

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_COLUMN_IMAGES

Images for columns

- **Type:** IAIMPUIImageList
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPUIImageList, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPUIImageList>)

### AIMPUI_TL_PROPID_COLUMN_VISIBLE

Column bar visibility.
0 - hidden.

Default value: 1

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_DRAG_SORTING

Allows custom sorting to user via drag-n-drop.
0 - switched off.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_DRAG_SORTING_CHANGE_LEVEL

Is used only if `AIMPUI_TL_PROPID_DRAG_SORTING` = 1
Enables an ability to change level of node via drag-n-drop.
0 - switched off.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_GRID_LINES

0 or combination of following flags:

`AIMPUI_FLAGS_TL_GRIDLINE_VERTICAL
AIMPUI_FLAGS_TL_GRIDLINE_HORIZONTAL`

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_GROUP_HEIGHT

Group height.
Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

Default value: 0 (auto height)

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_GROUPS

Enables grouping mode. Groups are creates for top-level nodes only.
0 - switched off.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_GROUPS_ALLOW_COLLAPSE

Enables an ability to collapse groups.
0 - switched off.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_GROUPS_FOCUS_ON_CLICK

Allows to groups get focus on mouse click.
0 - no, in this case click will focus a first row in the group

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_HOT_TRACK

Highlight the row that is under mouse cursor.
0 - hot track is switched off.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_INCSEARCH_COLUMN_INDEX

Absolute index of column for incremental search.
-1 - incremental search is switched off.

Default value: -1

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_NODE_HEIGHT

Height of node row.
Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

Default value: 0 (auto height)

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_NODE_IMAGE_ALIGNMENT

Alignment for node image in first cell of row.
0 - align left
1 - align right
2 - center

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_TL_PROPID_NODE_IMAGES

Images for nodes

- **Type:** IAIMPUIImageList
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPUIImageList, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPUIImageList>)

### AIMPUI_TL_PROPID_SORTING_MODE

Sorting mode:
0 - sorting by columns is switched off
1 - sorting by single column is available
2 - sorting by multiple columns is available

Default value: 2

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

## Methods: Columns

### AddColumn

- `in` **IID** — `TGUID`
  IID_IAIMPUITreeListColumn
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### ClearColumns

Removes all columns

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetColumn

- `in` **IID** — `TGUID`
  IID_IAIMPUITreeListColumn
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetColumnCount

- `out` **Result** — `Integer`

## Methods: Nodes

### Clear

Removes all nodes

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Delete

- `in` **Node** — `IAIMPUITreeListNode`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetPath

Returns path to node: <Name of parent node>\<Name of parent node>\<Name of node>\

- `in` **Node** — `IAIMPUITreeListNode`
- `out` **Path** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### SetPath

Focus the node via specified path. If node was not found - last node that contains part of path will focused.

- `in` **Node** — `IAIMPUITreeListNode`
- `in` **Path** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetRootNode

Returns interface for root node.

- `in` **IID** — `TGUID`
  IID_IAIMPUITreeListNode
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### MakeTop

Scroll the content to make the Node first visible (if it possible)

- `in` **Node** — `IAIMPUITreeListNode`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### MakeVisible

Scroll the content to make the Node visible

- `in` **Node** — `IAIMPUITreeListNode`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

## Methods: Node List

### GetAbsoluteVisibleNode

- `in` **Index** — `Integer`
- `out` **IID** — `TGUID`
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetAbsoluteVisibleNodeCount

- `out` **Result** — `Integer`

## Methods: Selected Nodes

### DeleteSelected

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### SelectAll

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### SelectNone

Clear Selection

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetFocused

Returns focused object. Object can be a Node, Group or Column.

- `out` **IID** — `TGUID`
  IID_IAIMPUITreeListColumn,
  IID_IAIMPUITreeListGroup,
  IID_IAIMPUITreeListNode
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### SetFocused

Set focus to object. Object can be a Node, Group or Column.

- `in` **Obj** — `IUnknown`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetSelected

- `in` **Index** — `Integer`
- `out` **IID** — `TGUID`
  IID_IAIMPUITreeListNode
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetSelectedCount

- `out` **Result** — `Integer`

## Methods: In-place editing

### GetEditingCell

Returns position of editing cell.
Method will returns an error if nothing is editing now.

- `out` **ColumnIndex** — `Integer`
- `out` **RowIndex** — `Integer`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### StartEditing

Starting editing for specified cell.
Editing must be enabled - refer to the `AIMPUI_TL_PROPID_ALLOW_EDITING` property.

- `in` **Column** — `IAIMPUITreeListColumn`
  Can be `nil/null`, in this case focused cell will be edited.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### StopEditing

Cancel editing

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

## Methods: Groups

### GroupBy

Group the list by specified column

- `in` **Column** — `IAIMPUITreeListColumn`
- `in` **ResetPrevGroupingParams** — `BOOL`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetGroup

- `in` **Index** — `Integer`
- `out` **IID** — `TGUID`
  IID_IAIMPUITreeListGroup
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### GetGroupCount

- `out` **Result** — `Integer`

### Regroup

Force regroup the list by previous used parameters

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### ResetGrouppingParams

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

## Methods: Sorting

### SortBy

Sort the list by specified column

- `in` **Column** — `IAIMPUITreeListColumn`
- `in` **Flags** — `DWORD`
  `AIMPUI_FLAGS_TL_SORTBY_FLAG_AUTO`
  `AIMPUI_FLAGS_TL_SORTBY_FLAG_ASCENDING`
  `AIMPUI_FLAGS_TL_SORTBY_FLAG_DESCENDING`
- `in` **ResetPrevSortingParams** — `BOOL`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Resort

Force resort the list by previous used parameters

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### ResetSortingParams

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

## Methods: Settings

### ConfigLoad / ConfigSave

This functions allows to load / save parameters that can be customized by end user during work session.

- `in` **Config** — `IAIMPConfig`
- `in` **Key** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

## Creating the instance

Instance must be created via the <IAIMPServiceUI>.CreateControl method.

Control is top-aligned at parent control by default, to change it placement use the `SetPlacement` method.

Control will be destroyed automatically with IAIMPUIForm that contains the control.

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## Events

### Events

- IAIMPUITreeListCustomDrawEvents
- IAIMPUITreeListDeleteEvents
- IAIMPUITreeListDragSortingEvents
- IAIMPUITreeListInplaceEditingEvents
- IAIMPUITreeListEvents

### IAIMPUITreeListCustomDrawEvents

#### Description

IAIMPUITreeListCustomDrawEvents provides an ability to override drawing for Node or Cell.

#### Methods

##### OnCustomDrawNode

Event occurs when node row is drawing

- `in` **Sender** — `IAIMPUITreeList`
- `in` **DC** — `HCANVAS`
  Handle of device context
- `in` **R** — `TRect`
  Row bounds
- `in` **Node** — `IAIMPUITreeListNode`
- `var` **Handled** — `LongBool`
  Set this parameter to True to suppress default drawing handler.
  Note that in this case the OnCustomDrawNodeCell event will not be called.

##### OnCustomDrawNodeCell

Event occurs when node cell is drawing

- `in` **Sender** — `IAIMPUITreeList`
- `in` **DC** — `HCANVAS`
  Handle of device context
- `in` **R** — `TRect`
  Cell bounds
- `in` **Node** — `IAIMPUITreeListNode`
- `in` **Column** — `IAIMPUITreeListColumn`
- `var` **Handled** — `LongBool`
  Set this parameter to True to suppress default drawing handler.

##### OnGetNodeBackground

Event provides an ability to change background color for node row

- `in` **Sender** — `IAIMPUITreeList`
- `in` **Node** — `IAIMPUITreeListNode`
- `var` **Color** — `DWORD`
  RRGGBB

### IAIMPUITreeListDeleteEvents

#### Description

Events from the IAIMPUITreeListDeleteEvents group occurs when user attempt to delete selected items from the list.

#### Methods

##### OnDeleteSelected

- `in` **Sender** — `IAIMPUITreeList`
- `var` **Allow** — `LongBool`
  Set this parameter to True to allow deletion.

#### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000

### IAIMPUITreeListDragSortingEvents

#### Description

Events from the IAIMPUITreeListDragSortingEvents group occurs after manual sorting the nodes (if this feature is enabled).

#### Methods

##### OnDragSorting

Event occurs after manual sorting the nodes via drag-n-drop.

- `in` **Sender** — `IAIMPUITreeList`

##### OnDragSortingNodeOver

Event occurs when trying to move selected nodes to specified position.

- `in` **Sender** — `IAIMPUITreeList`
- `in` **Node** — `IAIMPUITreeListNode`
  Target node
- `in` **Flags** — `DWORD`
  Insertion mode to the target node.

  One of following flags:
  `AIMPUI_FLAGS_TL_INSERTTO_AFTER
  AIMPUI_FLAGS_TL_INSERTTO_BEFORE
  AIMPUI_FLAGS_TL_INSERTTO_INTO`
- `var` **Allow** — `LongBool`
  Set this parameter to True if moving is allowed to specified position.

### IAIMPUITreeListInplaceEditingEvents

#### Description

Events from the IAIMPUITreeListInplaceEditingEvents group occurs when editing the cell value (if this feature is enabled)

#### Methods

##### OnEditing

Event occurs when user starting the editing

- `in` **Sender** — `IAIMPUITreeList`
- `in` **Node** — `IAIMPUITreeListNode`
- `in` **ColumnIndex** — `Integer`
  Absolute column index.
- `var` **Allow** — `LongBool`
  Set this parameter to True if editing is allowed for that cell.

##### OnEdited

Event occurs when user finishing the editing

- `in` **Sender** — `IAIMPUITreeList`
- `in` **Node** — `IAIMPUITreeListNode`
- `in` **ColumnIndex** — `Integer`
  Absolute column index.
- `var` **Value** — `IAIMPString`
  Entered value

### IAIMPUITreeListEvents

#### Methods

##### OnColumnClick

- `in` **Sender** — `IAIMPUITreeList`
- `in` **ColumnIndex** — `Integer`
  Absolute column index

##### OnFocusedColumnChanged

Event occurs when focus moved from one cell to another

- `in` **Sender** — `IAIMPUITreeList`

##### OnFocusedNodeChanged

Event occurs when focus moved from one node to another

- `in` **Sender** — `IAIMPUITreeList`

##### OnNodeChecked

- `in` **Sender** — `IAIMPUITreeList`
- `in` **Node** — `IAIMPUITreeListNode`

##### OnNodeDblClicked

- `in` **Sender** — `IAIMPUITreeList`
- `in` **Node** — `IAIMPUITreeListNode`

##### OnSelectionChanged

- `in` **Sender** — `IAIMPUITreeList`

##### OnSorted

- `in` **Sender** — `IAIMPUITreeList`

##### OnStructChanged

Event occurs when control recalculates

- `in` **Sender** — `IAIMPUITreeList`

## IAIMPUITreeListColumn

### Parent

IAIMPPropertyList — IAIMPUITreeListColumn

### Properties

#### AIMPUI_TL_COLUMN_PROPID_CAN_RESIZE

Default value: 1

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_COLUMN_PROPID_CAPTION

Refer to the automatic localization

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMPUI_TL_COLUMN_PROPID_DRAWINDEX

Drawing index, begins from 0
If column is hidden - index will be set to -1.
By default index is same to value of the AIMPUI_TL_COLUMN_PROPID_INDEX property.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_COLUMN_PROPID_IMAGEINDEX

Index of image to draw in the IAIMPUIImageList

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_COLUMN_PROPID_INDEX

Absolute index of column

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_COLUMN_PROPID_TEXT_ALIGNMENT

Horizontal text alignment. One of the following values:

- `AIMPUI_ALIGN_NEAR` - (left) (default)
- `AIMPUI_ALIGN_CENTER`
- `AIMPUI_ALIGN_FAR` - (right)

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_COLUMN_PROPID_TEXT_VISIBLE

Default value: 1

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_COLUMN_PROPID_VISIBLE

Default value: 1

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_COLUMN_PROPID_WIDTH

Width of column in pixels, can be changed by end user if the `AIMPUI_TL_COLUMN_PROPID_CAN_RESIZE` property is different from 0.
Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

Default value: 100

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

## IAIMPUITreeListGroup

### Parent

IAIMPPropertyList — IAIMPUITreeListGroup

### Properties

#### AIMPUI_TL_GROUP_PROPID_CAPTION

Group caption, generates automatically.

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(.., IID_IAIMPString, ..)

#### AIMPUI_TL_GROUP_PROPID_CHECKSTATE

State of check mark, calculates automatically based on check marks states of children elements.
Can be one of following values:
- `AIMPUI_CHECKSTATE_UNCHECKED`
- `AIMPUI_CHECKSTATE_CHECKED`
- `AIMPUI_CHECKSTATE_MIXED`

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_GROUP_PROPID_EXPANDED

0 - collapsed, otherwise - expanded.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_GROUP_PROPID_INDEX

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

#### AIMPUI_TL_GROUP_PROPID_SELECTED

0 - group is not selected.

Group selected if all children are selected.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### Methods

#### Get

An access to children elements - IAIMPUITreeListNode

- `in` **Index** — `Integer`
- `in` **IID** — `TGUID`
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetCount

- `out` **Result** — `Integer`

## IAIMPUITreeListNode

### Parent

IAIMPPropertyList — IAIMPUITreeListNode

### Properties

#### AIMPUI_TL_NODE_PROPID_ABS_VISIBLE_INDEX

Visible index among the list of visible nodes without hierarchy

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

#### AIMPUI_TL_NODE_PROPID_CHECK_ENABLED

Property provides an ability to disallow end user to modify check mark state.
0 - disallow.

Default Value: 1

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_NODE_PROPID_CHECKED

State of check mark: 0 - unchecked, 1 - checked.

Default value: 0

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_NODE_PROPID_CHILDREN_CHECK_STATE

State of check mark for children elements, calculates automatically.
Can be one of following values:
- `AIMPUI_CHECKSTATE_UNCHECKED`
- `AIMPUI_CHECKSTATE_CHECKED`
- `AIMPUI_CHECKSTATE_MIXED`

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_NODE_PROPID_EXPANDED

Default value: 1

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_NODE_PROPID_IMAGEINDEX

Index of image to draw in the IAIMPUIImageList

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_NODE_PROPID_INDEX

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_TL_NODE_PROPID_LEVEL

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

#### AIMPUI_TL_NODE_PROPID_SELECTED

0 - is not selected.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32

#### AIMPUI_TL_NODE_PROPID_TAG

Field for custom data

- **Type:** Integer (in 32-bit app) / Int64 (in 64-bit app)

### Methods: Nodes

#### Add

- `out` **Node** — `IAIMPUITreeListNode`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### ClearChildren

Removes all children nodes

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### FindByTag

- `in` **Tag** — `NativeUInt`
- `in` **Recursive** — `LongBool`
- `in` **IID** — `TGUID`
  IID_IAIMPUITreeListNode
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### FindByValue

- `in` **ColumnIndex** — `Integer`
  Absolute index of column
- `in` **Value** — `IAIMPString`
  Value to find
- `in` **Recursive** — `LongBool`
- `in` **IID** — `TGUID`
  IID_IAIMPUITreeListNode
- `out` **Node** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Get

- `in` **Index** — `Integer`
  Can be one of following values:

  `AIMPUI_FLAGS_TL_NODE_GET_PARENT` - an access to parent node
  `AIMPUI_FLAGS_TL_NODE_GET_NEXTSIBLING` - an access to next sibling node
  `AIMPUI_FLAGS_TL_NODE_GET_PREVSIBLING` - an access to previous sibling node

  From 0 to GetCount - 1 - an access to children IAIMPUITreeListNode elements
- `in` **IID** — `TGUID`
- `out` **Obj** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetCount

- `out` **Result** — `Integer`

### Methods: Values

#### ClearValues

Clear all values

- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### GetValue

- `in` **Index** — `Integer`
  Absolute column index of column, can be more than real number of columns.
- `out` **Value** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### SetValue

- `in` **Index** — `Integer`
  Absolute column index of column, can be more than real number of columns.
- `in` **Value** — `IAIMPString`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Methods: Groups

#### GetGroup

- `in` **IID** — `TGUID`
  IID_IAIMPUITreeListGroup
- `in` **Group** — ``
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread
