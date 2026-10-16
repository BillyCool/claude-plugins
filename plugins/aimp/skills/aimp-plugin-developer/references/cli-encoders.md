Integration of command-line based encoders
## Overview
First and important , the command line encoder  MUST  supports for 1) std-in (input pipe) 2) streaming mode (length of input stream is unknown).
The command-line based encoder integration is simple AIMP Addons Package that used for all other addons (Refer to the " AIMP  A ddon  P ackage "   article for more information).
Unlike plug-ins, entry-point of the encoder is special configuration template that  must be  named in following way " enc_*.xml ":
enc_test  \
enc_test . xml      -  general  configuration
x64\*.*          -  all 64-bit binaries
*.*          -  all 32-bit binaries
*.*          -  all other platform independent files (ReadMe.txt, License.pdf, etc)

## Configuration template  is :
## <encoders
generator = "AIMP"
version = "1000"
author = " author "
name = " plugin name "
info = " plugin description "
>
<encoder  Name = " Encoder Name " App = " cmd-line-encoder.exe "  debug=" 0 " >
<description>
<inputformats  type =" autogen ">
<autogen
SampleRates =" 44100;48000 "
SampleFormats =" 8;16 "
Channels =" 1;2 "
/>
</inputformats>
<inputformats  type =" list ">
<format
Channels =" 2 "
SampleFormat =" 16 "
SampleRate =" 44100 " />
...
</inputformats>
<property  name = " Ext "  value = " .mp3 "/>
<property  name = " InputMegaByteMax "  value = " Int64 "/>
<property  name = " OutputMegaBytesMax "  value = " Int64 "/>
<property  name = " IgnoreLength "  value = " 1 or 0 "/>
</description>
<presets>
<preset
name = " Preset Friendly Name "
cmdparams = " -switch %macro1% %macro2% -output %output% "
>
<var  name = " Friendly Name "  cmdparams = " macro 1 ">
<val  name = " Friendly Name "  cmdparams = " macro value " />
...
</var>
<var  name = " Friendly Name "  cmdparams = " macro 2 ">
<val  name = " Friendly Name "  cmdparams = " macro value " />
...
</var>
</preset>
...
</presets>
</encoder>
...
</encoders>

## Structure
encoder s  -  at least one   encoder  entry.
encoder  -  MUST  contains  description  and  presets  entries.
debug  - set to  1  to display encoder console output,  optional .
description  -  MUST  contains  one   inputformats  and  one or more   property  entries.
inputformats  may be defined in two ways according to value of  type  attribute:
autogen
List of supported formats will be generated according to specified lists.
Here you can specify lists of supported sample rates, sample formats 1  and channels.
1 ** Refer to  sampleFormat  description for details.**
list
In this case, the  inputformats  contains a plain list of the  format  entry.
sampleFormat  may be one of following values:  8 ,  16 ,  24 ,  24i32 ,  32 ,  32f .
property
Ext  - specifies output file extension, ** REQUIRED** .
InputMegaByteMax  - specifies how many bytes can be send into the encoder.  Optional , default is 4GB (limit of WAVE header that uses for pipe transfering).
IgnoreLength  - specifies that the encoder ignores length defined in WAVE header. Its means, more than 4GB can be transfered via pipe.
Optional , default is 0.
OutputMegaBytesMax  - specifies how many bytes can be written to a file of used format.
Optional , output will be unlimited if property is not specified.
ID3  - set to  "1"  if the encoder expects ID3v2 tag header in beginning of data stream.  Optional , default is 0.
RequiresLength  - set to  "1"  if the encoder requires correct length defined in WAVE header. By default, AIMP set length to 0 that usually interpreted by encoders like unknown length.
presets  - contains  at least one   preset  entry.
preset  -  MUST  contain  name  and  cmdparams  attributes. The  name  attribute specifies friendly name of the preset that will be displayed to user. The  cmdparams  attribute specifies command line arguments that will be passed to command line encoder if user selects the preset.
The command line  MUST  contains the  %output%  macro that will be expanded to an actual output file name. Additionally, it may refers to custom macros which values defines in  var/val  entry inside the  preset  entry.
var  -  optional  entry that defines a custom macro used in command line for the encoder. The  name  attribute of the entry defines a friendly name that will be displayed to user. The  cmdparams  specifies a macro name. The entry contains  at least one   val  entry.
val  - The  name  attribute of the entry defines a friendly name that will be displayed to user. The  cmdparams  defines command line arguments that will be used as replacement of macro in command line that passes to the encoder if user selects the entry. 

Example
Refer to configuration files of the encoders that shipped with the application:
<AIMP>\Plugins\enc_opus\enc_opus.xml
<AIMP>\Plugins\enc_tta\enc_tta.xml
