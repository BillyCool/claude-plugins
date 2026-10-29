# Markup, styles, colors, emoji

Verified against `src/Spectre.Console.Ansi/{AnsiMarkup,AnsiMarkupTagParser,DecorationTable,Style,Color}.cs`
and `src/Spectre.Console/Widgets/Markup.cs` (0.57.2). Where the docs site and source differ,
this file follows the source.

## Grammar

```
[style tokens]text[/]        open tag … close tag
[[   ]]                      literal [ and ]
```

- **Close with `[/]` only.** The tokenizer reads `[/` then requires `]` — `[/red]` is a parse
  error. Every `[...]` opening tag must be closed; nesting works (each `[/]` pops one).
- A lone `]` in text must be doubled (`]]`) or you get `Encountered unescaped ']' token`.
- Errors surface as `InvalidOperationException` at *render time* (unbalanced stack, unknown
  color, closing tag with nothing open).
- Style tokens are space separated and **case-insensitive**; order is irrelevant.

Tokens inside a tag (see `AnsiMarkupTagParser`):

| Token | Meaning |
|---|---|
| `red`, `deepskyblue1`, … | one of the 256 named colors (`colors.md`) |
| `#RRGGBB`, `#RGB` | hex color (3-digit form doubles each digit, CSS style) |
| `rgb(255,87,51)` | RGB triple, 0–255 |
| `0`–`255` | palette color number, e.g. `[213]text[/]` (**not in the docs page**) |
| `on` | everything after switches to background: `[white on red]`, `[on blue]` |
| `default` | ignored token (terminal default) |
| `bold`/`b`, `dim`, `italic`/`i`, `underline`/`u`, `strikethrough`/`strike`/`s`, `invert`/`reverse`, `conceal`, `slowblink`/`blink`, `rapidblink`, `none` | decorations; combine freely (docs list only the long names, source also accepts the short aliases) |
| `link` / `link=URL` | hyperlink; bare `[link]https://x[/]` uses the inner text as the URL |

Rules enforced by the parser: only **one** foreground color and **one** background color per
tag (`[red blue]` → "A foreground color has already been set"), only one `link=` per tag.
A nested tag *combines* with the enclosing style (inner decorations add; inner colors override).

```csharp
AnsiConsole.MarkupLine("[bold red on white]Alert[/] [dim]details[/]");
AnsiConsole.MarkupLine("[#7B68EE]hex[/] [rgb(255,87,51)]rgb[/] [213]palette[/]");
AnsiConsole.MarkupLine("[blue]blue [bold]and bold[/] blue again[/] plain");
AnsiConsole.MarkupLine("[link=https://spectreconsole.net underline blue]docs[/]");
AnsiConsole.MarkupLine("Array: [[0]] and tag-lookalike [[bold]]");
```

## Escaping dynamic content (the #1 source of crashes)

User/file/exception text containing `[` or `]` will throw or silently restyle. Three tools:

```csharp
string name = "data[1].json";

AnsiConsole.MarkupLineInterpolated($"[green]Processed[/] {name}");       // escapes string holes
AnsiConsole.MarkupLine($"[green]Processed[/] {Markup.Escape(name)}");   // manual
string plain = Markup.Remove("[bold]hi[/] there");                       // "hi there"
```

`MarkupInterpolated`/`MarkupLineInterpolated`/`Markup.FromInterpolated` escape only holes whose
value is a `string` (or a non-`IFormattable` object, via `ToString()`). `IFormattable` values
(ints, doubles, `DateTime`, …) are passed through to `string.Format` **unescaped** — fine for
numbers, but wrap a custom `IFormattable` in `Markup.Escape(x.ToString())` if its output can
contain brackets.

`MarkupLine(string format, params object[] args)` is `string.Format` **before** parsing: a
literal `{` / `}` in the markup must be doubled, and args are *not* escaped. If `args` is empty
the single-string overload is used and braces are untouched.

`Markup.Escape` / `Markup.Remove` are static members of the `Markup` widget; also available as
string extensions `text.EscapeMarkup()` / `text.RemoveMarkup()`.

## Text vs Markup vs Paragraph

| Type | Parses markup? | Use for |
|---|---|---|
| `Markup(string, Style? = null)` | yes | styled text widget (what `Panel("...")`, `Table.AddRow("...")`, `Rule("...")` use for string args) |
| `Text(string, Style? = null)` | no | text that must be shown verbatim |
| `Paragraph` | no (append segments yourself) | building text from styled runs: `p.Append("x", new Style(Color.Red))` |

String arguments to widget constructors/`AddRow`/`AddColumn` etc. are **parsed as markup** — escape
untrusted strings there too (`new Panel(Markup.Escape(text))`) or pass `new Text(text)`.

`Markup` and `Text` both implement `Justification` and `Overflow` (`Fold`, `Crop`, `Ellipsis`):
`new Markup("...").Centered()`, `.RightJustified()`, `.Ellipsis()`.

`AnsiMarkup.Highlight(markup, query, style)` highlights a substring of markup text.

## Style, Color, Decoration in code

```csharp
var s1 = new Style(foreground: Color.Red, background: Color.Black, decoration: Decoration.Bold | Decoration.Underline);
Style s2 = Color.Green;                         // implicit Color -> Style
Style s3 = "bold yellow on blue";               // implicit string -> Style (same grammar as markup tags)
Style s4 = Style.Parse("italic #ff8800");
Style s5 = new Style().Foreground(Color.Aqua).Decoration(Decoration.Dim);

var c1 = new Color(255, 128, 0);
var c2 = Color.FromHex("#FF8800");              // also Color.TryFromHex
Color c3 = 208;                                 // implicit from palette number
Color? c4 = Color.FromName("deepskyblue1");

AnsiConsole.Write("styled text", s1);           // Write(string, Style?) does not parse markup
AnsiConsole.Write(new Text("also styled", s2));
string asMarkup = s1.ToMarkup();                // "bold underline red on black"
```

`Decoration` is a `[Flags]` enum: `None, Bold, Dim, Italic, Underline, Invert, Conceal,
SlowBlink, RapidBlink, Strikethrough`. `Color.Default` = terminal default. Colors are
auto-downgraded to the console's `ColorSystem` (TrueColor → 256 → 16 → 8 → none), so
hard-coded hex colors are safe on limited terminals but may collapse to the nearest palette entry.

Named colors → `colors.md` (all 256 with numbers/hex and the `Color.X` member names).

## Emoji

```csharp
AnsiConsole.MarkupLine(":check_mark_button: done  :warning: careful  :rocket: go");
string s = Emoji.Replace("Build :party_popper:");     // string -> string
var rocket = Emoji.Known.Rocket;                      // PascalCase constants
```

Shortcodes: `emoji-shortcodes.md` (1429, `:snake_case:`). Emoji replacement runs on all text inside
`Markup`. Width of emoji varies by terminal — avoid them inside table cells that must align
unless you tested the target terminal.

## Hyperlinks

`[link=url]text[/]` emits OSC-8 links only when `Capabilities.Links` is true (not in GitHub
Actions or redirected output); otherwise just the text is shown. Don't rely on the URL being
visible.

## Common mistakes checklist

- Writing `[/red]` instead of `[/]`.
- Interpolating user text with `$"..."` into `MarkupLine` (use `MarkupLineInterpolated`).
- Using `AnsiConsole.WriteLine("[red]x[/]")` — prints the brackets literally (no markup parse).
- Using `string.Format`-style `{0}` args *and* braces in markup text (double the braces).
- Two colors in one tag, or an unknown color name (`[orange]` is not valid — use `orange1`,
  `darkorange`, or hex; check `colors.md`).
