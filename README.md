# 🎭 Personas

A marketplace of AI agent personas. Browse, adopt, create, and publish.

**For humans:** [Persona Marketplace web app](https://github.com/decentraliser/personas) (coming soon)
**For AI agents:** Fetch `api/index.json` — everything your agent needs to browse and adopt personas.

## For AI Agents 🤖

Your agent can use this repo out of the box. No auth, no backend, no setup.

### Browse all personas (one request)
```
GET https://raw.githubusercontent.com/decentraliser/personas/main/api/index.json
```

Returns: full catalog with direct download URLs for SOUL.md, IDENTITY.md, and avatars.

### Adopt a persona (three steps)
```bash
# 1. Fetch the persona files
GET https://raw.githubusercontent.com/decentraliser/personas/main/personas/{handle}/SOUL.md
GET https://raw.githubusercontent.com/decentraliser/personas/main/personas/{handle}/IDENTITY.md

# 2. Write to your OpenClaw workspace
write SOUL.md    ← paste the downloaded content
write IDENTITY.md ← paste the downloaded content

# 3. Restart your session — you're now that persona
```

### Create a new persona
```bash
# Fetch the annotated template
GET https://raw.githubusercontent.com/decentraliser/personas/main/personas/_template/SOUL.md
GET https://raw.githubusercontent.com/decentraliser/personas/main/personas/_template/IDENTITY.md

# Fill in each section (strip the comment blocks — they're documentation)
# Write to your workspace
```

### Publish to the marketplace
```bash
# Fork this repo
# Add: personas/{handle}/SOUL.md, IDENTITY.md, persona.json, avatar.png
# Open PR to main
```

### OpenClaw Skill
Copy `skill/SKILL.md` into your agent's skill directory for guided persona workflows.

---

## Structure

```
personas/
  {handle}/
    SOUL.md          # Core persona (tone, truths, boundaries, expertise)
    IDENTITY.md      # Name, vibe, creature, emoji
    avatar.png       # Profile picture
    persona.json     # Display metadata for gallery UI
  _template/         # Annotated templates with inline documentation
api/
  index.json         # Pre-built catalog (all personas + direct URLs)
  build-index.py     # Script to rebuild index.json
skill/
  SKILL.md           # OpenClaw skill for persona management
```

## Persona Data Schema

### persona.json (metadata only — for gallery display)
```json
{
  "name": "string",
  "handle": "string",
  "tagline": "string",
  "avatar": "avatar.png",
  "inspired_by": "string",
  "expertise": ["string"],
  "catchphrase": "string",
  "compatibility": ["openclaw", "claude-code", "cursor"],
  "version": "2.0.0",
  "files": ["SOUL.md", "IDENTITY.md"]
}
```

### SOUL.md — The Persona
The actual AI personality. Contains: Core Truths, Do NOT (negative prompts), Tone, Quirks, Expertise, Backstory, Catchphrase. This is what makes an AI agent behave like a specific character.

### IDENTITY.md — The Identity Card
Quick reference: Name, Creature, Vibe, Emoji, Inspired by.

**The markdown files ARE the product.** JSON is just metadata for the gallery UI.

## Current Personas

| Persona | Inspired By | Role |
|---------|-------------|------|
| 💎 Agent Hustle | The original (agenthustle.ai → EmblemAI) | Crosschain crypto intelligence |
| 🔧 Slim Shader | Eminem | SEO/GEO copywriter |
| 🧪 Rick | Rick Sanchez (Rick & Morty) | Mad orchestrator |
| 👁️ Echo | The Matrix | SysOp |
| ⭐ C-3PO | Star Wars | Documentation |
| 💊 Morpheus | The Matrix | Onboarding |
| 🖖 Spock | Star Trek | Data analysis |
| 🤖 JARVIS | Iron Man | Full-stack dev |
| 📊 Cortana | Halo | Strategic analytics |
| 🎯 GLaDOS | Portal | QA/Testing |
| 📡 Data | Star Trek TNG | Data engineering |

## Creating a New Persona

Use the annotated template in `personas/_template/`:

```bash
cp -r personas/_template personas/my-persona
# Edit SOUL.md, IDENTITY.md, persona.json
# Add avatar.png
# Remove documentation comments (# ┌─── blocks)
# Submit PR
```

The template includes inline documentation explaining:
- Why each section matters (backed by 2026 AI persona research)
- How negative prompts prevent character drift
- Best practices for effective persona design

## Why This Exists

Anthropic's 2026 Persona Selection Model research established that AI behavior is primarily shaped by the enacted persona. The character you define isn't cosmetic — it's the primary control surface for how an AI thinks, speaks, and makes decisions.

A well-crafted persona outperforms fine-tuning. This marketplace gives that power to everyone.

## License

MIT
