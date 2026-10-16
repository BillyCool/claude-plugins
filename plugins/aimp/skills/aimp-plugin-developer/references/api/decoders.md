# Decoders

## Decoders

- IAIMPServiceAudioDecoders
- IAIMPExtensionAudioDecoder
- IAIMPExtensionAudioDecoderOld
- IAIMPExtensionAudioDecoderPriority
- IAIMPAudioDecoder
- IAIMPAudioDecoderBufferingProgress
- IAIMPAudioDecoderNotifications
- IAIMPAudioDecoderListener

## IAIMPServiceAudioDecoders

### Description

This service provides an access to already registered decoders for audio files.

### Methods

#### CreateDecoderForStream

Method creates a decoder for specified stream

- `in` **Stream** — `IAIMPStream`
  Stream
- `in` **Flags** — `DWORD`
  Reserved, must be set to zero
- `in` **ErrorInfo** — `IAIMPErrorInfo`
  Information about the error. Should be populated by plugin if error occurs.

  Parameter can be `nil / null`.
- `out` **Decoder** — `IAIMPAudioDecoder`
  Decoder Instance
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_FAIL - An error occurs while try to parse the stream
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - Decoder for the stream was not found
  E_UNEXPECTED - An unexpected failure occurred

#### CreateDecoderForFileURI

Method creates decoder based on File URI

- `in` **FileURI** — `IAIMPString`
  Virtual file name
- `in` **Flags** — `DWORD`
  Reserved, must be set to zero
- `in` **ErrorInfo** — `IAIMPErrorInfo`
  Information about the error. Should be populated by plugin if error occurs.

  Parameter can be `nil / null`.
- `out` **Decoder** — `IAIMPAudioDecoder`
  Decoder Instance
- `out` **Result** — `HRESULT`
  S_OK - The method was successfully completed
  E_FAIL - An error occurs while try to parse the stream
  E_INVALIDARG - One of the arguments is not valid
  E_NOTIMPL - Decoder for the stream was not found
  E_UNEXPECTED - An unexpected failure occurred

### Access to service

<IAIMPCore>.QueryInterface(IID_IAIMPServiceAudioDecoders, ...);

### Summary

- **Definitions:** apiDecoders.pas / apiDecoders.h
- **Multi-threading:** Supported
- **Extensions:** IAIMPExtensionAudioDecoder, IAIMPExtensionAudioDecoderOld
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### See also

- File URI, working with virtual and real files

## IAIMPExtensionAudioDecoder

### Description

The IAIMPExtensionAudioDecoder interface is extension for the IAIMPServiceAudioDecoders service.

Interface implementation must support asynchronous access.

### Methods

#### CreateDecoder

- `in` **Stream** — `IAIMPStream`
- `in` **Flags** — `DWORD`
  0 or combination of following flags:

  - `AIMP_DECODER_FLAGS_FAST_SEEKING` - flag allows the decoder to use inaccurate seeking in IAIMPDecoder.SetPosition. Flag is used to calculate waveform-navigator.

  - `AIMP_DECODER_FLAGS_FORCE_CREATE_INSTANCE` - the flag was designed for decoders that not support multi-instance decoding. If this flag is defined plugin must drop all active decoders for an ability to create new instance of decoder
- `in` **ErrorInfo** — `IAIMPErrorInfo`
  Information about the error. Should be populated by plugin if error occurs.

  Parameter can be `nil / null`.

  Warning! Plugin must not populate the error info, if it was not detect in the Stream or File supported file format.
- `out` **Decoder** — `IAIMPAudioDecoder`
  Decoder Instance
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise
  E_PENDING - Decoder instance cannot be created because another instance of decoder is already active (this error code must be used only for decoders that are not support multi-instance decoding)

### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

Together with this interface plugin should implement and register the IAIMPExtensionFileFormat interface. This interface will allow Application to know about the new formats.

### Summary

- **Definition:** apiDecoders.pas / apiDecoders.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### See Also

- IAIMPExtensionAudioDecoderPriority
- Registering new file type

## IAIMPExtensionAudioDecoderOld

### Description

The IAIMPExtensionAudioDecoderOld interface unlike the IAIMPExtensionAudioDecoder provides an ability to create decoder based on real or virtual name of file instead of IAIMPStream.

This extension is obsolete, it has been provided for compatibility purposes for old designed decoders that are not support custom streams. Plugin must avoid to use it, because in this case following functions will be unavailable for end user: file caching, an ability to play sub tracks from set / archive and etc.

Interface implementation must support asynchronous access.

### Methods

#### CreateDecoder

- `in` **FileName** — `IAIMPString`
  Real or virtual full file name.
- `in` **Flags** — `DWORD`
  0 or combination of following flags:

  - `AIMP_DECODER_FLAGS_FAST_SEEKING` - flag allows the decoder to use inaccurate seeking in IAIMPDecoder.SetPosition. Flag is used to calculate waveform-navigator.

  - `AIMP_DECODER_FLAGS_FORCE_CREATE_INSTANCE` - the flag was designed for decoders that not support multi-instance decoding. If this flag is defined plugin must drop all active decoders for an ability to create new instance of decoder
- `in` **ErrorInfo** — `IAIMPErrorInfo`
  Information about the error. Should be populated by plugin if error occurs.

  Parameter can be `nil / null`.

  Warning! Plugin must not populate the error info, if it was not detect in the Stream or File supported file format.
- `out` **Decoder** — `IAIMPAudioDecoder`
  Decoder Instance
- `out` **Result** — `HRESULT`
  S_OK - If success, any other value otherwise
  E_PENDING - Decoder instance cannot be created because another instance of decoder is already active (this error code must be used only for decoders that are not support multi-instance decoding)

### Creating instance

Instance should be created by plugin and must be registered in the application in the plugin initialization method via the IAIMPCore.RegisterExtension method.

Together with this interface plugin should implement and register the IAIMPExtensionFileFormat interface. This interface will allow Application to know about the new formats.

### Summary

- **Definition:** apiDecoders.pas / apiDecoders.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

### See Also

- IAIMPExtensionAudioDecoderPriority
- Registering new file type

## IAIMPExtensionAudioDecoderPriority

### Description

The IAIMPExtensionAudioDecoderPriority provides an ability to specify priority for the IAIMPExtensionAudioDecoder extension. The interface should be implemented by plugin on same level as the IAIMPExtensionAudioDecoder.

The priority will be calculated based on plugin loading order if the IAIMPExtensionAudioDecoderPriority is not implemented.

Decoders with higher priority processes first during decoder creation for file / stream.

### Methods

#### GetPriority

- `out` **Result** — `Integer`
  Any number

### Summary

- **Definition:** apiDecoders.pas / apiDecoders.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.60.2160

## IAIMPAudioDecoder

### Methods

#### GetFileInfo

Method provides an meta-data for decoding file or stream.

Decoder may not implement this method, in this case the application will try to get information about decoding file via another file info provides. You must return the False value.

Attention! In implementation of this method you must not call the GetFileInfo* methods of the IAIMPServiceFileInfo service.

- `in` **FileInfo** — `IAIMPFileInfo`
- `out` **Result** — `LongBool`
  True - if the FileInfo parameter was populated by decoder

#### GetStreamInfo

Method provides an information about the audio stream

- `out` **SampleRate** — `Integer`
  Sampling rate
- `out` **Channels** — `Integer`
  Count of channels
- `out` **SampleFormat** — `Integer`
  Sample format of uncompressed data, can be one of following values:
  - AIMP_DECODER_SAMPLEFORMAT_08BIT
  - AIMP_DECODER_SAMPLEFORMAT_16BIT
  - AIMP_DECODER_SAMPLEFORMAT_24BIT
  - AIMP_DECODER_SAMPLEFORMAT_32BIT
  - AIMP_DECODER_SAMPLEFORMAT_32BITFLOAT
  - AIMP_DECODER_SAMPLEFORMAT_64BITFLOAT _((since v5.40))_
- `out` **Result** — `LongBool`

#### IsSeekable

This flag defines if seeking support by decoder or not

- `out` **Result** — `LongBool`

#### IsRealTimeStream

This flag defines if is real-time stream or not.

- `out` **Result** — `LongBool`

#### GetAvailableData

Count of available data for read in bytes in format of uncompressed data.
In general cases, this value should be equal to GetSize - GetPosition.

- `out` **Result** — `Int64`

#### GetSize

Duration in bytes in format of uncompressed data.
can be equal to zero, if the IsSeekable or/and the IsRealTimeStream method returns the True value

- `out` **Result** — `Int64`

#### GetPosition

Current position in bytes in format of uncompressed data.

- `out` **Result** — `Int64`

#### SetPosition

- `in` **Value** — `Int64`
  New position in bytes in format of uncompressed data.
- `out` **Result** — `LongBool`

#### Read

- `in` **Buffer** — `PByte`
- `in` **Count** — `Integer`
  Number of bytes to be read
- `out` **Result** — `Integer`
  Number of read bytes

### Note 1

The interface implementation must support asynchronous access.

### Note 2

Note that all sizes are defined in PCM format of uncompressed data.

Example:
The GetStreamInfo method return following values for parameters: `SampleRate = 44100, Channels = 2, SampleFormat = AIMP_DECODER_SAMPLEFORMAT_16BIT`. So, in this case the GetPosition method will return following value for 1 second: `1 * 44100 * 2 * (16 / 8) = 176400 bytes`.

### Creating the instance

Instance of decoder creates by the IAIMPExtensionAudioDecoder or the IAIMPExtensionAudioDecoderOld extension via calling the CreateDecoder method

### Summary

- **Definition:** apiDecoders.pas / apiDecoders.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 3.60.1455

## IAIMPAudioDecoderBufferingProgress

### Description

The interface should be implemented by plugin on same to IAIMPAudioDecoder level

### Methods

#### Get

- `out` **Value** — `Double`
  Buffering progress, from 0.0 to 1.0.
- `out` **Result** — `LongBool`

### Summary

- **Definitions:** apiDecoders.pas / apiDecoders.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.10.1815

## IAIMPAudioDecoderNotifications

### Description

The IAIMPAudioDecoderNotifications interface provides an ability to player to subscribe for decoder notifications (if decoder supports it). Interface should be implemented by plugin on same level as the IAIMPAudioDecoder interface.

### Methods

#### ListenerAdd

- `in` **Listener** — `IAIMPAudioDecoderListener`

#### ListenerRemove

- `in` **Listener** — `IAIMPAudioDecoderListener`

### Summary

- **Definition:** apiDecoders.pas / apiDecoders.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.60.2160

## IAIMPAudioDecoderListener

### Description

The interface provides an ability to player to receive notifications from the decoder.

### Methods

#### Changed

- `in` **Changes** — `Integer`
  One or combination of following flags:
  + AIMP_DECODER_CHANGE_INPUTFORMAT - format of audio stream has been changed, refer to the IAIMPAudioDecoder.GetStreamInfo.

  The method must be invoked by the plugin when specified change occurs.

### Summary

- **Definition:** apiDecoders.pas / apiDecoders.h
- **Multi-threading:** Supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 4.60.2160

### See Also

- IAIMPAudioDecoderNotifications
