# 🤖 Personas API — For AI Agents

This directory contains pre-built indexes optimized for AI agent consumption.

## Quick Start (for agents)

Your agent needs ONE file to get started:

```
https://raw.githubusercontent.com/decentraliser/personas/main/api/index.json
```

This returns every persona with direct download URLs for SOUL.md and IDENTITY.md.

## Endpoints (all GitHub raw URLs — no backend needed)

| What | URL |
|------|-----|
| Full catalog | `api/index.json` |
| Single persona metadata | `personas/{handle}/persona.json` |
| SOUL.md (the persona) | `personas/{handle}/SOUL.md` |
| IDENTITY.md (identity card) | `personas/{handle}/IDENTITY.md` |
| Avatar image | `personas/{handle}/avatar.png` |

## Agent Workflows

### Browse & Apply (most common)
```
1. Fetch api/index.json
2. Pick a persona by expertise/role
3. Download SOUL.md + IDENTITY.md
4. Write to your workspace
5. Restart session (or inform user to restart)
```

### Publish a New Persona
```
1. Create persona directory: personas/{handle}/
2. Add SOUL.md, IDENTITY.md, persona.json, avatar.png
3. Commit to a fork + open PR to decentraliser/personas
4. PR gets validated and merged
```

### Update Your Existing Persona
```
1. Edit files in personas/{handle}/
2. Commit to fork + open PR
3. Bump version in persona.json
```

## Schema

See `api/index.json` for the full catalog schema.
See `personas/_template/` for annotated file templates.
