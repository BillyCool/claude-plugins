# Threading

## Threading

- IAIMPServiceThreads
- IAIMPTask
- IAIMPTaskOwner
- IAIMPTaskPriority

## IAIMPServiceThreads

### Description

Service provides an access to thread pool and allows to plugin add a task to asynchronous execution. Note that number of running threads at same time is limited. All tasks will be added to special queue and will be executed when one of the threads is idle.

Warning! Make sure that all your tasks is completed or canceled during plugin finalization.

### Methods

#### ExecuteInMainThread

- `in` **Task** — `IAIMPTask`
- `in` **Flags** — `DWORD`
  Zero or combination of following flags:

  - `AIMP_SERVICE_THREADS_FLAGS_WAITFOR` - the method will not return control until operation has been completed if this flag is used. Not recommended. Otherwise, task will be queued and executed when main thread is idle
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### ExecuteInThread

- `in` **Task** — `IAIMPTask`
- `out` **TaskHandle** — `DWORD_PTR`
  Task handle, if method succeeded
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Cancel

- `in` **TaskHandle** — `DWORD_PTR`
  Task handle
- `in` **Flags** — `DWORD`
  Zero or combination of following flags:

  - `AIMP_SERVICE_THREADS_FLAGS_WAITFOR` - the method will not return control until operation has been completed if this flag is used
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### WaitFor

Method provides an ability to wait for task completion

- `in` **TaskHandle** — `DWORD_PTR`
  Task handle
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceThreads, ...);

### Summary

- **Definition:** apiThreading.pas / apiThreading.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.60.2160

## IAIMPTask

### Description

Must be implemented on plugin level.

Interface implementation must support asynchronous access.

### Methods

#### Execute

- `in` **Owner** — `IAIMPTaskOwner`
  Owner provides an ability to know if user cancel the task.
  You must abort current operation as soon as possible.

### Recommendations

During implementation the Execute method handler you should call the IsCanceled method and check it result. If method returns True - you must abort current operation as soon as possible.

Example:

```
procedure <IAIMPTask>.Execute(Owner: IAIMPTaskOwner);
begin
// Check if task is canceled
if Owner.IsCanceled then
// aborting the operation

// do something

// Check if task is canceled
if Owner.IsCanceled then
// aborting the operation

// do something
end;
```

### Summary

- **Definition:** apiThreading.pas / apiThreading.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.60.2160

### See Also

- IAIMPTaskPriority

## IAIMPTaskOwner

### Description

This is tool interface that provides an ability to plugin to be notified about canceling the operation. The instance of interface will be created by the application and will be sent to plugin as parameter of the IAIMPTask.Execute method.

### Methods

#### IsCanceled

- `out` **Result** — `LongBool`
  Plugin must break the operation if the method returns True.

### Summary

- **Definition:** apiThreading.pas / apiThreading.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.60.2160

## IAIMPTaskPriority

### Description

This is tool interface that provides an ability to plugin define priority of task. Interface should be implemented on same to IAIMPTask level. Priority affects to task position in the waiting queue (waiting queue is used if all threads from pool are busy) and to priority of working thread.

### Methods

#### GetPriority

- `out` **Result** — `Integer`
  AIMP_TASK_PRIORITY_NORMAL
  AIMP_TASK_PRIORITY_LOW
  AIMP_TASK_PRIORITY_HIGH

### Summary

- **Definition:** apiThreading.pas / apiThreading.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.60.2160
