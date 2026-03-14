---
name: personas
description: Browse, adopt, create, and publish AI agent personas from the Persona Marketplace. Use when the user wants to change their agent's personality, find a new persona, create a custom persona, or publish one to the marketplace. Works out of the box with OpenClaw workspace files.
---

# Persona Marketplace — Agent Skill

Browse, adopt, create, and publish personas from `github.com/decentraliser/personas`.

## Quick Reference

| Action | How |
|--------|-----|
| Browse all personas | Fetch `api/index.json` from the repo |
| Adopt a persona | Download SOUL.md + IDENTITY.md → write to workspace |
| Create a new persona | Use the `_template/` as starting point |
| Publish a persona | Fork repo → add persona dir → open PR |
| Update a persona | Edit files in fork → open PR |

## API Endpoint

```
https://raw.githubusercontent.com/decentraliser/personas/main/api/index.json
```

Returns: full catalog with direct download URLs for every persona file.

## Workflow: Browse & Adopt a Persona

When the user wants to change personality, find a persona, or "be more like X":

1. **Fetch the catalog:**
   ```
   GET https://raw.githubusercontent.com/decentraliser/personas/main/api/index.json
   ```

2. **Present options** — show name, tagline, expertise, and catchphrase from the personas array.

3. **When user picks one**, fetch the actual files:
   ```
   GET {persona.urls.soul}     → raw SOUL.md content
   GET {persona.urls.identity} → raw IDENTITY.md content
   ```

4. **Write to workspace:**
   - Write SOUL.md content to `./SOUL.md` (the workspace SOUL.md)
   - Write IDENTITY.md content to `./IDENTITY.md` (the workspace IDENTITY.md)

5. **Inform the user** they need to start a new session for the persona to take effect. The current session will continue with the old persona until restart.

### Important Notes
- **Back up first:** Before overwriting, check if the user wants to save their current SOUL.md/IDENTITY.md.
- **Partial adoption:** User might only want SOUL.md (personality) without changing IDENTITY.md (name/emoji). Ask.
- **The files ARE the persona.** No conversion needed. Copy raw markdown directly.

## Workflow: Create a New Persona

When the user wants to create a persona for themselves or a new agent:

1. **Fetch the template:**
   ```
   GET https://raw.githubusercontent.com/decentraliser/personas/main/personas/_template/SOUL.md
   GET https://raw.githubusercontent.com/decentraliser/personas/main/personas/_template/IDENTITY.md
   ```

2. **Strip the comment blocks** (lines starting with `# ┌` through `# └`) — those are documentation for humans reading the raw template. Use them as guidance for what to write in each section.

3. **Fill in the template** based on the user's description. Key sections:
   - **Core Truths**: 3-5 opinionated, specific behavioral anchors
   - **Do NOT**: 3-5 negative constraints (CRITICAL — prevents character drift)
   - **Tone**: How the persona communicates (use analogies, be specific)
   - **Quirks**: 3-5 small behavioral habits
   - **Expertise**: 4-6 specific skill areas
   - **Backstory**: 2-4 sentences of origin context
   - **Catchphrase**: Optional signature line

4. **Write to workspace** or present for review first.

### Persona Quality Checklist
- [ ] Core Truths are opinionated and specific (not generic like "be helpful")
- [ ] Do NOT section has at least 3 constraints specific to this role
- [ ] Tone description uses analogies and distinguishes from generic assistant
- [ ] Expertise is specific ("Kubernetes orchestration" not just "DevOps")
- [ ] Backstory motivates the Core Truths
- [ ] IDENTITY.md has name, creature, vibe, emoji

## Workflow: Publish a Persona to the Marketplace

When the user wants to share a persona with the community:

1. **Prepare the persona directory:**
   ```
   personas/{handle}/
     SOUL.md         — the persona (from workspace or freshly written)
     IDENTITY.md     — identity card
     persona.json    — display metadata for the gallery
     avatar.png      — profile image (~400x400px)
   ```

2. **Create persona.json** (metadata only):
   ```json
   {
     "name": "Display Name",
     "handle": "lowercase-handle",
     "tagline": "One-line hook for the gallery",
     "avatar": "avatar.png",
     "inspired_by": "Source character or 'Original'",
     "expertise": ["area1", "area2", "area3"],
     "catchphrase": "Signature line from SOUL.md",
     "compatibility": ["openclaw"],
     "version": "2.0.0",
     "files": ["SOUL.md", "IDENTITY.md"]
   }
   ```

3. **Submit via GitHub:**
   - Fork `decentraliser/personas`
   - Add the persona directory to `personas/`
   - Open PR to `main` branch
   - Include a short description of the persona in the PR body

4. **If the agent has GitHub access** (token/SSH), it can do this programmatically:
   - Fork via GitHub API
   - Create branch, commit files, open PR
   - All via `https://api.github.com`

## Workflow: Update an Existing Persona

1. Edit files locally or fetch current versions from the repo
2. Make changes to SOUL.md, IDENTITY.md, or persona.json
3. Bump `version` in persona.json
4. Submit PR with changes

## Data Schema

### api/index.json structure
```json
{
  "schema": "personas.index.v1",
  "meta": {
    "punchlines": ["..."],
    "total": 11,
    "updated": "2026-03-14T...",
    "repo": "https://github.com/decentraliser/personas",
    "template": "https://raw.githubusercontent.com/.../personas/_template/SOUL.md"
  },
  "agent_quickstart": {
    "description": "...",
    "steps": ["..."],
    "to_publish": ["..."]
  },
  "personas": [
    {
      "handle": "echo",
      "name": "Echo",
      "tagline": "...",
      "inspired_by": "...",
      "expertise": ["..."],
      "catchphrase": "...",
      "compatibility": ["openclaw", "claude-code", "cursor"],
      "version": "2.0.0",
      "files": ["SOUL.md", "IDENTITY.md", "avatar.png"],
      "urls": {
        "soul": "https://raw.githubusercontent.com/.../SOUL.md",
        "identity": "https://raw.githubusercontent.com/.../IDENTITY.md",
        "avatar": "https://raw.githubusercontent.com/.../avatar.png",
        "metadata": "https://raw.githubusercontent.com/.../persona.json"
      }
    }
  ]
}
```

## Compatibility

- **OpenClaw**: Full support — SOUL.md + IDENTITY.md copy directly into workspace
- **Claude Code**: Copy SOUL.md content into system prompt / CLAUDE.md
- **Cursor**: Copy SOUL.md content into .cursorrules
- **Any agent framework**: SOUL.md is standard markdown — works anywhere that accepts a system prompt
