# IAIMPUICardView

## Description

IAIMPUICardView is simplified version of the IAIMPUITreeList that presents the items like cards.

## Parent

IAIMPPropertyList — IAIMPUIControl — IAIMPUIWinControl — IAIMPUITreeList — IAIMPUICardView

## Properties

### AIMPUI_CV_PROPID_CARD_WIDTH

Width of card in pixels.
0 - card will use all available width (default).

Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_CV_PROPID_GLYPH_FRAME

Visibility of frame around the thumbnail (0/1)

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_CV_PROPID_GLYPH_SIZE

Size of thumbnail in pixels.
LoWord is used for width,
HiWord is used for height.

Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### AIMPUI_CV_PROPID_SETTINGS_BUTTON

Global option for settings button visibility (0/1). Default: 0.
If necessary, you may disable settings button for each card individually.

Attention! Local coordinates and sizes are defined for 100% (96 dpi) scale factor.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

## Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000

## IAIMPUICardViewItem

### Parent

IAIMPPropertyList — IAIMPUITreeListNode — IAIMPUICardViewItem

### Properties

#### AIMPUI_CV_ITEM_PROPID_CAN_DELETE

Set to 0 to disallow deletion of this card. Default: 1;
Only if the `AIMPUI_TL_PROPID_ALLOW_DELETING` property is set.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

#### AIMPUI_CV_ITEM_PROPID_GLYPH

Card glyph (optional)
Note that image must be 32-bit with correct alpha channel.

- **Type:** IAIMPImage
- **Read:** IAIMPPropertyList.GetValueAsObject(ID, IID_IAIMPImage, ..)
- **Write:** IAIMPPropertyList.SetValueAsObject(ID, <IAIMPImage>)

#### AIMPUI_CV_ITEM_PROPID_SETTINGS_BUTTON

Set to 1 to show the settings button for this card;
Only if the `AIMPUI_CV_PROPID_SETTINGS_BUTTON` property is set.

- **Type:** Integer
- **Read:** IAIMPPropertyList.GetValueAsInt32
- **Write:** IAIMPPropertyList.SetValueAsInt32

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000

## IAIMPUICardViewEvents

### Methods

#### OnItemSettings

Event occurs when user click on the settings button.

- `in` **Sender** — `IUnknown`
  Event sender
- `in` **Item** — `IAIMPUICardViewItem`
  Current card

### Summary

- **Definition:** apiGUI.pas / apiGUI.h
- **Multi-threading:** Not supported
- **Applications:** Player, Audio Converter, Advanced Tag Editor
- **Minimal Version:** 6.00.3000
