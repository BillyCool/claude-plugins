# Highlighter components — API (generated from source)

## MudHighlighter : MudComponentBase

Highlights occurrences of one or more search terms within a block of text, wrapping each match in a `mark` element.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Text` | `string?` | – | The text to consider for highlighting. |
| `HighlightedText` | `string?` | – | The text to highlight within `Text`. |
| `HighlightedTexts` | `IEnumerable<string>` | `[]` | The multiple text fragments to highlight within `Text`. |
| `CaseSensitive` | `bool` | `false` | Whether highlighted text is case sensitive. Defaults to `false`. |
| `UntilNextBoundary` | `bool` | `false` | Highlights text until the next RegEx boundary. Defaults to `false`. |
| `Markup` | `bool` | `false` | Renders text as a `RenderFragment`. Defaults to `false`. |
