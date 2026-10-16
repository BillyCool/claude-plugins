# Version provenance

This skill's knowledge is confirmed against live MudBlazor source, not memory.

- **MudBlazor version reflected:** v9.11.0 (released 2026-09-27)
- **Last synced:** 2026-10-05 (incremental sync from v9.8.0)
- **Synced by:** `mudblazor-skill-maintainer` skill (extraction script:
  `../mudblazor-skill-maintainer/scripts/extract_api.py`)
- **Source of truth:** https://github.com/MudBlazor/MudBlazor at tag `v9.11.0`

## What was extracted mechanically (regenerate, don't hand-edit)

| Files | Generated from |
|---|---|
| `api/*.md` (84 files) | `src/MudBlazor/Components/**/*.cs` + `Mud*.razor` (razor-only components) + `src/MudBlazor/Base/*.cs` — every `[Parameter]` property with type, default, XML doc summary/remarks, inheritance. 154 `Mud*` components, ~1,800 parameters (component count unchanged from v9.8.0; a handful of new parameters). |
| `components-index.md` | class declarations + class-level XML docs |
| `enums.md` | `src/MudBlazor/{Enums,Services,Utilities}/**` + enums found in Components — 87 enums with `[Description]` CSS names |

## What was hand-written (verify facts against these source anchors)

| File | Source anchors |
|---|---|
| `getting-started.md` | `src/MudBlazor.Docs/Pages/Getting Started/Installation/ManualMarkdown/*`, `src/MudBlazor/Extensions/ServiceCollectionExtensions.cs` (`AddMudServices`) |
| `theming.md` | `src/MudBlazor/Themes/MudTheme.cs`, `Themes/Models/{Palette,PaletteDark,Typography,LayoutProperties,Z-Index,Breakpoints}.cs`; CSS var names grepped from `src/MudBlazor/Styles/**` |
| `css-utilities.md` | `src/MudBlazor/Styles/utilities/**/*.scss`, `Styles/abstracts/{_variables,_colors}.scss`, `Styles/core/{_colors,_elevation}.scss`, `Styles/components/_typography.scss` |
| `layout-and-breakpoints.md` | `Styles/abstracts/_variables.scss` (breakpoint px), generated `api/{Layout,Grid,Container,Drawer,Hidden,Stack,BreakpointProvider}.md` |
| `services.md` | `src/MudBlazor/Services/Dialog/{IDialogService,DialogOptions}.cs`, `Components/Snackbar/SnackbarService.cs`, `Services/Browser/IBrowserViewportService.cs`, `Services/MudGlobal.cs` |
| `icons-and-colors.md` | `src/MudBlazor/Icons/**` (const counts per class), `src/MudBlazor/Colors/Colors.cs` |

## v9.8.0 → v9.11.0 changes worth knowing

- Breaking (v9.9.0): inputs now raise `OnBlur` for read-only inputs;
  `MudExpansionPanel` no longer greys icons in the body when disabled. Neither
  was asserted in hand-written prose.
- New parameters (in `api/`): `MudDataGrid` `CellClick`, `CellContextMenuClick`,
  `SelectionChangeable`, `ColumnReorderMode` (new enum
  `DataGridDragAndDropColumnReorderMode`: `Swap`/`Insert`); `MudDialog`
  `AriaLabel`/`AriaLabelledBy`; `MudPicker` `PopupAriaLabel`/`PopupAriaLabelledBy`;
  `MudListItem` `KeyboardEnabled`; data-grid footer `GroupItems`.
  `TableGroupDefinition.GroupHeaderClass` exists (not a component, so not tabulated).
  `RegexMask` gained ZIP, MAC, GUID, hex-colour and 24-hour presets.
- Behavior: `SelectOnRowClick` now selects/deselects the row (not just toggles
  the checkbox); `MudChip` with `Href` renders an anchor (browser handles the click;
  `OnClick`/selection not raised; v9.11 fixed navigation when inside a
  `MudChipSet` or with `OnClick` set); `MudDataGrid`
  `Comparer` is honored for selection and hierarchy expansion.
- Default-text change: `MudBaseInput.RequiredError`, `MudSelect.SelectAllText`
  and `MudPageContentNavigation.Headline` now default to `string.Empty`, falling
  back to a localized message at render time (no longer the literal English).
- Services: localization services in `AddMudServices` are now registered
  **Scoped** instead of Transient. Dialog, snackbar, viewport, theme, colors and
  utility SCSS: no substantive changes (BOM removals only; `sr-only` moved to a
  mixin with the same class).
- Public members that are **not** tabulated (parameters-only extraction):
  `DataGridCellClickEventArgs<T>` (`MouseEventArgs`, `Item`, `RowIndex`,
  `ColumnIndex`, `Column`); `Column<T>.GetCellContent(T item)`;
  `MudColorPicker.ClearAsync(bool close = true)` override;
  `MudFabMenuItem.ParentMenu` cascading parameter;
  `RegexMask.UsZipCode/MacAddress/Guid/HexColor/Time24` static factories;
  `TableGroupDefinition.GroupHeaderClass`. `IForm`/`IFormComponent` member
  changes are only `public` modifier removals + doc comments (no API change).
- Analyzers: `MUD0002` now appends migration hints (rename / inverted value /
  `@bind-` partner / initial-state) for parameters removed in v7–v9.
- Source audit method (v9.8.0→v9.11.0): `git diff` of `src/MudBlazor` for
  `public|protected|[Parameter]|[CascadingParameter]|[Obsolete]` lines, plus
  added/removed files, `Styles/`, `Themes/`, `Services/`, `Colors/`,
  csproj/install docs. Everything else was internal refactoring, BOM removal,
  render-performance work, or razor markup/ARIA output.
- Many ARIA/accessibility improvements (v9.10.0) and render performance work
  (v9.11.0: "median component renders 31% less vs v9.8.0") — no API impact.

## v9.7.0 → v9.8.0 changes worth knowing

- Breaking changes traced to source: `MudInput`/`MudMask` no longer apply the
  user `Class` to the input adornment; `MudSwitch` no longer applies the label
  class to its text; `MudNavLink` now forwards user attributes to the anchor
  element; `MudDrawer`/`MudDataGrid`/`MudTable` changes below. None required
  prose edits — no hand-written file asserted the old behavior.
- `MudTableBase.AriaLabel` is now `[Obsolete]` in favor of the new
  `TableAttributes` parameter (also added to `MudDataGrid<T>`), reflected in
  `api/Table.md` and `api/DataGrid.md`.
- `DrawerVariant.Mini` now behaves like `Temporary` below its `Breakpoint`
  (was previously always mini-width); reflected in `enums.md` and
  `api/Drawer.md`.
- `IDialogService.ShowAsync<TComponent>` gained title-less
  `(DialogOptions options)` and `(DialogParameters parameters, DialogOptions options)`
  overloads (plus the `Type component` equivalents) — updated by hand in
  `services.md` since that file isn't mechanically generated.
- New parameters worth knowing: `MudDatePicker`/date-picker base
  `ShowAdjacentMonthDays`; `MudNavMenu` `MultiExpansion`; `MudNavLink` `Rel`;
  `MudStepper` `ActionsClass`; `MudFab` `Variant` (adds `Filled`/`Text`/`Outlined`);
  `MudPagination` `BoundaryCount` can now be `0`; `DataGridEditMode` gained
  `Inline`.
- A large number of component/base-class/enum XML doc **summaries** were
  reworded in source for this release (confirmed against
  `src/MudBlazor/Components/Button/MudButton.razor.cs` and others) — not a
  behavior change, just improved doc text now reflected in `api/*.md`,
  `components-index.md`, and `enums.md`.

## Known caveats of the extraction

- Parameter tables list each class's **own** parameters; inherited ones live in
  the base class's table (`api/_base-classes.md` for `MudComponentBase`,
  `MudBaseInput<T>`, etc., or the parent component's section). Always check the
  `: BaseClass` in the heading.
- `[CascadingParameter]`s and public methods are not tabulated. For public
  methods (e.g. `MudForm.Validate()`, `MudThemeProvider.GetSystemDarkModeAsync()`)
  check the component source if unsure.
- Multi-line property declarations may drop the default value (rare; the
  "Defaults to …" remark text usually still captures it).

- `MudFormComponent.Validation` is `<inheritdoc/>` in v9.11.0, so the script
  extracts an empty summary; the v9.8.0 text was restored by hand in
  `api/_base-classes.md` — re-apply after regenerating.

## What to re-check on each MudBlazor release

1. Re-run `extract_api.py` against the new tag; diff `api/`, `enums.md`,
   `components-index.md`.
2. Breakpoint values / new breakpoints in `_variables.scss`.
3. Palette/typography/layout defaults in `Themes/Models/*`.
4. New or changed utility classes in `Styles/utilities`.
5. `AddMudServices` chain and service interface signatures.
6. Release notes at https://github.com/MudBlazor/MudBlazor/releases for
   breaking changes worth surfacing in the writer's guidance.
