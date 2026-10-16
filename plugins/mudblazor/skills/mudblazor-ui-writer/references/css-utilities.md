# CSS utility classes

Enumerated from the actual SCSS in `src/MudBlazor/Styles/utilities` and
`Styles/core` + `Styles/abstracts` (v9.7.0). All utility rules use
`!important` unless noted.

## Breakpoint infix rule

Most utilities exist in a responsive form. The pattern is
`{prefix}-{breakpoint}-{value}`; the un-infixed form applies at all sizes.
Breakpoints are **min-width** thresholds (mobile-first):

| Infix | Min width |
|---|---|
| (none) | 0 |
| `sm` | 600px |
| `md` | 960px |
| `lg` | 1280px |
| `xl` | 1920px |
| `xxl` | 2560px |

Example: `d-none d-md-flex` hides below 960px, flex at 960px+.
Responsive variants exist for: spacing (`m*`/`p*`), `d-*`, all flexbox
utilities (`flex-*`, `justify-*`, `align-*`, `align-content-*`, `align-self-*`,
`order-*`, `gap-*`).

## Spacing (margin / padding)

Pattern: `{m|p}{side}-{breakpoint?}-{size}` where side is
`t` top · `b` bottom · `l` left · `r` right · `x` left+right · `y` top+bottom ·
`s` inline-start · `e` inline-end · `a` all.

Sizes: `0`–`16` map to 0–64px in 4px steps (`1`=4px, `2`=8px, `4`=16px …),
continuing `17`=68px to `20`=80px; plus `auto`.
Negative **margins only**: `n1`–`n20` (−4px … −80px), e.g. `mt-n4`.

Examples: `pa-4` (padding 16px), `mx-auto`, `my-2`, `px-sm-8`, `mt-n2`.

## Display

`d-{breakpoint?}-{value}` with values: `none`, `block`, `inline`,
`inline-block`, `flex`, `inline-flex`, `table`, `table-cell`, `table-row`,
`contents`.

## Flexbox

- Direction: `flex-{row|row-reverse|column|column-reverse}`
- Wrap: `flex-{wrap|nowrap|wrap-reverse}`
- Grow/shrink: `flex-grow-0`, `flex-grow-1`, `flex-shrink-0`, `flex-shrink-1`
- Sizing shorthands: `flex-1` (1 1 0%), `flex-auto` (1 1 auto),
  `flex-initial` (0 1 auto), `flex-none`
- Grow presets: `flex-grow-all`, `flex-grow-start`, `flex-grow-middle`,
  `flex-grow-end`, `flex-grow-start-and-end` (apply grow to children subsets)
- Justify: `justify-{start|end|center|space-between|space-around|space-evenly}`
- Align items: `align-{start|end|center|baseline|stretch}`
- Align content: `align-content-{start|end|center|space-between|space-around|stretch}`
- Align self: `align-self-{auto|start|end|center|stretch}`
- Order: `order-first`, `order-0` … `order-12`, `order-last`
- Gap: `gap-0` … `gap-20` (4px steps), `gap-x-*` (column-gap), `gap-y-*` (row-gap).
  Note: gap classes do **not** use `!important`.

All of the above take breakpoint infixes (`justify-md-center`, `flex-sm-column`).

## Borders

- Width: `border` (1px), `border-0`, `border-2`, `border-4`, `border-8`;
  per-side `border-{t|r|b|l|x|y}` and `border-{t|r|b|l|x|y}-{0|2|4|8}`
- Style: `border-solid`, `border-dashed`, `border-dotted`, `border-double`,
  `border-hidden`, `border-none`
- Color: `mud-border-{primary|secondary|tertiary|info|success|warning|error|dark}`
  and `mud-border-lines-default`
- Radius: `rounded` (default var), `rounded-{0|sm|lg|xl}`
  (0 / 2px / 8px / 24px), `rounded-circle`, `rounded-pill`; per-corner/side:
  `rounded-{t|b|l|r|s|e|tl|tr|bl|br|ts|te|bs|be}` each with optional
  `-{0|sm|lg|xl}` suffix
- Outline: `outline-{solid|dashed|dotted|double|none|hidden}`

## Elevation

`mud-elevation-0` … `mud-elevation-25` (box-shadow from theme `Shadows`).
Components also expose an `Elevation` int parameter with the same scale.

## Position, overflow, z-index, visibility

- Position: `relative`, `static`, `fixed`, `sticky` (plus `absolute` via style)
- Overflow: `overflow-{hidden|scroll|visible}` (no `overflow-auto`!) and axis
  variants `overflow-x-{auto|hidden|scroll|visible}`, `overflow-y-...`
- Z-index: `z-0`, `z-10`, `z-20` … `z-100` (steps of 10), `z-auto`
- Visibility: `visible`, `invisible`
- Screen-reader only: `mud-sr-only`

## Object fit / position (images)

`object-{contain|cover|fill|none|scale-down}` and
`object-{top|bottom|left|right|center|left-top|left-bottom|right-top|right-bottom}`.
(`MudImage` exposes these as `ObjectFit`/`ObjectPosition` parameters.)

## Interactivity

- Cursor: `cursor-{auto|default|pointer|wait|text|move|help|not-allowed|none|progress|cell|crosshair|vertical-text|alias|copy|no-drop|grab|grabbing|all-scroll|col-resize|row-resize|n-resize|w-resize|zoom-in|zoom-out}`
- Pointer events: `pointer-events-none`, `pointer-events-auto`

## Theme color classes (from `abstracts/_colors.scss`)

For each theme color `{primary, secondary, tertiary, info, success, warning, error, dark}`:

- `mud-{color}` — background-color
- `mud-{color}-text` — text color
- `mud-{color}-hover` and `hover:mud-{color}-hover` — hover background
- `mud-border-{color}` — border color
- `mud-theme-{color}` — background **and** correct contrast text color

Plus: `mud-inherit-text`, `mud-background`, `mud-background-gray`,
`mud-theme-transparent`, `mud-text-primary`, `mud-text-secondary`,
`mud-text-disabled` (palette text colors).

## Material color classes (from `core/_colors.scss`)

Every Material palette (red, pink, purple, deep-purple, indigo, blue,
light-blue, cyan, teal, green, light-green, lime, yellow, amber, orange,
deep-orange, brown, blue-gray, gray, shades) generates:

- Background: `{name}` for base, `{name} {shade}` combined classes for shades,
  e.g. `class="red"`, `class="red darken-2"`
- Text: `{name}-text` and `{name}-text text-{shade}`,
  e.g. `class="red-text text-darken-2"`

Shades: `lighten-5`…`lighten-1`, `darken-1`…`darken-4`, `accent-1`…`accent-4`.

## Typography classes

`MudText` renders `mud-typography mud-typography-{typo}` — you can also use
these classes directly: `mud-typography-{h1..h6|subtitle1|subtitle2|body1|body2|button|caption|overline}`.
Modifiers rendered by MudText parameters: `mud-typography-align-{left|center|right|justify}`,
`mud-typography-gutterbottom`, `mud-typography-nowrap`, `mud-typography-paragraph`.
