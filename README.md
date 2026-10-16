# claude-plugins

My personal collection of [Claude Code](https://code.claude.com) plugins and [Agent Skills](https://agentskills.io/specification), published as a plugin marketplace. Use whatever is useful to you.

## Install

Add the marketplace, then install any plugin from it:

```bash
claude plugin marketplace add BillyCool/claude-plugins
claude plugin install <plugin>@billycool
```

For example, `claude plugin install mudblazor@billycool`. Inside a session, `/plugin` opens the same browser.

Skills are namespaced by plugin, e.g. `mudblazor:mudblazor-ui-writer`, and still trigger automatically from their descriptions. Plugins omit `version`, so they track commits. Run `/plugin marketplace update billycool` (or enable auto-update for the marketplace) to pick up new ones.

## Plugins

| Plugin | Skills | Purpose |
|--------|--------|---------|
| [`ublock-origin`](plugins/ublock-origin/) | `ublock-origin-filter-writer`, `ublock-origin-skill-maintainer` | Writes correct, minimal uBlock Origin filter rules (Firefox-focused); the maintainer keeps the writer in sync with new uBO releases. |
| [`violentmonkey`](plugins/violentmonkey/) | `violentmonkey-userscript-writer` | Writes correct, minimal Violentmonkey userscripts using the real GM_/GM.* API and the official `@violentmonkey/*` libraries. |
| [`mudblazor`](plugins/mudblazor/) | `mudblazor-ui-writer`, `mudblazor-skill-maintainer` | MudBlazor UI development backed by an offline, source-verified copy of the docs; the maintainer re-syncs it for new releases. |
| [`aimp`](plugins/aimp/) | `aimp-plugin-developer`, `aimp-sdk-skill-maintainer` | AIMP plugin development against an offline copy of the AIMP SDK; the maintainer regenerates it for new SDK releases. |

## Layout

```
.claude-plugin/marketplace.json     # marketplace "billycool"
plugins/<plugin>/
├── .claude-plugin/plugin.json
└── skills/<skill-name>/
    ├── SKILL.md
    ├── references/                 # on-demand knowledge files
    └── scripts/                    # optional
```

## Conventions

- Skill `name` matches its directory and follows the spec (lowercase, hyphens). `SKILL.md` stays under 500 lines, with detail in `references/`.
- A "writer" skill and its "maintainer" live in the same plugin. Maintainers edit their sibling writer via `../<writer>/`, so keep them together.
- Reference files are **sourced, not recalled**: documented syntax and APIs are confirmed against live source or the official SDK, not model memory.
- Run maintainer skills from a checkout of this repo, not from the installed plugin cache, since updates overwrite the cache.

## Local development

```bash
claude plugin validate .
claude plugin marketplace add /path/to/claude-plugins
```

A local marketplace is read in place, so edits apply on the next session or `/reload-plugins`.

## License

[MIT](LICENSE)
