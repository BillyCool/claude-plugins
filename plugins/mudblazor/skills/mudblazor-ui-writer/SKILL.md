---
name: mudblazor-ui-writer
description: >-
  Expert MudBlazor UI development with a full offline, source-verified copy of
  the MudBlazor docs. Use for any MudBlazor work: building pages/layouts/forms,
  picking or configuring Mud* components, questions about component parameters,
  breakpoints, colors, theming, typography, CSS utility classes, dialogs,
  snackbars, or data grids ("add a MudTable", "make this responsive", "why
  doesn't this MudSelect bind", "customize the theme"). Covers every component
  and enum in MudBlazor v9.11.0.
---

# MudBlazor UI writer

Write correct, idiomatic MudBlazor (Blazor component library) UIs. This skill
is a **fully offline copy of the MudBlazor docs**, extracted and verified from
the actual v9.11.0 source code (see `references/version.md` for provenance) —
prefer it over memory, which may reflect older MudBlazor versions with
different APIs.

**Golden rule: never guess a parameter, enum value, or CSS class.** Every
component parameter, default, enum, utility class, and theme default is in
`references/`. Look it up.

## How to find things

1. **Which component?** → `references/components-index.md` — one line per
   component (154 of them) with its folder. Then open
   `references/api/<Folder>.md` for the full parameter table (name, type,
   default, description).
2. **Inherited parameters:** each API table lists only the class's *own*
   parameters. Follow the `: BaseClass` in the heading — shared bases
   (`MudComponentBase` → `Class`, `Style`, `Tag`, `UserAttributes`;
   `MudBaseInput<T>` → `Value`, `Label`, `Variant`, validation, etc.) are in
   `references/api/_base-classes.md`.
3. **Enum values** (Color, Size, Variant, Typo, Severity, Anchor, …) →
   `references/enums.md` — all 87 enums with the CSS names they emit.
4. **Everything else:**

| Topic | Reference |
|---|---|
| Install, providers, `AddMudServices`, layout skeleton | `references/getting-started.md` |
| Theme, palettes (light/dark defaults), typography, CSS variables, dark mode | `references/theming.md` |
| Spacing/flex/display/border/elevation/color utility classes | `references/css-utilities.md` |
| Breakpoints (px values), grid, container, drawer, responsive patterns | `references/layout-and-breakpoints.md` |
| `IDialogService`, `ISnackbar`, `IBrowserViewportService`, `MudGlobal` | `references/services.md` |
| Icon names/namespaces, `Colors.*` constants | `references/icons-and-colors.md` |

## Writing good MudBlazor code

- **Use the component system before custom CSS.** Order of preference:
  component parameters (`Spacing`, `Elevation`, `Color`, `Dense`) → MudBlazor
  utility classes in `Class="..."` → theme customization → custom CSS with
  `var(--mud-palette-*)` variables. Raw hex colors and hand-rolled flex divs
  are usually a smell — `MudStack`, `MudGrid`, and `gap-*`/`d-flex` utilities
  exist for that.
- **Responsive = mobile-first.** Component params (`MudItem xs sm md`) and
  utility infixes (`pa-2 pa-md-8`) apply at that breakpoint *and up*. Prefer
  CSS-level responsiveness (utilities, `MudHidden`) over C# viewport
  subscriptions.
- **Bind, don't poke.** Inputs support `@bind-Value` (`@bind-Open`,
  `@bind-IsDarkMode`, …). For forms, wrap in `MudForm` with
  `@bind-IsValid` + per-input validation, or use `EditForm` with
  `DataAnnotationsValidator` — don't mix the two systems.
- **Check the default before setting it.** The API tables include defaults;
  don't write `Elevation="1"` noise when 1 is already the default.
- **Prerequisites bite silently.** Popover-based components (Select,
  Autocomplete, Menu, DatePicker, Tooltip) need `MudPopoverProvider`;
  `IDialogService`/`ISnackbar` need their providers; everything needs
  `AddMudServices()` and the css/js includes — `references/getting-started.md`
  has the checklist. "Component renders but doesn't open/work" is almost
  always a missing provider or non-interactive render mode.
- **Name what screen readers can't infer (v9.10+).** `MudDialog` names itself
  from its title bar; if you hide the header or replace it with a custom one,
  set `AriaLabel` or point `AriaLabelledBy` at a heading id inside the content
  (`AriaLabelledBy` wins). Pickers (`MudDatePicker`, `MudTimePicker`, …) name
  their popup after `Label`/`Placeholder`; set `PopupAriaLabel` /
  `PopupAriaLabelledBy` when the field has neither. Your own `UserAttributes`
  now override the ARIA attributes MudBlazor generates, so an explicit
  `aria-*` there is respected.
- **Empty built-in texts are localized, not blank.** Since v9.9, defaults such
  as `RequiredError`, `MudSelect.SelectAllText` and
  `MudPageContentNavigation.Headline` are `string.Empty` and resolve to a
  localized message at render time. Don't treat `""` as "no text", don't
  re-set the English literal, and customize wording through the localization
  interceptor (`ILocalizationInterceptor`) for app-wide changes. Don't read
  the parameter's value expecting the displayed text.
- **DataGrid cell/row interaction.** Prefer `CellClick` /
  `CellContextMenuClick` (v9.9) — their `DataGridCellClickEventArgs<T>` carry
  `Item`, `RowIndex`, `ColumnIndex`, `Column` and `MouseEventArgs` — over
  hand-rolled cell templates when you need to know which cell was hit.
  `SelectOnRowClick="false"` plus `SelectColumn`, or `SelectionChangeable="false"`
  (selection settable only in code), covers checkbox-only and read-only
  selection. `ColumnReorderMode` (`Swap` default / `Insert`) controls drag-drop
  reordering.
- **Chips and links.** A `MudChip` with `Href` renders as a real anchor: the
  browser handles the click, `OnClick` is not raised and the chip can't be
  selected in a `MudChipSet` (v9.11 fixed link chips that failed to navigate
  inside a set or with `OnClick` set). The close button is also unavailable
  with `Href` — use a plain `OnClick` chip if you need click/close/selection.
- **Upgrading from old majors:** the `MUD0002` analyzer (unknown parameter)
  now names the replacement for parameters removed in v7–v9 (rename,
  inverted value, `@bind-` partner changes), so follow its hint rather than
  guessing.
- **Version honesty.** This skill documents v9.11.0. If the user's project pins
  an older major (check their `.csproj`), flag API differences rather than
  assuming — v7 renamed many members and halved spacing increments.

## Answer style

- For "how do I…" questions, give a minimal working `.razor` snippet using
  verified parameters, not prose alone.
- When several components could work (Table vs DataGrid, Select vs
  Autocomplete), state the choice and the one-line reason
  (DataGrid = built-in sorting/filtering/editing; Table = lighter,
  template-driven).
- Cite the reference you used when correcting someone's code, e.g.
  "per `api/Select.md`, the parameter is `MultiSelection`, not `MultiSelect`".
