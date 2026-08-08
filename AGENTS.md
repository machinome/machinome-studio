# SolidNode Studio: agent operating contract

This repository is the development entry point for the solid-node
ecosystem. It is both:

1. the source of the experimental `solid-node-studio` agent harness; and
2. a workspace in which the solid-node framework and independent
   mechanical projects are developed.

The shop is the harness for both kinds of work. Do not treat a checkout of
the solid-node framework as a separate development environment with its own
unrelated process.

## Current status

- `solid-node` is functional and is approaching its broadly usable v0.4
  release. Framework changes must preserve that level of usefulness.
- `solid-node-studio` is private and experimental. Its roles, prompts, and
  development disciplines are being exercised and revised before release.
- The public community-contribution workflow described by the shop is the
  intended direction, not a claim that it is already published or stable.
  At present the framework author is the only active framework developer and
  may explicitly choose a simpler direct-commit/direct-push path while the
  harness is being bootstrapped.
- An agent never infers permission to push, publish, open a PR, or contact a
  contributor. Do so only when the pilot explicitly asks.

Keep those facts accurate when changing documentation. Do not describe an
experimental capability as already portable or released.

## Why development starts here

solid-node is meant to evolve empirically from real mechanical work. A
framework requirement should normally begin as evidence from a project:
something a project needs, a workaround its agent had to learn, a contract the
framework cannot express, or a failure in an existing promise. The agents
working on that project carry the context needed to explain the requirement.

The intended chain is:

    mechanical project -> empirical finding -> framework requirement
    -> framework change -> validation in the originating project

This keeps framework design emergent and accountable to users rather than
invented in isolation. Explicit maintainer work such as release engineering,
maintenance, or a known conformance bug may start without a new project
finding, but it still starts through the shop so the same evidence and
repository discipline apply.

## Start every task in the right lane

### Mechanical project work

Mechanical work happens on a shop floor, and the repository agent's only part in
it is opening that floor with the parameters the pilot chose. Read
`skills/running-the-shop/SKILL.md` and run the one launcher command it
documents, selecting the runtime profile explicitly (`builder` for direct work
or `fordesmac` for the delegated pipeline) and the backend the pilot named.

Once the floor is open, the profile's own agents do the work and the pilot
steers them in the browser. The repository agent does not coordinate
specialists, dispatch assignments, relay broker messages, carry the project
thread, or machine parts. Do not paste role cards into an ad-hoc agent or
assemble a substitute pipeline in this conversation when a launch fails; report
the failure instead.

Runtime conduct is profile-owned and stated in each role's prompt under
`profiles/`, not here: the designer's document ownership and drawing-release
protocol, the machinist's evidence and commit discipline, the foreman's
dispatch and one-increment-ahead pipeline, and the provisional rule keeping
every runtime agent inside its active project. `shop-skills/solid-node-api/SKILL.md`
is the complete public contract and `shop-skills/solid-node/SKILL.md` is
machining craft; both are exposed to runtime agents through profile allowlists
and are not repository-agent reading.

In this workspace, every project lives at `projects/<name>/` as its own Git
repository, untracked by the shop. A shop installed as a plugin may operate on a
project elsewhere, but that project directory must still be its own repository
root. The launcher enforces this before any agent starts, and the runtime agents
re-verify it before writing; a reported open floor is evidence the gate passed.

### Framework work

Framework development also starts in this repository, normally from an
empirical finding surfaced by a project agent, but it is a separate discipline
from running the mechanical shop. Read `skills/framework-change/SKILL.md`
first for every framework mutation. Do not dispatch mechanical-project roles
to design or implement framework changes. Read the target framework checkout's
architecture, baseline specs, and relevant decisions before work.

Use an isolated framework worktree at `./solid-node/WTs/<name>/`; never make
framework changes in the primary `./solid-node/` checkout.

Framework cycles are standalone by default. A framework cycle belongs to an
active sprint only when the pilot explicitly includes it in that sprint's
ratified scope. It then branches from and integrates into the framework's
paired `sprint-NNN` integration line under the sprint and framework-change
protocols; unrelated framework maintenance remains standalone.

Framework work may inspect framework source because changing the framework is
its assignment. Keep the originating project, reproduction, or contract named
in the change so the requirement does not lose its empirical context.

OpenSpec changes, ratification, implementation, and archival are repository
workflows performed directly under the pilot's authority. During the current
private bootstrap, follow the pilot's explicit direction about which portions
to exercise. Never silently present an unratified interface as settled, and
never silently substitute a different design when implementation evidence
contradicts the proposed one.

All agent prompts and framework-development orchestration live in this shop.
Never read or rely on a framework-local `AGENTS.md`, assistant command, or
copied agent workflow as authority. The framework repository owns its source,
tests, OpenSpec records, architecture, and ADRs—not agent prompts.

Framework commits belong only to a solid-node repository or one of its
worktrees. Mechanical-project commits never do.

### Shop work

Changes to role cards, skills, plugin metadata, workspace scripts, and
governance belong to this repository. They change the harness itself, so check
their effect on both product work and framework work. Preserve assistant
portability: keep durable process in repository files and skills rather than
depending on one vendor's hidden state or conversation memory.

Perform shop changes in a dedicated worktree, leaving the pilot-controlled
primary checkout alone unless the pilot explicitly directs work there. Before
editing, assess whether the requested change requires an OpenSpec cycle. Use
OpenSpec whenever the pilot asks for it and normally for a new or changed
user-visible behavior, a story or sprint outcome, a consequential interface or
architecture decision, or work that needs ratification and durable behavioral
specs.

A narrow adjustment may proceed without OpenSpec when it preserves ratified
behavior and architecture—for example, a small correction, repository hygiene,
or an equivalent maintenance edit. This is a judgment exception, not a route
around proposal or ratification. If the classification is uncertain, the work
expands beyond the adjustment, or skipping OpenSpec could conceal a product or
architecture choice, stop before editing and confirm the direct path with the
pilot. Direct adjustments still use a correctly based worktree, focused commit,
proportionate validation, integration into the appropriate branch, and safe
worktree cleanup.

An active sprint does not make unrelated shop maintenance sprint-scoped. Use
the sprint workflow only when the work advances a story, outcome, or other
scope explicitly recorded in that sprint, or when the pilot labels it as sprint
work. Do not place an unrelated adjustment on a sprint branch merely because
`current.md` exists. When the pilot explicitly directs an edit in the primary
checkout, make the focused change and commit there instead of creating a shop
or sprint worktree.

### CAD library catalogue

`library/` is the shop's durable, evidence-backed catalogue of external reuse
candidates for supported CAD technologies. Its directory taxonomy identifies
the technology; its keywords identify what a maker is trying to build. A
librarian derives search terms from the design—physical components, mechanisms,
product categories, and manufacturing-relevant features such as `gear`,
`bearing`, `electronics-enclosure`, `threaded-hole`, `hinge`, or `pcb-mount`—
not from a backend or implementation detail.

Never use a backend, language, generic CAD concept, file format, or operation
as a catalogue keyword: `cadquery`, `openscad`, `jscad`, `solid2`, `python`,
`javascript`, `stl`, `step`, `geometry`, `utility`, `import`, and `export` are
not maker design intents. Each record names a canonical source and an explicit
license value; use `Unknown` when evidence is ambiguous rather than guessing.
The catalogue is an extensible research index, not a claim to enumerate all
open-source CAD libraries, an endorsement, a compatibility guarantee, or a
substitute for project-specific license, maintenance, geometry, manufacturing,
and safety review.

### Sprint, worktree, and OpenSpec/ADR cycle

Read `skills/sprint/SKILL.md` for any sprint-scoped work. The active sprint's
identity and ratified starting scope come from `docs/product/sprints/current.md`
on the pilot-controlled shop primary branch. Once its integration worktree
exists, the copy at the shop `sprint-NNN` head is the authoritative operational
record; the primary copy remains an intentionally older active-sprint marker
until final integration. A sprint always has shop branch and worktree
`sprint-NNN` and `WTs/sprint-NNN`. When ratified scope includes framework work,
it also has
framework branch and worktree `sprint-NNN` and
`solid-node/WTs/sprint-NNN`. The latter is linked at
`WTs/sprint-NNN/solid-node` inside the shop sprint worktree so combined
validation uses the exact paired integration content.

Each cycle branches from the current sprint integration head in the repository
that owns it and integrates only back into that repository. Framework cycle
benches use `scripts/dev-env sprint-NNN-<change> setup --base sprint-NNN`.
Dependencies between shop and framework cycles live in the sprint record and
gate integration. Every cycle worktree opens when proposal work begins and
contains the complete two-commit OpenSpec cycle:

1. propose, ratify, validate, and commit the planning artifacts; then
2. apply red-first, test, promote accepted ADRs, sync baseline specs, archive
   the OpenSpec change, and commit the completed implementation record.

After a cycle integrates, run relevant combined validation from the shop sprint
worktree against its linked framework sprint worktree and record both tested
content commits. A later commit changing only sprint evidence does not create a
new paired product state or invalidate that result. Shop-cycle opening evidence
travels in that cycle's planning commit so recording it cannot make the cycle
stale. An archived change is not integrated, and repository-local integration
is not paired validation. Never force-remove dirty worktrees or silently resolve
stale bases, broken links, dependency blockers, or divergence.

Archive only after every included cycle is integrated into the repository that
owns it or coherently deferred, no dependency remains unresolved, and combined
validation passes for the final paired content commits. The pilot controls integration of
each `sprint-NNN` into its intended primary branch. Remove the paired worktrees
only after both archived content commits and the shop archive commit are
verified there. Worktree removal
never implies permission to delete a branch, push, publish, or disturb
unrelated worktrees.

User stories and behavioral specs describe user-visible needs and outcomes,
not orchestration, transports, payload formats, blocking behavior, or other
implementation mechanisms. Spikes are design evidence: they can validate or
invalidate a design option, but they do not create requirements. If design or
implementation evidence conflicts with a ratified behavior, return the choice
to the pilot rather than silently changing the spec.

## Workspace and repository boundaries

- Resolve all relative workspace paths from the primary shop checkout; from a
  shop worktree, locate it through Git's common directory.
- Never inspect or use sibling repositories or their executables. If an
  expected path inside this workspace is absent, stop and report it.

The normal workspace layout is:

    solid-node-studio/        this repository: the harness
    solid-node/             ignored independent framework repository
    solid-node/WTs/<name>/  ignored framework worktrees
    WTs/<name>/             ignored shop worktrees
    projects/<name>/        ignored independent project repositories

Repository membership, not directory nesting, defines ownership. Before every
commit, run `git rev-parse --show-toplevel` in the target and confirm it is the
repository intended for that change. Never stage the ignored framework clone,
a project, generated CAD artifacts, or a worktree in the shop repository.

Preserve pre-existing dirty state and unrelated user files. In particular,
do not delete or absorb ignored projects, framework checkouts, worktrees, or
archives merely because the outer shop repository does not track them.

`README.md` describes the workspace mechanics in full: `scripts/setup` (tier 1
plain, tier 2 development clone at `solid-node/`), the workspace venv at
`.venv/` whose CLI is `.venv/bin/solid`, `scripts/dev-env <name> setup|teardown`
for per-slot framework benches, and `python -m floor.orchestrator <name>` for a
project floor. Run bench code from inside the bench so its `.env` is picked up,
with `PYTHONPATH="$PWD"` and the workspace venv. The shop does not pin a
framework version; that is the pilot's choice.

## Authority and durable state

- The human user is the pilot and design authority. Agents make and record
  reversible working assumptions; bring the pilot decisions that change
  purpose, major architecture, consequential interfaces, manufacturing or
  safety assumptions, or would risk substantial rework.
- `docs/design.md` and increment specs are a mechanical project's durable
  record. The designer owns them; released specs are committed and
  immutable while machining. The machinist owns project code and tests.
  Framework specs, change artifacts, ADRs, tests, and history are the
  framework's durable record. Skills and role cards are the shop's durable
  operating knowledge.
- Chat context is never the only record of a settled decision.
- Knob values are not design decisions. Parameter schemas, derived
  relationships, guards, interfaces, and observable behavior are.
- Pixels are evidence for CAD work. A green suite does not replace snapshot
  inspection.
- Tests must prove the relevant failure red before the change turns them
  green. Report structural blind spots and environmental failures honestly.

## Assistant portability

The shop is intended to work from this checkout and eventually as a plugin or
equivalent package for Claude Code, Codex, and other assistants. Today those
surfaces are not equally mature.

This file is the single operating contract for every assistant. `CLAUDE.md`
imports it and adds only what is specific to Claude Code; it never restates or
overrides a rule from here. Keep it that way: a rule that applies to more than
one assistant belongs in this file.

Runtime agents exist only as sessions the launcher opens from a selected
profile. There is no fallback in which an assistant hand-assembles one by
pasting a role card and its skills into a general-purpose agent: that produces
an unversioned role with the wrong skills and no broker, and it silently
replaces the thing under evaluation. When a host cannot open the selected
profile through the persistent backend, stop and report the transport
limitation. Porting the shop to another assistant means giving it a real
launcher, not reproducing the roles in conversation.

Codex-native repository-development defaults live in `.codex/config.toml`.
Runtime model, effort, tool, prompt, and skill choices belong only to selected
profile declarations; never recreate global runtime role adapters.

## Architecture documentation

`docs/architecture-overview.md` is the reference architecture of the shop
as it stands — the document to read before proposing any change. The
Architecture Decision Records under `docs/adrs/` are deltas: each records a
single decision and its context. Their index is `docs/adrs/README.md`.

`docs/design/README.md`, together with the HTML prototypes in `docs/design/`,
is the reference design for the application. Treat its stated screens,
behaviour, and fidelity requirements as the source of truth for application UI
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
the system that exists. It is also not `AGENTS.md` — that file is the
operating contract (lanes, worktree discipline, OpenSpec, authority). This
file governs *how to work*; the overview governs *what the system is*.

## Useful entry points

- `README.md` — product and workspace overview.
- `CLAUDE.md` — imports this contract; adds Claude Code specifics.
- `docs/architecture-overview.md` — reference architecture; read before proposing any change.
- `docs/design/README.md` — reference design for the application.
- `docs/adrs/README.md` — index of architecture decision records.
- `.codex/` — Codex repository-development defaults.
- `skills/sprint/SKILL.md` — sprint state, branching, integration, and
  worktree lifecycle.
- `skills/framework-change/SKILL.md` — standalone or sprint-scoped framework
  proposal, ratification, implementation, integration, and cleanup.
- `skills/running-the-shop/SKILL.md` — opening a floor: launcher command,
  project/profile/backend parameters, and launch failures.
- `profiles/` — trusted runtime topology, prompts, and allowlisted skills.
- `shop-skills/` — shared runtime API and machining skills.
- `docs/product/stories/` — pilot-authored inputs to shop OpenSpec changes.
- `scripts/setup` — plain or development workspace bootstrap.
- `scripts/dev-env` — isolated framework worktree benches.
- `governance/` — proposed public contribution templates; experimental until
  the contribution workflow is published.
