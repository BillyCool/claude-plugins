# widgets/Rule — API (generated from source)

## `public sealed class Rule : Renderable, IHasJustification, IHasBoxBorder`

*core* · `src/Spectre.Console/Widgets/Rule.cs`

A renderable horizontal rule.

**Constructors**

- `Rule()` — Initializes a new instance of the `Rule` class.
- `Rule(string title)` — Initializes a new instance of the `Rule` class.

**Properties**

- `string? Title { get; set; }` — Gets or sets the rule title markup text.
- `Style? Style { get; set; }` — Gets or sets the rule style.
- `Justify? Justification { get; set; }` — Gets or sets the rule's title justification.
- `BoxBorder Border { get; set; }` = `BoxBorder.Square` — Gets or sets the box.

**Methods**

- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods on this type** (call as `x.Method(...)`)

- `RuleTitle(string title) -> Rule` — Sets the rule title.
- `RuleStyle(Style style) -> Rule` — Sets the rule style.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IHasBoxBorder`: `Border`, `NoBorder`, `SquareBorder`, `AsciiBorder`, `RoundedBorder`, `HeavyBorder`, `DoubleBorder`, `HeavyHorizontalBorder`, `HeavyVerticalBorder`, `DoubleHorizontalBorder`, `DoubleVerticalBorder`, `DashedBorder`, `RoundedDashedBorder`, `HeavyDashedBorder`, `DottedBorder`, `RoundedDottedBorder`, `HeavyDottedBorder`, `DashedWideBorder`, `RoundedDashedWideBorder`, `HeavyDashedWideBorder`, `NearBorder`, `BeveledBorder`, `McGuganHorizontalBorder`, `McGuganVerticalBorder`
- via `IHasJustification`: `Justify`, `LeftJustified`, `Centered`, `RightJustified`
- via `IRenderable`: `GetSegments`

