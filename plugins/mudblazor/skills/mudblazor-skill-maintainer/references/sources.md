# Canonical MudBlazor sources

Repo: https://github.com/MudBlazor/MudBlazor · Docs site: https://mudblazor.com
· Default branch: `dev` — **but always work from the latest release tag**
(`vX.Y.Z`), which is what the writer skill documents.

**Source code is authoritative. The docs site and release notes are secondary.**

## Release / version

- Latest release (API): https://api.github.com/repos/MudBlazor/MudBlazor/releases/latest
  → `tag_name`, `published_at`, `body` (release notes).
- All releases (for walking baseline→current):
  https://api.github.com/repos/MudBlazor/MudBlazor/releases
- Releases page: https://github.com/MudBlazor/MudBlazor/releases

## Source anchors (paths under `src/MudBlazor/` unless noted)

| Path | Confirms | Writer file |
|---|---|---|
| `Components/**/*.razor.cs` + razor-only `Mud*.razor`, `Base/*.cs` | every `[Parameter]`: name, type, default, XML docs, inheritance | `api/*.md`, `components-index.md` (via `scripts/extract_api.py`) |
| `Enums/*.cs`, plus enums in `Components/`, `Services/`, `Utilities/` | enum values + `[Description]` CSS names | `enums.md` (via script) |
| `Themes/MudTheme.cs`, `Themes/Models/{Palette,PaletteDark,Typography,LayoutProperties,Z-Index,Shadow,Breakpoints}.cs` | theme structure and every default value | `theming.md` |
| `Styles/abstracts/_variables.scss` | breakpoint px values, `$mud-palette-colors` | `layout-and-breakpoints.md`, `css-utilities.md` |
| `Styles/utilities/**/*.scss` | utility class families and value maps (spacing, flex, gap, borders, display, overflow, z, cursor…) | `css-utilities.md` |
| `Styles/abstracts/_colors.scss`, `Styles/core/_colors.scss` | theme color classes (`mud-*`), Material color classes (`red-text text-darken-2`) | `css-utilities.md` |
| `Styles/core/_elevation.scss`, `Styles/components/_typography.scss` | elevation range, `mud-typography-*` classes | `css-utilities.md` |
| `Styles/**` grep for `--mud-` | emitted CSS variable names | `theming.md` |
| `Extensions/ServiceCollectionExtensions.cs` | `AddMudServices` chain and per-feature `AddMud*` extensions | `getting-started.md`, `services.md` |
| `Services/Dialog/{IDialogService,DialogOptions}.cs` | dialog service API | `services.md` |
| `Components/Snackbar/SnackbarService.cs` | `ISnackbar.Add` overloads | `services.md` |
| `Services/Browser/IBrowserViewportService.cs`, `Services/Browser/Breakpoint.cs` | viewport service, Breakpoint enum | `services.md`, `layout-and-breakpoints.md` |
| `Services/MudGlobal.cs` | global defaults groups | `services.md` |
| `Icons/Material/*.cs`, `Icons/Custom/*.cs` | icon classes + `public const string` counts | `icons-and-colors.md` |
| `Colors/Colors.cs` | Material color constants and shade names | `icons-and-colors.md` |
| `src/MudBlazor.Docs/Pages/Getting Started/Installation/ManualMarkdown/*` | official install wiring (css/js includes, providers) | `getting-started.md` |

## Method notes

- The parameter surface is ~1,800 entries; never diff it by reading — run
  `scripts/extract_api.py` and use `git diff` on the writer skill.
- Some components omit `public` on the code-behind partial, and a few
  (`MudContainer`, `MudSpacer`, `MudRender`) are razor-only with parameters in
  `@code {}` — the script handles both; keep that behavior when editing it.
- SCSS value maps (`$spacing-values`, `$border-radiuses`, `$cursors`,
  `$typography-types`, breakpoint loops) must be read exactly — a summarizer
  will drop entries.
- Docs-site pages correspond to `src/MudBlazor.Docs/Pages/**`; useful for
  human-readable feature descriptions, but treat every syntactic fact as
  unconfirmed until seen in `src/MudBlazor/`.
