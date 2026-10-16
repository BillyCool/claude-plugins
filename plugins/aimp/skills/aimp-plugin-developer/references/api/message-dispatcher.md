# Message Dispatcher

## IAIMPServiceMessageDispatcher

### Description

All communication between application modules is carried out via messages. This service provides an access to the messaging mechanism.

### Methods

#### Send

- `in` **Message** — `DWORD`
  Message identification.
  Please refer to the "Properties", "Events", "Commands" chapters.
- `in` **Param1** — `Integer`
- `in` **Param2** — `Pointer`
- `out` **Result** — `HRESULT`

#### Register

Method allows to register custom message

- `in` **MessageName** — `PChar`
  Message name
- `out` **Result** — `DWORD`
  Message identification, it depended from name. Method will return same ID for same names.

#### Hook

- `in` **Hook** — `IAIMPMessageHook`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Unhook

- `in` **Hook** — `IAIMPMessageHook`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceMessageDispatcher, ...);

### Summary

- **Definitions:** apiMessages.pas / apiMessages.h
- **Multi-threading:** Supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

## IAIMPMessageHook

### Description

The IAIMPMessageHook interface provides an ability to hook all messages that processes via IAIMPServiceMessageDispatcher.

Note that you must remove hook manually in the IAIMPPlugin.finalize handler

### Methods

#### CoreMessage

- `in` **Message** — `DWORD`
  Message identification.
  Please refer to the "Properties", "Events", "Commands" chapters.
- `in` **Param1** — `Integer`
- `in` **Param2** — `Pointer`
- `var` **Result** — `HRESULT`
  Set value to S_OK if you have processed this message.

### Creating the instance

Instance must implemented and created by plugin

### Summary

- **Definitions:** apiMessages.pas / apiMessages.h
- **Multi-threading:** Not supported
- **Applications:** Player
- **Minimal Version:** 3.60.1455

### See also

- Custom messages
- Hook messages

## More in this chapter

- **Commands** — `api/message-dispatcher-commands.md`
- **Properties** — `api/message-dispatcher-properties.md`
- **Events** — `api/message-dispatcher-events.md`
