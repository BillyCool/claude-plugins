# Image components — API (generated from source)

## MudImage : MudComponentBase

A simple component that displays an image.

*This component is equivalent to the `img` HTML tag.*

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Fluid` | `bool` | `false` | Scales this image to the parent container. Defaults to `false`. |
| `Src` | `string?` | – | The path to the image. |
| `FallbackSrc` | `string?` | – | The fallback image path to use if `Src` fails to load. |
| `Alt` | `string?` | – | The alternate text for this image. |
| `Height` | `int?` | `null` | The height of this image, in pixels. Defaults to `null`. |
| `Width` | `int?` | `null` | The width of this image, in pixels. Defaults to `null`. |
| `Elevation` | `int` | `0` | The size of the drop shadow for this image. Defaults to `0`. |
| `ObjectFit` | `ObjectFit` | `ObjectFit.Fill` | Controls how this image is resized. Defaults to `Fill`. |
| `ObjectPosition` | `ObjectPosition` | `ObjectPosition.Center` | Controls how this image is positioned within its container. Defaults to `Center`. |
