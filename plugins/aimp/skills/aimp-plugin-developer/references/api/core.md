# Core

## Core

- IAIMPServiceConfig
- IAIMPServiceLog
- IAIMPServiceShutdown
- IAIMPServiceVersionInfo

## IAIMPServiceConfig

### Description

IAIMPServiceConfig is interface for an access to common configuration file for current user.

Plugin must use this interface for loading / saving it own settings.

### Parent

IAIMPServiceConfig is inherited from IAIMPConfig

### Methods

#### FlushCache

Method saves all cached data to disk.
Method works slowly, do not call it so often.

- `out` **Result** — `HRESULT`
  S_OK - Method successes
  E_ACCESSDENIED - Method has been called from non-main thread
  E_UNEXPECTED - Unexpected failure

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceConfig, ...);

### Summary

- **Definitions:** apiCore.pas / apiCore.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### See also

- Where plugin must store user settings?]

## IAIMPServiceLog

### Description

IAIMPServiceLog allows the plugin to write its events to the app's main log.

### Methods

#### Add

- `in` **Text** — `PChar`
  The message text for logging, should not contain line breaks, should end with a null-character.
- `in` **Reserved** — `DWORD`
  Reserved, put `0`

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceLog, ...);

### Summary

- **Definitions:** apiCore.pas / apiCore.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3061

## IAIMPServiceShutdown

### Description

IAIMPServiceShutdown provides an ability to shutdown Windows or the application.

### Methods

#### Restart

- `in` **Params** — `IAIMPString`
  Command line parameters, can be `nil / null`
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

#### Shutdown

- `in` **Flags** — `DWORD`
  Combination of following flags:
  - `AIMP_SERVICE_SHUTDOWN_FLAGS_HIBERNATE`
  - `AIMP_SERVICE_SHUTDOWN_FLAGS_POWEROFF`
  - `AIMP_SERVICE_SHUTDOWN_FLAGS_SLEEP`
  - `AIMP_SERVICE_SHUTDOWN_FLAGS_LOGOFF`
  - `AIMP_SERVICE_SHUTDOWN_FLAGS_REBOOT`
  - `AIMP_SERVICE_SHUTDOWN_FLAGS_CLOSE_APP`
  - `AIMP_SERVICE_SHUTDOWN_FLAGS_NO_CONFIRM` - Suppress confirmation dialog (for Computer shutdown only)
  Remark 1: flags `AIMP_SERVICE_SHUTDOWN_FLAGS_HIBERNATE`, `AIMP_SERVICE_SHUTDOWN_FLAGS_SHUTDOWN`, `AIMP_SERVICE_SHUTDOWN_FLAGS_LOGOFF`, `AIMP_SERVICE_SHUTDOWN_FLAGS_REBOOT` and `AIMP_SERVICE_SHUTDOWN_FLAGS_SLEEP` must not be used at same time.

  Remark 2: flag `AIMP_SERVICE_SHUTDOWN_FLAGS_CLOSE_APP` can be used only with `AIMP_SERVICE_SHUTDOWN_FLAGS_SLEEP` or `AIMP_SERVICE_SHUTDOWN_FLAGS_HIBERNATE`.
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - The method is not implemented
  E_UNEXPECTED - An unexpected failure occurred
  E_ACCESSDENIED - The method was called from non-main thread

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceShutdown, ...);

### Summary

- **Definitions:** apiCore.pas / apiCore.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1401

## IAIMPServiceVersionInfo

### Description

This service provides an access to information about application version.

### Methods

#### FormatInfo

Method returns information about version in following format:

```
v<major number>.<minor number> <build state>, build <build number> (<build date)
```

For example:
v3.60, build 1400 (18.12.2013)
v3.60 Beta, build 1400 (18.12.2013)

- `out` **S** — `IAIMPString`
  Result
- `out` **Result** — `HRESULT`
  S_OK - Method successes
  E_UNEXPECTED - Unexpected failure

#### GetBuildDate

- `out` **Result** — `Integer`
  Build date.
  HiWord(Result) - year
  HiByte(LoWord(Result)) - month
  LoByte(LoWord(Result)) - day

#### GetBuildState

- `out` **Result** — `Integer`
  One of the following values:
  - AIMP_SERVICE_VERSION_STATE_RELEASE
  - AIMP_SERVICE_VERSION_STATE_RELEASE_CANDIDATE
  - AIMP_SERVICE_VERSION_STATE_BETA
  - AIMP_SERVICE_VERSION_STATE_ALPHA Note: flags are placed in descending order of product readiness.

#### GetBuildNumber

- `out` **Result** — `Integer`
  Absolute build number (not depended from version).

#### GetVersionID

- `out` **Result** — `Integer`
  ID of version in the XYYZ format.
  X - Major version number, does not limited
  YY - Minor version number, from 0 to 99
  Z - Number of edition, from 0 to 9

  Examples:
  3551 — 3.55.1
  10051 — 10.05.1
  0010 — 0.01.0

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceVersionInfo, ...);

### Summary

- **Definitions:** apiCore.pas / apiCore.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455
