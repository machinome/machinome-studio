# SolidNode Studio — Claude Code entry point

Read [AGENTS.md](./AGENTS.md) as the shared operating contract. This file adds
only Claude-specific dispatch guidance.

For a mechanical project, the operator selects a trusted runtime profile when
opening the floor: `builder` is direct one-agent work and `fordesmac` is the
delegated four-agent pipeline. Runtime prompts, backend choices, and allowed
skills are resolved from project configuration plus trusted profile data under
`profiles/`; do not substitute `agents/*.md`,
`.codex/agents/`, or repository `skills/` paths.

If a host cannot launch the selected profile through the persistent backend,
stop and report the transport limitation. Do not paste global role cards or
expand a runtime agent's skills from repository-development instructions.

## Slash commands

- `/file-a-wart` — `skills/file-a-wart/SKILL.md`.
