# Internet

## Internet

- IAIMPServiceConnectionSettings
- IAIMPServiceHTTPClient
- IAIMPServiceHTTPClient2
- IAIMPServiceHTTPClient3
- IAIMPHTTPClientEvents
- IAIMPHTTPClientEvents2

## IAIMPServiceConnectionSettings

### Description

This service provides an access to current connection settings.

### Parent

IAIMPServiceConnectionSettings is inherited from IAIMPPropertyList.

### Properties

#### AIMP_SERVICE_CONSET_PROPID_CONNECTION_TYPE

Connection type, can be one of following values:
- `AIMP_SERVICE_CONSET_CONNECTIONTYPE_DIRECT` - direct connection
- `AIMP_SERVICE_CONSET_CONNECTIONTYPE_PROXY` - connection via proxy server that defined in player
- `AIMP_SERVICE_CONSET_CONNECTIONTYPE_SYSTEMDEFAULTS` - connection with current system settings

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMP_SERVICE_CONSET_PROPID_PROXY_SERVER

Symbolic or IP address of proxy-service, only for ConnectionType = AIMP_SERVICE_CONSET_CONNECTIONTYPE_PROXY

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMP_SERVICE_CONSET_PROPID_PROXY_PORT

Port of proxy server, only for ConnectionType = AIMP_SERVICE_CONSET_CONNECTIONTYPE_PROXY

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMP_SERVICE_CONSET_PROPID_PROXY_USERNAME

User name (optional, can be empty), only for ConnectionType = AIMP_SERVICE_CONSET_CONNECTIONTYPE_PROXY

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMP_SERVICE_CONSET_PROPID_PROXY_USERPASS

User password (optional, can be empty), only for ConnectionType = AIMP_SERVICE_CONSET_CONNECTIONTYPE_PROXY

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

#### AIMP_SERVICE_CONSET_PROPID_TIMEOUT

Timeout, in milliseconds.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMP_SERVICE_CONSET_PROPID_USERAGENT

- **Type:** IAIMPString
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPString, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPString>)

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceConnectionSettings, ...);

### Summary

- **Definitions:** apiInternet.pas / apiInternet.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

## IAIMPServiceHTTPClient

### Description

This service provides an ability to send "GET" or "POST" queries to remote HTTP servers.

All queries are running in separate threads - you should not create thread by yourself.
Plugin will be notified via IAIMPHTTPClientEvents when query will be completed

### Methods

#### Get

- `in` **URL** — `IAIMPString`
  To create a secure connection, you must specify "`https://`" in the URL.

  AIMP provides an ability to put custom fields in the HTTP-header. You should specify it in the URL string separate each field by CRLF.

  Example:

  ```
  'https://example.org/'#13#10'Field 1: Data'#13#10'Field 2: Data'
  ```
- `in` **Flags** — `DWORD`
  Zero or combination of followed flags:

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_WAITFOR` - the method will not return control until operation has been completed. Not recommended
  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_ACCEPT` - IAIMPHTTPClientEvents.OnAccept event will be called without synchronization (from non main thread) _((Since v6))_

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_COMPLETE` - IAIMPHTTPClientEvents.OnComplete event will be called without synchronization (from non main thread) _((Since v6))_

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_PROGRESS` - IAIMPHTTPClientEvents.OnProgress event will be called without synchronization (from non main thread) _((Since v6))_

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_PRIORITY_XXX` - task priority, refer to the IAIMPTaskPriority
  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_UTF8` - Use this flag to encode URL value to the UTF-8 Encoding
- `in` **AnswerData** — `IAIMPStream`
  Instance of binary stream for response from the server.
- `in` **EventsHandler** — `IAIMPHTTPClientEvents`
  See also IAIMPHTTPClientEvents2
- `in` **Params** — `IAIMPConfig`
  Extended settings for query (Optional, can be `nil / null`).
  For now you can use following parameters:
  - `"File\Offset"` - initial position in bytes (Int64). If server does not support seeking, query will be completed with error
- `out` **Task** — `TTaskHandle`
  Unique ID of asynchronous task
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Post

- `in` **URL** — `IAIMPString`
  To create a secure connection, you must specify "`https://`" in the URL.

  AIMP provides an ability to put custom fields in the HTTP-header. You should specify it in the URL string separate each field by CRLF.

  Example:

  ```
  'https://example.org/'#13#10'Field 1: Data'#13#10'Field 2: Data'
  ```
- `in` **Flags** — `DWORD`
  Zero or combination of followed flags:

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_WAITFOR` - the method will not return control until operation has been completed. Not recommended
  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_ACCEPT` - IAIMPHTTPClientEvents.OnAccept event will be called without synchronization (from non main thread) _((Since v6))_

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_COMPLETE` - IAIMPHTTPClientEvents.OnComplete event will be called without synchronization (from non main thread) _((Since v6))_

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_PROGRESS` - IAIMPHTTPClientEvents.OnProgress event will be called without synchronization (from non main thread) _((Since v6))_

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_PRIORITY_XXX` - task priority, refer to the IAIMPTaskPriority
  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_UTF8` - Use this flag to encode URL value to the UTF-8 Encoding
- `in` **AnswerData** — `IAIMPStream`
  Instance of binary stream for response from the server.
- `in` **PostData** — `IAIMPStream`
  Data to be sent to the server, can be set to `nil / null`.
- `in` **EventsHandler** — `IAIMPHTTPClientEvents`
- `in` **Params** — `IAIMPConfig`
  Reserved, must be set to `nil / null`
- `out` **Task** — `TTaskHandle`
  Unique ID of asynchronous task
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Cancel

Method allow you to cancel active task

- `in` **Task** — `TTaskHandle`
  Unique ID of asynchronous task
- `in` **Flags** — `DWORD`
  Zero or combination of followed flags:

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_WAITFOR` - the method will not return control until operation has been completed. Not recommended
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceHTTPClient, ...);

### Summary

- **Definitions:** apiInternet.pas / apiInternet.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

## IAIMPServiceHTTPClient2

### Description

This service is common version of the IAIMPServiceHTTPClient service. Provides an ability to send requests to remote HTTP servers.

All queries are running in separate threads - you should not create thread by yourself.
Plugin will be notified via IAIMPHTTPClientEvents when query will be completed

### Methods

#### Request

- `in` **URL** — `IAIMPString`
  To create a secure connection, you must specify "`https://`" in the URL.

  AIMP provides an ability to put custom fields in the HTTP-header. You should specify it in the URL string separate each field by CRLF.

  Example:

  ```
  'https://example.org/'#13#10'Field 1: Data'#13#10'Field 2: Data'
  ```
- `in` **Method** — `DWORD`
  Request method, can be one of following values:

  - `AIMP_SERVICE_HTTPCLIENT_METHOD_GET`
  - `AIMP_SERVICE_HTTPCLIENT_METHOD_POST`
  - `AIMP_SERVICE_HTTPCLIENT_METHOD_PUT`
  - `AIMP_SERVICE_HTTPCLIENT_METHOD_DELETE`
  - `AIMP_SERVICE_HTTPCLIENT_METHOD_HEAD`
- `in` **Flags** — `DWORD`
  Zero or combination of followed flags:

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_WAITFOR` - the method will not return control until operation has been completed. Not recommended
  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_ACCEPT` - IAIMPHTTPClientEvents.OnAccept event will be called without synchronization (from non main thread) _((Since v6))_

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_COMPLETE` - IAIMPHTTPClientEvents.OnComplete event will be called without synchronization (from non main thread) _((Since v6))_

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_PROGRESS` - IAIMPHTTPClientEvents.OnProgress event will be called without synchronization (from non main thread) _((Since v6))_

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_PRIORITY_XXX` - task priority, refer to the IAIMPTaskPriority
  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_UTF8` - Use this flag to encode URL value to the UTF-8 Encoding
- `in` **AnswerData** — `IAIMPStream`
  Instance of binary stream for response from the server.
- `in` **PostData** — `IAIMPStream`
  Data to be sent to the server, can be set to `nil / null`.

  Only for Method = AIMP_SERVICE_HTTPCLIENT_METHOD_POST / AIMP_SERVICE_HTTPCLIENT_METHOD_PUT.
- `in` **EventsHandler** — `IAIMPHTTPClientEvents`
  See also IAIMPHTTPClientEvents2
- `in` **Params** — `IAIMPConfig`
  Reserved, must be set to `nil / null`
- `out` **Task** — `TTaskHandle`
  Unique ID of asynchronous task
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Cancel

Method allow you to cancel active task

- `in` **Task** — `TTaskHandle`
  Unique ID of asynchronous task
- `in` **Flags** — `DWORD`
  Zero or combination of followed flags:

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_WAITFOR` - the method will not return control until operation has been completed. Not recommended
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceHTTPClient2, ...);

### Summary

- **Definitions:** apiInternet.pas / apiInternet.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660

## IAIMPServiceHTTPClient3

### Description

This service is common version of the IAIMPServiceHTTPClient service. Provides an ability to send requests to remote HTTP servers.

All queries are running in separate threads - you should not create thread by yourself.
Plugin will be notified via IAIMPHTTPClientEvents when query will be completed

### Methods

#### Request

- `in` **URL** — `IAIMPString`
  To create a secure connection, you must specify "`https://`" in the URL.

  AIMP provides an ability to put custom fields in the HTTP-header. You should specify it in the URL string separate each field by CRLF.

  Example:

  ```
  'https://example.org/'#13#10'Field 1: Data'#13#10'Field 2: Data'
  ```
- `in` **Method** — `DWORD`
  Request method as a string. For example: `GET`, `POST`, `PUT` and etc
- `in` **Flags** — `DWORD`
  Zero or combination of followed flags:

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_WAITFOR` - the method will not return control until operation has been completed. Not recommended
  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_ACCEPT` - IAIMPHTTPClientEvents.OnAccept event will be called without synchronization (from non main thread) _((Since v6))_

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_COMPLETE` - IAIMPHTTPClientEvents.OnComplete event will be called without synchronization (from non main thread) _((Since v6))_

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC_PROGRESS` - IAIMPHTTPClientEvents.OnProgress event will be called without synchronization (from non main thread) _((Since v6))_

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_PRIORITY_XXX` - task priority, refer to the IAIMPTaskPriority
  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_UTF8` - Use this flag to encode URL value to the UTF-8 Encoding
- `in` **AnswerData** — `IAIMPStream`
  Instance of binary stream for response from the server.
- `in` **PostData** — `IAIMPStream`
  Data to be sent to the server, can be set to `nil / null`.
- `in` **EventsHandler** — `IAIMPHTTPClientEvents`
  See also IAIMPHTTPClientEvents2
- `in` **Params** — `IAIMPConfig`
  Reserved, must be set to `nil / null`
- `out` **Task** — `TTaskHandle`
  Unique ID of asynchronous task
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

#### Cancel

Method allow you to cancel active task

- `in` **Task** — `TTaskHandle`
  Unique ID of asynchronous task
- `in` **Flags** — `DWORD`
  Zero or combination of followed flags:

  - `AIMP_SERVICE_HTTPCLIENT_FLAGS_WAITFOR` - the method will not return control until operation has been completed. Not recommended
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceHTTPClient2, ...);

### Summary

- **Definitions:** apiInternet.pas / apiInternet.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 5.40.2660

## IAIMPHTTPClientEvents

### Description

This interface allows to plugin receive notifications from active asynchronous task.

All notifications will be called from main thread if the `AIMP_SERVICE_HTTPCLIENT_FLAGS_ASYNC` flag is not specified.

### Methods

#### OnAccept

Event occurs when active task receives an HTTP-header from the server

- `in` **ContentType** — `IAIMPString`
  Mime type of received content data
- `in` **ContentSize** — `Int64`
  Content size in bytes. can be equal to zero if content size is undefined.
- `var` **Allow** — `LongBool`
  Set this parameter to FALSE to prevent content downloading and cancel the operation

#### OnComplete

- `in` **ErrorInfo** — `IAIMPErrorInfo`
  The ErrorInfo parameter contains extended information about the error, if operation failed.
- `in` **Canceled** — `LongBool`
  True if operation was canceled by user

#### OnProgress

- `in` **Downloaded** — `Int64`
  Count of downloaded data in bytes
- `in` **Total** — `Int64`
  Total data size in bytes. can be equal to zero, if total data size is undefined.

### Creating the instance

Instance of interface must be created by plugin and set to one of the IAIMPServiceHTTPClient methods.

### Summary

- **Definitions:** apiInternet.pas / apiInternet.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

## IAIMPHTTPClientEvents2

### Description

This interfaces is extension for IAIMPHTTPClientEvents. It should be implemented by plugin on same to IAIMPHTTPClientEvents level.

Interface provides an ability to receive "raw" header from server.

### Methods

#### OnAcceptHeaders

Event occurs when active task receives an HTTP-header from the server

- `in` **Header** — `IAIMPString`
  "Raw" HTTP header
- `var` **Allow** — `LongBool`
  Set this parameter to FALSE to prevent content downloading and cancel the operation

### Summary

- **Definitions:** apiInternet.pas / apiInternet.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.00.1660
