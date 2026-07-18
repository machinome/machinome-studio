# solid-node-shop

This checkout is two things at once:

1. **The plugin source** — the shop's skills, agent role cards, and
   workspace scripts are versioned here. Editing them IS developing
   the next shop version.
2. **A live workspace** — the framework working copy at `solid-node/`
   (untracked), benches at `WTs/`, projects at `projects/<name>`
   (each its OWN git repository, untracked here).

## Working here directly (plugin not installed)

The installed plugin normally wires the shop up; from this checkout,
wire it by hand:

- **To run the shop** — start or advance a CAD project — read
  `skills/running-the-shop/SKILL.md` FIRST and follow it: it is the
  foreman's loop (design → ratify → build → judge → bank). The
  machinist's craft manual is `skills/solid-node/SKILL.md`. The
  specialists are defined by the role cards under `agents/`.
- **Dispatching a specialist**: the plugin's named agent types
  (`solid-node-shop:<name>`) do not exist here. Dispatch a
  general-purpose subagent whose prompt carries, verbatim, the role
  card body (`agents/<role>.md`, below the frontmatter) plus every
  skill its frontmatter names (`skills: [solid-node]` → include
  `skills/solid-node/SKILL.md` in the prompt). The card's rules bind
  exactly as if the plugin had loaded them — including its STOP-and-
  report refusals. Honor the card's `model:` field when dispatching.
- `/file-a-wart` is `skills/file-a-wart/SKILL.md`.

## The repo boundary (never skip)

Project work commits to the project's own repo; framework work
commits to a framework working copy; shop work commits here. Before
EVERY dispatch that writes into a project:

    git -C <project> rev-parse --show-toplevel   # must print <project> itself

If an enclosing repository answers, the project is mis-homed — stop
and fix the homing first. Never commit a project into this repo or
into the framework repo.

## Workspace mechanics

- Bootstrap: `scripts/setup` (tier 1: pip install) or
  `scripts/setup dev [ref]` (tier 2: framework clone at
  `solid-node/`, latest release tag by default — the framework
  version is the pilot's choice and is NOT pinned by this repo).
- Venv: `.venv/` — the CLI is `.venv/bin/solid`.
- Framework benches: `scripts/dev-env <name> setup|teardown` →
  worktrees at `WTs/<name>` with per-slot ports; run from inside a
  bench so its `.env` is picked up, and use `PYTHONPATH="$PWD"` with
  the workspace venv to run the bench's own code.
- Projects: `git init` a new project at `projects/<name>` and commit
  its scaffold before the first dispatch.

## Developing the shop itself

Shop changes (skills, role cards, scripts, governance) are ordinary
commits in this repo — one commit per coherent change. Lessons about
the craft belong in the skills, not in this file: this file only
bootstraps a session; the skills are the product.
