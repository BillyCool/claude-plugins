# FileUpload components — API (generated from source)

## MudFileUpload<T> : MudFormComponent<T, string>

A form component that lets users upload one or more files.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Files` | `T?` | – | The selected file or files. When `T` is `IBrowserFile`, a single file is provided. When `T` is `IReadOnlyList{IBrowserFile}`IReadOnlyList&lt;IBrowserFile&gt;</see>, multiple files are provided. |
| `FilesChanged` | `EventCallback<T?>` | – | Occurs when `Files` has changed. |
| `DraggingChanged` | `EventCallback<bool>` | – | Occurs when `Dragging` has changed. |
| `OnFilesChanged` | `EventCallback<InputFileChangeEventArgs>` | – | Occurs when the user selects or drops files. Not raised when `SuppressOnChangeWhenInvalid` is `true` and validation fails. |
| `OnDragEnter` | `EventCallback<DragEventArgs>` | – | Occurs when a drag operation enters this component. |
| `OnDrop` | `EventCallback<DragEventArgs>` | – | Occurs when files are dropped onto this component. |
| `OnDragLeave` | `EventCallback<DragEventArgs>` | – | Occurs when a drag operation leaves this component. |
| `OnDragEnd` | `EventCallback<DragEventArgs>` | – | Occurs when a drag operation ends for this component. |
| `AppendMultipleFiles` | `bool` | `false` | Appends new files to the existing selection. Defaults to `false`. This applies when `T` is `IReadOnlyList{IBrowserFile}`IReadOnlyList&lt;IBrowserFile&gt;</see>. |
| `CustomContent` | `RenderFragment<MudFileUpload<T>>?` | – | The custom content used to render the upload UI. The context is the current `MudFileUpload{T}` instance and can be used to call `OpenFilePickerAsync`. |
| `SelectedTemplate` | `RenderFragment<T?>?` | – | The template used to render selected files. When `null`, a default chip list is shown. |
| `SuppressOnChangeWhenInvalid` | `bool` | `false` | Prevents raising `OnFilesChanged` when validation fails during an upload. Defaults to `false`. |
| `Accept` | `string?` | `null` for any file type` | The accepted file types for the file picker. Defaults to `null` for any file type. Multiple file types must be separated by commas (e.g. `".png,.jpg"`). |
| `Hidden` | `bool` | `true` | Hides the internal `InputFile` element. Defaults to `true`. When `false`, the input is visible. |
| `DragAndDrop` | `bool` | `false` | Enables a drag-and-drop area inside the component. Defaults to `false`. During drag operations, the internal `InputFile` element can be shown to capture drop events even when `Hidden` is `true`. |
| `Dragging` | `bool` | – | Indicates whether a drag operation is active. When `true`, the internal `InputFile` element is shown to capture the drop, which temporarily overrides `Hidden`. When `false`, visibility follows `Hidden` again. Drop-related events reset it to `false`. |
| `InputClass` | `string?` | `null` | The CSS classes applied to the internal `InputFile` element. Defaults to `null`. These classes apply when `Hidden` is `false`. Multiple classes must be separated by spaces. |
| `InputStyle` | `string?` | `null` | **[Obsolete]** The CSS styles applied to the internal `InputFile` element. Defaults to `null`. These styles apply when `Hidden` is `false`. Prefer `InputClass`. |
| `MaximumFileCount` | `int` | `10` | The maximum number of files retrieved per selection. Defaults to `10`. This does not limit the total number of files; enforce overall limits in `FilesChanged`. |
| `MaxFileSize` | `long?` | `null` (no limit)` | The maximum allowed file size in bytes. Defaults to `null` (no limit). Files exceeding this limit are rejected and a validation error is added. |
| `Disabled` | `bool` | `false` | Prevents the user from interacting with this component. Defaults to `false`. |
