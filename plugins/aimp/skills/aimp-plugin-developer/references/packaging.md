AIMP Add-on Package
## Overview
AIMP add-on package (*.aimppack or *.zip) is simple zip archive with a speci fic  structure.
## Structure
## Package for IconSet or Skin
Each package MUST contain no more than one file. IconSet (*.dll) or Skin (*.acs?) file must be placed to root of zip-archive.
Package for Plugin
Plugin's package MUST contain a folder with a plugin name. All other files must be placed inside the folder. All 32-bit binaries and platform independed files must be placed in root of the folder. All 64-bit binaries must be placed in x64 sub-folder.
For example:
aimp_test \
Langs\*.lng      -  plugin's localization files
x64\aimp_test.so -  general 64-bit library  ( Linux)
x64\aimp_test.dll      -  general 64-bit library  ( Windows)
x64\*.*          -  all other 64-bit binaries
aimp_test.dll      -  general 32-bit library
*.*          -  all other 32-bit binaries
*.*          -  all other platform independent files (ReadMe.txt, License.pdf, etc)
