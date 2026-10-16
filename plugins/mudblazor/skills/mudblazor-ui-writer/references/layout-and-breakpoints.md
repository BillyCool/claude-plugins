# Layout, grid, and breakpoints

Verified against v9.7.0 source. Full parameter tables live in
`api/Layout.md`, `api/Grid.md`, `api/Container.md`, `api/Drawer.md`,
`api/Hidden.md`, `api/Stack.md`.

## Breakpoints (the single source of truth)

| Name | Range starts at | Meaning |
|---|---|---|
| xs | 0 | small→large phone |
| sm | 600px | small→medium tablet |
| md | 960px | large tablet / laptop |
| lg | 1280px | desktop |
| xl | 1920px | HD/4K desktop |
| xxl | 2560px | ultra-wide / 4K+ |

Defined in `Styles/abstracts/_variables.scss` and `Themes/Models/Breakpoints.cs`
(the C# model exposes them as strings if you customize a theme).

The `Breakpoint` enum additionally has combination values used by
`MudHidden.Breakpoint` and `MudDrawer.Breakpoint`:
`SmAndDown/MdAndDown/LgAndDown/XlAndDown`, `SmAndUp/MdAndUp/LgAndUp/XlAndUp`,
`None`, `Always`. See `enums.md` → Breakpoint.

Three ways to respond to breakpoints, in order of preference:
1. **CSS utilities** (`d-none d-md-flex`, `pa-2 pa-md-8`) — no C# needed.
2. **`MudHidden`** — `<MudHidden Breakpoint="Breakpoint.SmAndDown">` renders
   children conditionally (set `Invert="true"` to flip).
3. **`IBrowserViewportService`** — C# logic on breakpoint change (`services.md`).

## Page layout components

```
MudLayout
├── MudAppBar        (Fixed=true default, Elevation, Dense, Color, Bottom)
├── MudDrawer        (@bind-Open, Anchor, Variant, ClipMode, Elevation, Mini)
│   ├── MudDrawerHeader / MudDrawerContainer
│   └── MudNavMenu > MudNavLink / MudNavGroup
└── MudMainContent   (content area; add top padding via AppBar automatically)
```

- `DrawerVariant`: `Responsive` (default; collapses below `Breakpoint`),
  `Persistent`, `Temporary`, `Mini`.
- `DrawerClipMode`: `Never` (default), `Docked`, `Always` — whether the app bar
  pushes/overlaps the drawer.
- `Anchor`: `Left/Right/Start/End/Top/Bottom` (Start/End honor RTL; wrap the app
  in `MudRTLProvider` for RTL).

## MudContainer

Centers content with a max width. `MaxWidth` enum values map to breakpoints:
`ExtraSmall`, `Small`, `Medium`, `Large` (default), `ExtraLarge`,
`ExtraExtraLarge`, `False` (no cap). `Fixed="true"` snaps width to the current
breakpoint's min-width; `Gutters` (default true) adds side padding.

## 12-column grid

```razor
<MudGrid Spacing="3" Justify="Justify.Center">
    <MudItem xs="12" sm="6" md="4">…</MudItem>
    <MudItem xs="12" sm="6" md="8">…</MudItem>
</MudGrid>
```

- `MudGrid.Spacing`: int 0–20, gap = 4px × value, **default 6** (24px).
- `MudItem` takes `xs sm md lg xl xxl` ints (columns out of 12, mobile-first —
  a size applies at that breakpoint and up until overridden).
- `MudGrid.Justify` distributes items horizontally.

## MudStack — flexbox without CSS

`MudStack` is a flex container: `Row` (bool, default false = column),
`Reverse`, `Spacing` (gap, 4px steps, default 3), `Justify`, `AlignItems`,
`StretchItems`, `Wrap`, `Breakpoint` (default `None` — the breakpoint at which
the stack flips between row and column), `HtmlTag` (default `div`).
Prefer `MudStack`/`MudGrid` over hand-rolled flex divs; fall back to
`d-flex` utilities for one-offs.

## Other structure components

- `MudPaper` — surface with `Elevation` (0–25), `Outlined`, `Square`.
- `MudCard` family — `MudCardHeader/Media/Content/Actions`.
- `MudToolBar`, `MudSpacer` (flex-grow filler), `MudDivider`.
- `MudBreakpointProvider` — cascades the current `Breakpoint` to children and
  raises `OnBreakpointChanged` (`api/BreakpointProvider.md`); for most cases
  `MudHidden` or CSS utilities are simpler.
