# Machinome Studio: agent operating contract

This repository is Machinome Studio, the end-user product of the machinome
ecosystem: a local agent harness in which a maker builds mechanical CAD
projects with the machinome framework. It holds the floor runtime (the
`floor/` package: the hub, per-project sessions, the Claude, OpenCode and scoped Codex
backends and the browser frontend under `floor/frontend/`), the runtime
profiles under `profiles/`, the shared runtime skills under `shop-skills/`,
the tests, and the studio's own architecture, design, product and OpenSpec
records.

The studio is developed from the machinome workspace repository, beside the
framework and the other packages of the ecosystem. The workspace governs
framework development, cross-repository sprints, manuals and the rest of the
ecosystem's process. This file governs work inside this repository, whichever
checkout an agent is working in.

## Current status

- Machinome Studio 0.1.0 is experimental and unpublished. Its repository is
  public at <https://github.com/machinome/machinome-studio>; it is on no
  package index, and installing it means cloning that repository.
- It runs on Linux against Claude Code, OpenCode or qualified pinned Codex
  backends and is still
  hacky to set up. Do not describe it as released or portable.
- Its profiles, prompts and runtime disciplines are being exercised and
  revised before any release.
- Delivering the studio experience to a maker in the browser, on an existing
  assistant subscription, is being explored in separate prototype
  repositories. No delivery architecture has been chosen, and nothing in this
  repository depends on those prototypes.
- The framework `machinome` is Apache-2.0 and complete without the studio.
  The studio invokes the `machinome` command from its own Python environment
  and never imports framework internals. The browser viewer
  `machinome-viewer` (AGPL-3.0-or-later) is installed as the framework's
  `viewer` extra; the floor serves the bundle that package carries, obtained
  through `machinome viewer`, and refuses to open a project when no usable
  viewer is installed. Neither package is part of this repository.
- An agent never infers permission to push, publish, open a PR, or contact a
  contributor. Do so only when the pilot explicitly asks.

Keep those facts accurate when changing documentation. Do not describe an
experimental capability as already portable or released.

## Changing the studio

Changes to the floor, profiles, runtime skills, plugin metadata, scripts,
tests and records belong to this repository. They change the harness a maker
works in, so check their effect on the floor as the maker meets it. Keep
durable process in repository files rather than in one vendor's hidden state
or conversation memory.

### Worktrees

Perform changes in a dedicated worktree under `WTs/<name>/`, which is
ignored, leaving the pilot-controlled primary checkout alone unless the pilot
explicitly directs work there. A worktree branches from the head it will
integrate into. When the pilot directs an edit in the primary checkout, make
the focused change and commit there instead of creating a worktree.

Never force-remove a dirty worktree, and never silently resolve a stale base,
a broken link or divergence. Removing a worktree never implies permission to
delete a branch, push, publish, or disturb unrelated worktrees.

### When a change needs OpenSpec

Before editing, assess whether the change requires an OpenSpec cycle. Use
OpenSpec whenever the pilot asks for it, and normally for:

- a new or changed user-visible behaviour;
- a story or sprint outcome;
- a consequential interface or architecture decision; or
- work that needs ratification and durable behavioural specs.

A narrow adjustment may proceed without OpenSpec when it preserves ratified
behaviour and architecture: a small correction, repository hygiene, or an
equivalent maintenance edit. This is a judgment exception, not a route around
proposal or ratification. If the classification is uncertain, the work
expands beyond the adjustment, or skipping OpenSpec could conceal a product or
architecture choice, stop before editing and confirm the direct path with the
pilot. A direct adjustment still uses a correctly based worktree, a focused
commit, proportionate validation, integration into the appropriate branch,
and safe worktree cleanup.

### The OpenSpec cycle

The studio's specs and changes live under `openspec/`: baseline specs in
`openspec/specs/`, active changes in `openspec/changes/`, and finished changes
in `openspec/changes/archive/`. The cycle is run with the OpenSpec CLI
(`openspec`); use the subcommands it actually offers and read its own help
rather than inventing any.

Every cycle worktree opens when proposal work begins and carries the complete
two-commit cycle:

1. propose, ratify, validate, and commit the planning artifacts; then
2. apply red-first, test, promote accepted ADRs, sync baseline specs, archive
   the change, and commit the completed implementation record.

An archived change is not an integrated change. The cycle is finished when
its branch has been integrated into the branch it was cut from, and that
integration is the pilot's to direct.

Never silently present an unratified interface as settled, and never silently
substitute a different design when implementation evidence contradicts the
proposed one.

### Stories, specs and spikes

User stories and behavioural specs describe user-visible needs and outcomes,
not orchestration, transports, payload formats, blocking behaviour, or other
implementation mechanisms. Spikes are design evidence: they can validate or
invalidate a design option, but they do not create requirements. If design or
implementation evidence conflicts with a ratified behaviour, return the choice
to the pilot rather than silently changing the spec.

Pilot-authored stories live in `docs/product/stories/`; they are inputs to
OpenSpec changes, not specs themselves.

### Sprints

A cross-repository sprint is coordinated from the workspace's sprint record
and procedure, not from this repository. A studio cycle belongs to a sprint
only when the pilot includes it in that sprint's ratified scope; it then
branches from and integrates into this repository's `sprint-NNN` line, under
the workspace's sprint protocol. Unrelated maintenance is not sprint work,
even while a sprint is active: do not place an adjustment on a sprint branch
merely because a sprint exists.

## Every feature needs a need

A studio feature is proposed only when a maker, or a named project, needs it
now, and the proposal names who needs it, what they hit, and what they do with
the result. Nothing is built for a use nobody has: not to make a screen or a
table look symmetric, not for a maker who might appear later, not because a
plan listed it. Design symmetry is not evidence and a plan is not evidence;
a plan inherited from an earlier agent is re-checked before each change is
proposed. If a genuine need seems to require speculative groundwork, bring
the pilot the need and the smallest change that serves it, and let the pilot
decide whether the groundwork is wanted.

## Runtime conduct belongs to the profiles

The floor runs a project's work through the agents of its profile. Each
profile under `profiles/<id>/` declares its roster, prompts, allowlisted
skills, tool policy and safe runtime defaults; `builder` and `fordesmac` are
the profiles today. Runtime conduct is stated in each role's prompt there and
never here: the designer's document ownership and drawing-release protocol,
the machinist's evidence and commit discipline, the foreman's dispatch and
one-increment-ahead pipeline, the builder's own OpenSpec record, and the
provisional rule keeping every runtime agent inside its active project.

The profile's declared tool policy is the whole authority a runtime session
holds. No session runs with permission checking disabled, and a backend that
cannot enforce a profile-declared tool policy is not selectable.

`shop-skills/` holds the shared runtime skills the profiles allowlist through
symlinks: `shop-skills/machinome-api/SKILL.md` is the framework's complete
public contract and `shop-skills/machinome/SKILL.md` is machining craft. Here
they are runtime skills like any other. Framework-facing changes to them
arrive from the workspace's framework-change process when the framework's
public contract changes; a change made here must not contradict that
contract.

## Repository boundaries

- Every mechanical project lives at `<projects-dir>/<name>/` as its own Git
  repository. The catalogue path comes only from the launcher's
  `--projects-dir` option or the studio configuration file's `projects`
  key; the studio never derives it. Nothing about a project is ever staged
  or committed here.
- `floor/static/` (the generated frontend build), `docs/_build/` (the built
  manual), `node_modules/`, `.venv/`, `WTs/` and generated CAD artifacts are
  never staged.
- Before every commit, run `git rev-parse --show-toplevel` and confirm it
  names this repository.
- Preserve pre-existing dirty state and unrelated user files. Do not delete
  or absorb an ignored directory merely because this repository does not
  track it.
- Do not inspect or use sibling repositories or their executables as part of
  a studio change. The framework and the viewer are reached only through the
  installed `machinome` command.

## Authority and durable state

- The human user is the pilot and design authority. Agents make and record
  reversible working assumptions; bring the pilot decisions that change
  purpose, major architecture, consequential interfaces, manufacturing or
  safety assumptions, or would risk substantial rework.
- The studio's durable record is its baseline specs, OpenSpec changes, ADRs,
  architecture overview, design reference, tests and Git history. Profiles
  and runtime skills are its durable operating knowledge for runtime agents.
- Chat context is never the only record of a settled decision.
- Knob values are not design decisions. Parameter schemas, derived
  relationships, guards, interfaces, and observable behaviour are.
- Pixels are evidence for interface and CAD work. A green suite does not
  replace inspecting what the maker sees.
- Tests must prove the relevant failure red before the change turns them
  green. Report structural blind spots and environmental failures honestly.

## Assistant portability

The studio is intended to work from this checkout and eventually as a plugin
or equivalent package for Claude Code, Codex, and other assistants; its plugin
metadata is in `.claude-plugin/`. Today those surfaces are not equally mature.

This file is the single operating contract for every assistant working in
this repository. `CLAUDE.md` imports it and never restates or overrides a rule
from here; a rule that applies to more than one assistant belongs in this
file. Codex repository-development defaults live in `.codex/config.toml`.

Runtime agents exist only as sessions the floor opens from a selected
profile. There is no fallback in which an assistant hand-assembles one by
pasting a role prompt and its skills into a general-purpose agent: that
produces an unversioned role with the wrong skills and no broker, and it
silently replaces the thing under evaluation. When a host cannot open the
selected profile through the persistent backend, stop and report the
transport limitation. Porting the studio to another assistant means giving it
a real launcher, not reproducing the roles in conversation.

Runtime model, effort, tool, prompt, and skill choices belong only to profile
declarations and the project's own `[tool.machinome-studio]` table; never
recreate global runtime role adapters.

## Architecture documentation

`docs/architecture-overview.md` is the reference architecture of the studio
as it stands — the document to read before proposing any change. The
Architecture Decision Records under `docs/adrs/` are deltas: each records a
single decision and its context. Their index is `docs/adrs/README.md`.

`docs/design/README.md`, together with the HTML prototypes in `docs/design/`,
is the reference design for the application. Treat its stated screens,
behaviour, and fidelity requirements as the source of truth for interface
work.

- **Before proposing a change** — read the architecture overview and the
  relevant ADRs to understand the current boundaries and the reasoning behind
  them. A proposal that conflicts with an accepted decision must address the
  conflict explicitly.
- **After creating or accepting an ADR** — update the architecture overview
  so it reflects the new state. If the ADR changes an existing boundary,
  rewrite the affected section rather than appending a note; the overview is
  the reference, not a log.
- **After updating an ADR** — if the update changes the architecture, update
  the overview. A status change alone (`Accepted` → `Superseded by NNNN`) or
  a corrected date does not require an overview update.
- **The ADR index** — keep `docs/adrs/README.md` current: add new ADRs,
  update status fields, and preserve the table's chronological order.

The overview is not a design document, a proposal, or a spec. It describes
the system that exists. This file governs how to work; the overview governs
what the system is.

The user manual is separate from all of that: the `.rst` pages under
`docs/` (built with Sphinx; the Markdown records above are excluded from the
build), `README.md`, `CHANGELOG.md` and the `floor` package's docstrings.
It is written under the workspace's `write-the-manual` skill, and
`tests/test_documentation.py` holds its shape: release facts derived from
the package, the publication state on `docs/project/status.rst` only, no
project name, worktree or sibling checkout on a reader-facing page.
`workflow/` is the working record beside it: how the manual is built and
would be hosted, and archived history that is not for a reader.

## Useful entry points

- `README.md` — product overview, install, opening the hub, and the checks.
- `docs/index.rst` — the user manual; `workflow/documentation.md` says how
  it is built and checked.
- `CHANGELOG.md` — what the current source gives a maker.
- `docs/architecture-overview.md` — reference architecture; read before
  proposing any change.
- `docs/design/README.md` — reference design for the application, with its
  HTML prototypes.
- `docs/adrs/README.md` — index of architecture decision records.
- `docs/product/` — pilot-authored stories and the studio's sprint records.
- `profiles/` — runtime topology, prompts, tool policy and allowlisted
  skills.
- `shop-skills/` — the shared runtime skills the profiles allowlist.
- `openspec/` — baseline specs, active changes and the archive.
- `workflow/` — the working record: the manual's build and hosting notes,
  implementation notes and archived history.
- `scripts/setup` — creates `.venv/` and installs the studio and its
  runtime dependencies.
- `scripts/test-e2e` — builds the frontend and runs the end-to-end modules.
- `.claude-plugin/` — plugin metadata.
- `.codex/config.toml` — Codex repository-development defaults.
