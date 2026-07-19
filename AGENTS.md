# solid-node shop: agent operating contract

This repository is the development entry point for the solid-node
ecosystem. It is both:

1. the source of the experimental `solid-node-shop` agent harness; and
2. a workspace in which the solid-node framework and independent
   mechanical projects are developed.

The shop is the harness for both kinds of work. Do not treat a checkout of
the solid-node framework as a separate development environment with its own
unrelated process.

## Current status

- `solid-node` is functional and is approaching its broadly usable v0.4
  release. Framework changes must preserve that level of usefulness.
- `solid-node-shop` is private and experimental. Its roles, prompts, and
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

Read `skills/running-the-shop/SKILL.md` first and follow its pipelined product
loop. The main assistant is the foreman: it coordinates specialists and
consequential pilot decisions; it does not machine parts itself. The relevant
roles are under `agents/`. `skills/solid-node-api/SKILL.md` is the complete
public contract; `skills/solid-node/SKILL.md` is machinist craft.

The drawing office uses the public API and never inspects framework
implementation. The machinist starts from that API and may inspect narrowly
relevant framework source or tests to diagnose a concrete active-project
question. It may never modify the framework during product work, depend on a
private API, or treat a source scan as routine preparation.

While the shop is experimental, the foreman and product agents must not inspect
any other mechanical project for reference: no sibling, example, archived,
framework-example, or previously generated project files. Restrict evaluation
context to the active project and shop-provided skills. This provisional
isolation rule does not prevent the machinist's targeted framework diagnosis or
the librarian's use of an external library's own materials.

In this workspace, every project lives at `projects/<name>/` as its own Git
repository. A shop installed as a plugin may operate on a project elsewhere,
but that project directory must still be its own repository root. Before
dispatching any writer, verify:

    git -C projects/<name> rev-parse --show-toplevel

It must return that exact project directory.

### Framework work

Framework development also starts in this repository, normally from an
empirical finding surfaced by a project agent, but it is a separate discipline
from running the mechanical shop. Do not dispatch mechanical-project roles to
design or implement framework changes. Read the target framework checkout's
`AGENTS.md`, architecture, baseline specs, and relevant decisions before work.

Framework work may inspect framework source because changing the framework is
its assignment. Keep the originating project, reproduction, or contract named
in the change so the requirement does not lose its empirical context.

OpenSpec changes, ratification, implementation, and archival are repository
workflows performed directly under the pilot's authority. During the current
private bootstrap, follow the pilot's explicit direction about which portions
to exercise. Never silently present an unratified interface as settled, and
never silently substitute a different design when implementation evidence
contradicts the proposed one.

Framework commits belong only to a solid-node repository or one of its
worktrees. Mechanical-project commits never do.

### Shop work

Changes to role cards, skills, plugin metadata, workspace scripts, and
governance belong to this repository. They change the harness itself, so check
their effect on both product work and framework work. Preserve assistant
portability: keep durable process in repository files and skills rather than
depending on one vendor's hidden state or conversation memory.

Shop product development is story-first:

1. The pilot writes user stories in `docs/product/stories/`.
2. Select one story or a coherent group and use it as the input to an OpenSpec
   proposal.
3. Ratify the proposal's observable behavioral specs before settling its
   architecture.
4. Record consequential architectural choices as candidate decisions in the
   change's `design.md`, and ratify them before implementation.
5. After successful implementation, promote accepted decisions to permanent
   ADRs under `docs/adrs/` and archive the OpenSpec change into the baseline
   specs.

User stories and behavioral specs describe user-visible needs and outcomes,
not orchestration, transports, payload formats, blocking behavior, or other
implementation mechanisms. Spikes are design evidence: they can validate or
invalidate a design option, but they do not create requirements. If design or
implementation evidence conflicts with a ratified behavior, return the choice
to the pilot rather than silently changing the spec.

## Workspace and repository boundaries

The normal workspace layout is:

    solid-node-shop/        this repository: the harness
    solid-node/             ignored independent framework repository
    WTs/<name>/             ignored framework worktrees
    projects/<name>/        ignored independent project repositories

Repository membership, not directory nesting, defines ownership. Before every
commit, run `git rev-parse --show-toplevel` in the target and confirm it is the
repository intended for that change. Never stage the ignored framework clone,
a project, generated CAD artifacts, or a worktree in the shop repository.

Preserve pre-existing dirty state and unrelated user files. In particular,
do not delete or absorb ignored projects, framework checkouts, worktrees, or
archives merely because the outer shop repository does not track them.

## Authority and durable state

- The human user is the pilot and design authority. Agents make and record
  reversible working assumptions; bring the pilot decisions that change
  purpose, major architecture, consequential interfaces, manufacturing or
  safety assumptions, or would risk substantial rework.
- `docs/design.md` and increment specs are a mechanical project's durable
  record. The drawing office owns them; released specs are committed and
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

When a named plugin agent is unavailable, `CLAUDE.md` explains the direct
checkout fallback: dispatch a general-purpose agent with the complete role
card body and every skill named by its frontmatter. On assistants with a
different delegation mechanism, preserve the same role boundaries,
ratification points, repository checks, and evidence requirements rather than
pretending vendor-specific syntax is portable.

Codex-native model and role defaults live in `.codex/config.toml` and
`.codex/agents/*.toml`. The TOML definitions deliberately load the shared
Markdown role cards and skills instead of duplicating their operating
instructions. Keep those adapters aligned whenever a role is added or renamed.

## Useful entry points

- `README.md` — product and workspace overview.
- `CLAUDE.md` — direct-checkout bootstrap and dispatch fallback.
- `.codex/` — Codex foreman defaults and custom specialist agents.
- `skills/running-the-shop/SKILL.md` — foreman's mechanical-project loop.
- `skills/solid-node-api/SKILL.md` — complete stable public API.
- `skills/solid-node/SKILL.md` — machinist craft manual.
- `agents/` — specialist authority and stop conditions.
- `docs/product/stories/` — pilot-authored inputs to shop OpenSpec changes.
- `scripts/setup` — plain or development workspace bootstrap.
- `scripts/dev-env` — isolated framework worktree benches.
- `governance/` — proposed public contribution templates; experimental until
  the contribution workflow is published.
