# Machinome Studio: agent operating contract

This repository is the development entry point for the machinome
ecosystem. It is both:

1. the source of the experimental `machinome-studio` agent harness; and
2. a workspace in which the machinome framework and independent
   mechanical projects are developed.

The shop is the harness for both kinds of work. Do not treat a checkout of
the machinome framework as a separate development environment with its own
unrelated process.

## Current status

- `machinome` is released: the last published version is 0.6.0, on PyPI
  under the old name `solid-node` (1 September 2026), the release that
  makes a model a machine. Its main branch holds Machinome 0.7.0 at
  released state, dated 23 September 2026 in its records: the rename, the
  declarative node API, the motion layer, running and clocked machines,
  the 22 September source-timing correction that makes running exports
  declare document version 11, the 23 September `Follow` law between
  two moving surfaces, whose exports declare version 12, and the
  23 September finite profile contact inside a running `Bound`, whose
  exports declare version 13. It is tagged `v0.7.0` locally; the tag is
  not pushed and nothing is uploaded. `docs/v0.7.0-checklist.md` lists
  what publication still needs. Framework changes must preserve that level of usefulness.
- `molejo`, the analytic flexible-parts library born from a machinome
  flexible-leaf finding, is released and public: 0.2.0 on PyPI and on npm,
  with its manual at <https://molejo.readthedocs.io>. Its main branch holds
  0.2.1, which caps the `brep` extra below OCP 8, prepared and not yet
  pushed or uploaded. Like the framework it is genuinely published, and its
  claims are held to that standard (see "molejo library work").
- `machinome-viewer`, the browser viewer for machinome models, has just
  left the framework to become an independent AGPL-3.0-only repository and
  package, installed through the framework's `viewer` extra and reached only
  as a separate process. Version 0.7.0, numbered with the framework and
  declaring viewer API 26 and document versions 1 to 13, is at released
  state in its records and tagged `v0.7.0` locally; the tag is not pushed
  and it is not uploaded to any index (see "machinome-viewer work"). Do
  not describe it as published.
- `machinome-studio` is private and experimental. Its roles, prompts, and
  development disciplines are being exercised and revised before release.
- The public community-contribution workflow described by the shop is the
  intended direction, not a claim that it is already published or stable.
  At present the framework author is the only active framework developer and
  may explicitly choose a simpler direct-commit/direct-push path while the
  harness is being bootstrapped.
- The studio concept is proven, but its packaging is limited: it runs on
  Linux against Claude Code or opencode backends and is still hacky to set
  up. Delivering the studio experience to an average maker in the browser,
  on their existing assistant subscription, is under active exploration in
  three independent prototype repositories (see "Browser delivery
  prototypes"). No delivery architecture has been chosen.
- `machinome.org`, the public website for the whole ecosystem, is an
  independent AGPL-3.0-only repository beside this one. Its first
  pre-release build was completed on 21 September 2026 through five archived
  OpenSpec changes: a Python generator, Home, the Foundry (14 of 17 launch
  projects, none reviewed), the Software roster with four hosted manuals
  (only molejo genuinely released; the rest rehearse the 0.7 release set),
  the empty Articles and Videos sections, the four About pages and the
  updates stream. The build is made in pre-release mode, which its publish
  command refuses to upload. Nothing is published and no site is live at
  any address (see "machinome.org site work").
- An agent never infers permission to push, publish, open a PR, or contact a
  contributor. Do so only when the pilot explicitly asks.

Keep those facts accurate when changing documentation. Do not describe an
experimental capability as already portable or released.

## Why development starts here

machinome is meant to evolve empirically from real mechanical work. A
framework requirement should normally begin as evidence from a project:
something a project needs, a workaround its builder had to learn, a contract
the framework cannot express, or a failure in an existing promise. Whoever
worked that project — a floor agent or this conversation — carries the context
needed to explain the requirement.

The intended chain is:

    mechanical project -> empirical finding -> framework requirement
    -> framework change -> validation in the originating project

This keeps framework design emergent and accountable to users rather than
invented in isolation. Explicit maintainer work such as release engineering,
maintenance, or a known conformance bug may start without a new project
finding, but it still starts in this repository so the same evidence and
repository discipline apply.

**Every feature needs empirical evidence.** A feature, a spelling, a new
declaration, a document field, or a viewer capability is proposed only when
a named project needs it now, and the proposal names the project, the finding
and what the project does with the result. Nothing is built for a use nobody
has: not to complete a table whose squares look asymmetric, not to make a
decomposition "honest", not for a machine someone might write later, not
because a plan listed it. Design symmetry is not evidence and a plan is not
evidence; a campaign plan inherited from an earlier agent is re-checked cycle
by cycle, and a cycle with no originating finding is struck before it is
proposed, not executed because it was ordered. A change whose own record says
the originating project "is owed nothing, and gets nothing" is the shape this
rule forbids. If a genuine requirement seems to need speculative groundwork,
bring the pilot the requirement and the smallest change that serves it, and
let the pilot decide whether the groundwork is wanted.

## Start every task in the right lane

### Mechanical project work

Mechanical work happens in one of two lanes, and the pilot chooses by where
they ask. Asked on the shop floor, the work belongs to that project's profile
agents. Asked here, the repository agent does it directly in the project's own
repository. Neither lane is a fallback for the other: a failed launch is not
permission to imitate the floor in conversation, and direct work is not a
reason to leave the floor unopened when the pilot asked for it.

**On the shop floor.** When the pilot asks for the shop, the repository agent's
only part is opening the project hub. Read `skills/running-the-shop/SKILL.md`
and run the one launcher command it documents. The launcher requires the exact
external `--projects-dir` catalogue but takes no project and no profile; the
pilot chooses or creates a project in the browser. It never derives runtime
paths from a Git checkout or process cwd. An existing project's `profile`
declaration selects its roster, with `fordesmac` as the fallback, and creation
records the profile the pilot chooses. Per-agent backend, provider, model, and
reasoning selections come from the project's `pyproject.toml`; the launcher
accepts no runtime override.

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
every runtime agent inside its active project.

**Directly from this conversation.** When the pilot asks for project work here,
do it. Design, model, test, inspect, and commit inside that project's own Git
repository, under the project's own records — its design documents, specs, and
history. The craft and the evidence discipline are the same in both lanes:
`shop-skills/machinome-api/SKILL.md` is the complete public contract and
`shop-skills/machinome/SKILL.md` is machining craft, exposed to runtime agents
through profile allowlists and read by the repository agent when it machines a
project directly. Pixels remain evidence, tests still prove the failure red
first, and the pilot remains the design authority. Giving an existing
open-source project a simulation layer is the recurring shape of this work,
and `skills/simulate-project/SKILL.md` is its procedure: the thin
`simulation/` package, the control surface sized to the machine, the small
demo set, and the project-owned OpenSpec record.

Direct project work is not shop work: nothing about a project is staged or
committed in the shop repository, and the shop's worktree, sprint, and OpenSpec
machinery does not govern it. A project may keep its own OpenSpec records under
its own repository when the pilot wants them. An empirical finding is worth the
same whichever lane produced it, and still becomes a framework requirement
through `skills/framework-change/SKILL.md`.

Every project lives at `<projects-dir>/<name>/` as its own Git repository,
untracked by the shop. In this development workspace the normal explicit
catalogue is the primary workspace's `projects/` directory; an installed shop
may use an arbitrary unrelated catalogue and requires no shop Git checkout.
The project-open operation enforces the project repository boundary before any
agent starts, and the runtime agents re-verify it before writing; a project
shown as open is evidence the gate passed. Working directly, the repository
agent is its own gate: confirm `git rev-parse --show-toplevel` names that
project before writing or committing.

### Framework work

Framework development also starts in this repository, normally from an
empirical finding surfaced by project work, but it is a separate discipline
from running the mechanical shop. Read `skills/framework-change/SKILL.md`
first for every framework mutation. Do not dispatch mechanical-project roles
to design or implement framework changes. Read the target framework checkout's
architecture, baseline specs, and relevant decisions before work.

Use an isolated framework worktree at `./machinome/WTs/<name>/`; never make
framework changes in the primary `./machinome/` checkout.

The user manuals of the framework, the viewer and the mechanics package are
written and released under `skills/write-the-manual/SKILL.md`: the layout by
reader intent, release facts stated once, sibling links that exist, examples
on the public contract, and the tests that pin them. Read it before touching
a page a reader is sent to, in any of the three repositories.

Framework cycles are standalone by default. A framework cycle belongs to an
active sprint only when the pilot explicitly includes it in that sprint's
ratified scope. It then branches from and integrates into the framework's
paired `sprint-NNN` integration line under the sprint and framework-change
protocols; unrelated framework maintenance remains standalone.

Framework work may inspect framework source because changing the framework is
its assignment. Keep the originating project, reproduction, or contract named
in the change so the requirement does not lose its empirical context.

Not every piece of framework thinking is an OpenSpec artifact. The framework
repository's `workflow/` directory is its pre-spec working record: `warts.md`
is the running log of findings and their ratified triage, `workflow/docs/`
holds the provisional plan a change is later cut from, and `workflow/archive/`
keeps finished campaigns — audits, due diligences, remediation programmes —
with their reports and raw evidence. Record a finding there when a project
produces one, and work a plan out there before proposing, so a settled
direction does not live only in a conversation. Read
`machinome/workflow/README.md` for its conventions. Nothing in `workflow/` is
ratified: it is evidence and intent, never authority over a baseline spec or an
accepted ADR, and it is framework material committed to the framework
repository, never staged in the shop.

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

Framework commits belong only to a machinome repository or one of its
worktrees. Mechanical-project commits never do.

The browser viewer is not framework source. machinome is Apache-2.0 and
complete without it: `machinome develop` opens OpenSCAD when the viewer package
is absent, and the commands that need the browser viewer name the `viewer`
extra. A framework change that needs the viewer to change is two changes in
two repositories, and nothing of the viewer's code may be moved into the
framework; see "machinome-viewer work".

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

### molejo library work

`molejo/` is an ignored, independent Git repository
(<https://github.com/LibreSolid/molejo>) holding molejo: an analytic
representation for the flexible parts of a machine — valve springs, timing
belts, cable looms, filament — parts whose shape is a function of machine
state rather than only of their placement. A molejo shape is a serializable
spec; the Python package authors and evaluates it to meshes, STL, and
optionally exact OCCT solids, and the JavaScript package evaluates the same
spec to three.js buffers at frame rate, the two pinned to each other by
shared parity fixtures.

molejo was born from a machinome flexible-leaf finding and is the
flexible-part technology machinome adapts, but it is its own product:
independently consumable by any Python or three.js project, and depending on
nothing else in this workspace. Do not treat it as part of the framework, and
do not fold a molejo change into a framework cycle.

Like machinome, molejo is released: version 0.2.0 implementing spec
version `"0.2"`, on PyPI and on npm, with the manual at
<https://molejo.readthedocs.io>; 0.2.1, the same spec with the `brep`
extra capped below OCP 8, is prepared on its main branch and awaits the
pilot's upload. Both packages carry the spec version they
implement and release together for it; neither runtime is ever published
against a spec version the other has not caught up to. Publishing is the
pilot's explicit decision and never a side effect of building —
`molejo/scripts/check-dist` packs each package, installs it into a throwaway
environment outside the repository and evaluates a fixture there, and uploads
nothing.

Work on molejo happens inside that repository, under its own history, README,
changelog, and OpenSpec records at `molejo/openspec/` — not through the shop's
worktree or sprint machinery, and never staged in the shop repository. Read
`molejo/README.md` and `molejo/CHANGELOG.md` before working there, and keep
their status claims as honest as this file's: a released capability is one the
published version actually has, with the recorded gaps.

### machinome-viewer work

`machinome-viewer/` is an ignored, independent Git repository
(<https://github.com/machinome/machinome-viewer>) holding the browser
viewer for machinome models: the embeddable three.js widget with its
driver controls and molejo evaluation, the standalone export page, the
development server `machinome develop` launches, and the headless capture behind
`machinome snapshot --renderer web`. It is licensed AGPL-3.0-only, where the
framework is Apache-2.0, and that difference is why it is a separate
package: the framework installs it as its optional `viewer` extra, finds it
through one entry point, and runs it as a separate process; neither package
imports the other. The shop floor serves the bundle that package carries,
still obtained through the framework's `machinome viewer` report.

The viewer is the framework's viewer and nothing else's dependency, but it
is its own product with its own history, README, changelog, OpenSpec records
at `machinome-viewer/openspec/` and decision log at
`machinome-viewer/workflow/adrs/` (the viewer-owned ADRs relocated from the
framework under their original numbers). Work on it happens inside that
repository — not through the shop's worktree or sprint machinery, never
staged in the shop repository, and never folded into a framework cycle. A
change that spans both packages is one change in each, and the contract
between them — the `machinome.viewer` entry point and the
`machinome-viewer describe|serve|capture` commands — is specified on both
sides. Read `machinome-viewer/README.md` and `machinome-viewer/CHANGELOG.md`
before working there, and keep their status claims honest: 0.7.0 is at
released state, not yet published; `scripts/check-dist` there builds and smokes the
distributions and uploads nothing, and publishing is the pilot's explicit
decision.

### machinome.org site work

`machinome.org/` is an ignored, independent Git repository holding the public
website for the whole machinome ecosystem: the Foundry of reconstructed
machines, the software packages with their complete hosted manuals, Luis's
articles, the videos, and the standing pages recording the people, the
credits, the licensing policy and how AI was used.

It is licensed AGPL-3.0-only, copyright Luis Henrique Cassis Fagundes, as
this shop is. It is its own product. Its editorial authority is its own
`docs/editorial-spine.md` and `docs/guiding-specs.md`, its visual design is
its own `docs/design/`, and its work runs through its own OpenSpec records at
`machinome.org/openspec/` — not through the shop's worktree or sprint
machinery, and never staged in the shop repository. It depends on nothing
else in the workspace at build time except the artifacts other repositories
publish: viewer exports, model previews, package manuals, and the facts a
project's `CREDITS` and `NOTICE` record. Nothing in the shop depends on it.

The site restates nothing it does not own. A manual's text belongs to its
package, a project's credits belong to the project's records, and a
correction is made upstream and arrives with the next build. Read
`machinome.org/README.md` and `machinome.org/docs/roadmap.md` before working
there, and keep its status claims as honest as this file's: a pre-release
build is a pre-release build, not a published site, and publication — the
launch set, the domain, the hosting account, the announcement and the e-mail
to project authors — is the pilot's explicit decision and never a side effect
of a green build.

The site publishes other people's work under other people's licences beside
machine-written text. Its editorial law is therefore binding, not stylistic:
status honesty, reconstruction honesty, AI disclosure, credits compiled and
never inferred, the three licence words with held projects never listed, no
safety or security claims, and no positioning. Its own `README.md` states
them.

Its content model carries part of that law structurally, and an agent
writing content there follows it: prose is Markdown and facts are YAML, with
no prose field in any record; a Markdown file is written by a person or by a
model, never both; a machine-written file ends `.ai.md` and sits beside the
human-written prose of the same thing, carrying its model, generation date
and review date. Never write a sentence into a record, and never put
machine-written text in a plain `.md`.

### Browser delivery prototypes

`browser-engine/`, `mcp-server/`, and `browser-plugin/` are three ignored,
independent Git repositories prototyping browser delivery of the studio
experience: a maker chatting with a web assistant (claude.ai first; others
intended) installs a browser extension, the studio opens in a side panel next
to the conversation, and the assistant reaches the studio over MCP — no local
install, no API key, just the maker's existing assistant subscription. Two
candidate architectures are being evaluated and neither is chosen: render all
CAD in Python inside the MCP server, or pack the machinome stack into the
browser with WebAssembly. That choice is the pilot's; prototype findings are
evidence for it, not requirements.

Each repository is a concept-proving spike:

- `browser-engine/` — CAD evaluation in the browser. Proved that CadQuery
  builds correct geometry in headless Chromium via Pyodide/WebAssembly, with
  volume matching native CadQuery; peak memory on mid-range hardware and a
  non-Chromium browser matrix remain unmeasured. Carries its own OpenSpec
  records under `browser-engine/openspec/`.
- `mcp-server/` — the MCP server. Proved a hello-world interactive widget
  over MCP Apps (SEP-1865), but that route looks like a dead end for the
  studio panel: Apps rendering on Claude web custom connectors is unreliable,
  and an in-transcript widget is not the docked studio surface. The browser
  plugin is the current direction for the panel; the server remains the MCP
  transport the assistant talks to.
- `browser-plugin/` — the browser extension. Proved a side panel that opens
  beside claude.ai in Chrome and Firefox and stays sticky to the tabs the
  user opted in.

Each prototype is its own product with its own history, README, and process;
work on one happens inside that repository, not through the shop's worktree
or sprint machinery, and is never staged in the shop repository. They depend
on nothing else in this workspace and nothing in the shop depends on them.
Read each repository's `README.md` before working there, and keep its status
claims as honest as this file's: proven means proven for the recorded
environment, with the recorded gaps.

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
`machinome/WTs/sprint-NNN`. The latter is linked at
`WTs/sprint-NNN/machinome` inside the shop sprint worktree so combined
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

- For repository-development operations only, resolve relative workspace paths
  from the primary shop checkout; from a shop worktree, locate it through Git's
  common directory. This is not runtime discovery: both floor entry points use
  the caller's required `--projects-dir`, and loaded package resources identify
  the running shop implementation.
- Never inspect or use sibling repositories or their executables. If an
  expected path inside this workspace is absent, stop and report it.
- On a collaborator's machine the workspace is built, not inherited:
  `docs/collaborator-setup.md` says which repositories to clone where, which
  are private, which exist only on the pilot's machine, and how a fresh clone
  may lag the status above. An agent in a workspace that lacks
  `machinome/`, `machinome-viewer/` or `.venv/` follows it before any other
  work.

The normal workspace layout is:

    machinome-studio/        this repository: the harness
    machinome/             ignored independent framework repository
    machinome/WTs/<name>/  ignored framework worktrees
    WTs/<name>/             ignored shop worktrees
    projects/<name>/        ignored independent project repositories
    molejo/                 ignored independent published library repository
    machinome-viewer/      ignored independent viewer repository (AGPL)
    machinome.org/          ignored independent public website repository
    browser-engine/         ignored independent browser-delivery prototype
    mcp-server/             ignored independent browser-delivery prototype
    browser-plugin/         ignored independent browser-delivery prototype

Repository membership, not directory nesting, defines ownership. Before every
commit, run `git rev-parse --show-toplevel` in the target and confirm it is the
repository intended for that change. Never stage the ignored framework clone,
a project, the molejo repository, the viewer repository, the machinome.org
repository, a browser-delivery prototype, generated CAD artifacts, or a
worktree in the shop repository.

Preserve pre-existing dirty state and unrelated user files. In particular,
do not delete or absorb ignored projects, framework checkouts, the molejo
repository, the viewer repository, the machinome.org repository,
browser-delivery prototypes, worktrees, or archives merely because the outer
shop repository does not track them.

`README.md` describes the workspace mechanics in full: `scripts/setup` (tier 1
plain, installing `machinome[viewer]`; tier 2 development clones at
`machinome/` and `machinome-viewer/`), the workspace venv at
`.venv/` whose CLI is `.venv/bin/machinome`, `scripts/dev-env <name> setup|teardown`
for per-slot framework benches, and
`python -m floor.orchestrator --projects-dir <path>` for the project hub. Run
bench code from inside the bench so its `.env` is picked up,
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
  project/profile parameters, project-owned runtime selection, and launch failures.
- `skills/simulate-project/SKILL.md` — adding a machinome simulation layer
  to an existing open-source project directly from this conversation.
- `skills/write-the-manual/SKILL.md` — writing, revising and releasing the
  framework, viewer and mechanics user manuals without repeating the 0.7
  pass's defects.
- `profiles/` — trusted runtime topology, prompts, and allowlisted skills.
- `shop-skills/` — shared machinome API and machining skills: allowlisted to
  runtime agents, and read here when a project is built directly.
- `docs/product/stories/` — pilot-authored inputs to shop OpenSpec changes.
- `scripts/setup` — plain or development workspace bootstrap.
- `docs/collaborator-setup.md` — building the whole workspace, every
  repository included, on a collaborator's machine.
- `scripts/dev-env` — isolated framework worktree benches.
- `governance/` — proposed public contribution templates; experimental until
  the contribution workflow is published.
- `molejo/README.md` — independent published library repository for analytic
  flexible parts; see "molejo library work".
- `machinome/workflow/README.md` — the framework's pre-spec working record:
  findings (`warts.md`), provisional plans, and archived campaigns.
- `machinome-viewer/README.md` — independent AGPL viewer repository, the
  framework's `viewer` extra; see "machinome-viewer work".
- `machinome.org/README.md` — independent public website repository; its
  editorial spine, design proposal and roadmap; see "machinome.org site
  work".
- `browser-engine/README.md`, `mcp-server/README.md`,
  `browser-plugin/README.md` — independent browser-delivery prototype
  repositories; see "Browser delivery prototypes".
