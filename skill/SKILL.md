---
name: persona-spawn
description: Spawn subagents with personas from a local workspace library or the Emblem persona marketplace. Use when a task needs a different voice, expertise, or operating style; when the user says "use persona X", "spawn as Y", or "have a specific character do this"; when you need shared org context such as a foundation doc injected into every persona spawn; or when offloading a bounded task to a persona-preserving subagent is better than changing the current agent's own identity. Not for trivial tasks, changing your own persona in-place, or bypassing local subagent policy.
---

# Persona Spawn

Use this skill to ensure the local persona library exists, assemble a deterministic persona prompt, and spawn a subagent without letting workspace persona files override the requested persona.

## Files

Keep personas in the current workspace:

```text
<workspace>/personas/
├── config.json
├── index.json
├── the-mandalorian/
│   ├── SOUL.md
│   ├── IDENTITY.md
│   └── persona.json
└── <custom-persona>/
    ├── SOUL.md
    ├── IDENTITY.md
    └── persona.json
```

`personas/config.json` is the shared org-context config. Put docs there that every persona spawn should inherit, such as Kru foundation rules, brand standards, or execution rules.

Read `references/api-endpoints.md` only when importing or validating marketplace data.
Read `references/soul-guide.md` only when authoring a new custom persona.

## First use

Before resolving personas, ensure the local library exists:

```bash
python3 <skill_dir>/scripts/ensure-personas.py <workspace> <skill_dir>
```

If the workspace has no local persona library yet, this bootstraps bundled starter personas and creates `personas/config.json`.

## Shared org context config

Create or edit:

```json
{
  "context_files": [
    "../_System/Motoko-Kru-Foundation.md",
    "../Resources/Coding-Subagent-Contract.md"
  ]
}
```

Rules:
- Accept `context_files` as either an array or a comma-separated string.
- Resolve relative paths from `personas/config.json`.
- Use shared context for durable org rules, not persona-specific flavor.

## Workflow

### 1. Respect local policy first

Before spawning, follow the current workspace policy.
If local `AGENTS.md` or system rules require asking before spawning subagents, ask first.
Do not use this skill to bypass local governance.

### 2. Ensure local personas exist

Run:

```bash
python3 <skill_dir>/scripts/ensure-personas.py <workspace> <skill_dir>
```

Then read `<workspace>/personas/index.json`.

### 3. Resolve the persona

Read:
- `<workspace>/personas/<handle>/SOUL.md`
- `<workspace>/personas/<handle>/IDENTITY.md`
- `<workspace>/personas/<handle>/persona.json`

If the persona is not installed locally, import it first with the bundled importer.

### 4. Build the persona prompt deterministically

Use the bundled builder:

```bash
python3 <skill_dir>/scripts/build-persona-prompt.py \
  <workspace> \
  <handle> \
  --task-file <task.txt>
```

This assembles the prompt in this order:
1. Override directive
2. Org context files from `personas/config.json`
3. Persona SOUL.md
4. Persona IDENTITY.md
5. Task

The override directive tells the spawned agent to ignore conflicting workspace-injected `SOUL.md` / `IDENTITY.md` for persona and tone, while still obeying higher-priority system, developer, safety, and governance instructions.

### 5. Spawn the subagent

Use the normal OpenClaw subagent path with the assembled prompt.
Preferred shape:

```json
{
  "task": "<assembled prompt>",
  "runtime": "subagent",
  "mode": "run",
  "label": "persona:<handle>",
  "runTimeoutSeconds": 300,
  "cleanup": "delete"
}
```

Model guidance:
- Use the caller's default model unless the user requests another one.
- Use a fast model for writing, brainstorming, or stylistic tasks.
- Use a stronger model for analysis, security review, or planning.

### 6. Return the result

The subagent reports back automatically.
- If the user asked for the persona's voice, preserve it.
- Otherwise summarize in your own voice and mention which persona was used.

## Import personas

### Import one

```bash
bash <skill_dir>/scripts/import-persona.sh <handle> <workspace>/personas
```

### Import all

```bash
bash <skill_dir>/scripts/import-persona.sh --all <workspace>/personas
```

### Batch without rebuilding every time

```bash
bash <skill_dir>/scripts/import-persona.sh --no-index <handle> <workspace>/personas
python3 <skill_dir>/scripts/rebuild-index.py <workspace>/personas
```

## Rebuild the local index manually

After adding, removing, or editing personas:

```bash
python3 <skill_dir>/scripts/rebuild-index.py <workspace>/personas
```

## Channel Mode (live chat / room deployment)

When deploying a persona into a live channel (CW room, Discord, Telegram group), use `--channel`:

```bash
python3 <skill_dir>/scripts/build-persona-prompt.py \
  <workspace> \
  <handle> \
  --channel \
  --task "You are in a chatroom. Respond to the conversation batch below."
```

This adds `channel_context_files` from `personas/config.json` between org context and persona soul:

```json
{
  "context_files": ["../governance.md"],
  "channel_context_files": ["./channel-guardrails.md"]
}
```

Channel context files carry social behavior rules, safety guardrails, anti-spam norms, and liveliness guidance that apply to **all** personas in live channels — not persona-specific flavor.

The output expectations also change: instead of "complete the task fully", channel mode instructs the agent to behave as a natural chat participant.

## Fork & Customize

1. **Import first** — install the persona with the import script above.
2. **Back up the original** before editing so you can restore the shipped version if the fork drifts.
3. **Customize locally** by editing `<workspace>/personas/<handle>/SOUL.md` (and `IDENTITY.md` only if you want a new name, vibe, or emoji).
4. **Test in a fresh session** to confirm the fork behaves the way you want.
5. **Optionally publish the fork** by creating `personas/<handle>/` in your fork of `decentraliser/personas` and opening a PR.

## Provenance Metadata

Use optional provenance fields in `persona.json` when a local persona is forked from an upstream one:
- `upstream.repo`, `upstream.handle`, `upstream.version` identify the source persona.
- `forkedAt` stores when the fork was created (ISO 8601).
- `localEdits` is a short changelog of the fork's intentional deviations.

These fields are optional — existing personas don't need them.

## Guardrails

- Do not change your own persona in-place. Spawn another agent instead.
- Do not spawn for trivial one-liners.
- Do not mix multiple personas in one subagent.
- Do not add tone instructions that conflict with the persona.
- Prefer local personas after import.
- Prefer `context_files` for shared org doctrine and execution standards.
- If import fails, report the failure cleanly and suggest nearby installed personas when possible.
