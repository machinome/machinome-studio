# solid-node shop — Claude Code entry point

The operating contract is shared across assistants and lives in one
file. Read it as part of this one:

@AGENTS.md

Everything below is Claude-specific and adds to that contract; it never
overrides it.

## Dispatching a specialist from a direct checkout

When the shop is installed as a plugin, its named agent types
(`solid-node-shop:<name>`) do the dispatching. From this checkout they do
not exist, so wire a specialist by hand:

Dispatch a fresh general-purpose subagent whose prompt carries, exactly
once and verbatim, the role card body (`agents/<role>.md`, below the
frontmatter) plus every skill its frontmatter names (`skills:
[solid-node-api, solid-node]` means include both skill bodies in the
prompt). The card's rules bind exactly as if the plugin had loaded them —
including its STOP-and-report refusals. Honor the card's `model:` field
when dispatching. Do not also inherit a context containing those files.

Isolation still applies: never give a product agent files from another
project as reference, even when dispatching by hand.

**Do not use this fallback for Codex.** Codex loads the local named-agent
adapters under `.codex/agents/` through one app-server-owning
orchestrator; its concise delivery contains task-local paths and
evidence, not pasted role or skill bodies. The exact host protocol lives
in `skills/running-the-shop/SKILL.md`. Persistent Claude orchestration is
not yet implemented or claimed.

## Slash commands

- `/file-a-wart` — `skills/file-a-wart/SKILL.md`.
