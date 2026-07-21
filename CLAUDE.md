# solid-node-shop

This checkout is two things at once:

1. **The plugin source** — the shop's skills, agent role cards, and
   workspace scripts are versioned here. Editing them IS developing
   the next shop version.
2. **A live workspace** — the framework working copy at `solid-node/`
   (untracked), framework benches at `solid-node/WTs/`, shop worktrees at
   `WTs/`, and projects at `projects/<name>`
   (each its OWN git repository, untracked here).

## Working here directly (plugin not installed)

The installed plugin normally wires the shop up; from this checkout,
wire it by hand:

- **To run the shop** — start or advance a CAD project — read
  `skills/running-the-shop/SKILL.md` FIRST and follow it: it is the
  foreman's pipelined loop (brief → first release → concurrent design
  and machining → reconcile). The public contract is
  `skills/solid-node-api/SKILL.md`; machinist craft is
  `skills/solid-node/SKILL.md`. The specialists are defined by the
  role cards under `agents/`.
- **Dispatching a specialist from Claude Code**: the plugin's named agent types
  (`solid-node-shop:<name>`) do not exist here. Dispatch a
  fresh general-purpose subagent whose prompt carries, exactly once and
  verbatim, the role
  card body (`agents/<role>.md`, below the frontmatter) plus every
  skill its frontmatter names (`skills: [solid-node-api, solid-node]`
  means include both skills in the prompt). The card's rules bind
  exactly as if the plugin had loaded them — including its STOP-and-
  report refusals. Honor the card's `model:` field when dispatching. Do
  not also inherit a context containing those files.
- **Do not use that fallback for Codex.** Codex loads the local named-agent
  adapters under `.codex/agents/` through one app-server-owning orchestrator;
  its concise delivery contains task-local paths and evidence, not pasted role
  or skill bodies. The exact host protocol lives in
  `skills/running-the-shop/SKILL.md`. Persistent Claude orchestration is not yet
  implemented or claimed.
- During the current experimental evaluation, never give a product
  agent files from another project as reference. Follow the isolation
  rule in `skills/running-the-shop/SKILL.md` even when dispatching by
  hand.
- `/file-a-wart` is `skills/file-a-wart/SKILL.md`.
- **To change the framework** — read `skills/framework-change/SKILL.md` first.
  Every mutation uses a non-sprint OpenSpec cycle in a dedicated
  `solid-node/WTs/<change>` worktree. Agent prompts live here in the shop;
  never read or rely on a framework-local `AGENTS.md` or copied workflow.

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
  worktrees at `solid-node/WTs/<name>` with per-slot ports; run from inside a
  bench so its `.env` is picked up, and use `PYTHONPATH="$PWD"` with
  the workspace venv to run the bench's own code.
- Projects: open with `python -m floor.orchestrator <name>`. The launcher
  resolves only `projects/<name>`, creates and commits a missing `solid new`
  scaffold, validates an existing exact repository root, and completes
  `solid build root` before starting Floor or any role.

## Developing the shop itself

Shop changes (skills, role cards, scripts, governance) follow the shop's
worktree and, when applicable, sprint/OpenSpec protocol. Lessons about the
craft belong in the skills, not in this file: this file only bootstraps a
session; the skills are the product.
