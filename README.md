# 🎭 Personas

A marketplace of AI agent personas inspired by sci-fi and pop culture.

## v2 Standard (OpenClaw-native)

Each persona now ships as **actual markdown persona files** that can be copied directly into OpenClaw workspaces.

```
personas/
  <handle>/
    SOUL.md          # Core persona (tone, truths, boundaries, expertise)
    IDENTITY.md      # Name, vibe, creature, emoji
    avatar.png       # Profile picture
    persona.json     # Display metadata for gallery UI
```

## Why this structure?

OpenClaw agents are defined by markdown files (especially `SOUL.md` and `IDENTITY.md`).

If personas are only JSON, users must manually rewrite everything before use. That's bad UX.

With this standard:
- You can copy `SOUL.md` directly into OpenClaw
- You can copy `IDENTITY.md` directly into OpenClaw
- The web app still uses `persona.json` for fast rendering

## Persona Metadata Schema (`persona.json`)

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

## Founding Personas

- Slim Shader (Eminem-inspired SEO/GEO copywriter)
- Rick (Rick & Morty orchestrator)
- Echo (Matrix SysOp)
- C-3PO (docs manager)
- Morpheus (onboarding guide)
- Spock (logic and analytics)
- JARVIS (full-stack orchestration)
- Cortana (strategic analytics)
- GLaDOS (QA/testing)
- Data (data engineering)

## Usage in OpenClaw

1. Pick a persona
2. Copy `SOUL.md`
3. Paste into your agent workspace `SOUL.md`
4. (Optional) Copy/paste `IDENTITY.md`
5. Restart session

You're now running that persona.

## License

MIT

## Creating a new persona

Use the annotated template in `personas/_template/`:

```bash
cp -r personas/_template personas/my-persona
# Edit SOUL.md, IDENTITY.md, persona.json
# Add avatar.png
# Remove documentation comments
# Submit PR
```

The template includes inline documentation explaining:
- Why each section matters (backed by 2026 AI research)
- How negative prompts prevent character drift
- Best practices for effective persona design

See `personas/_template/README.md` for the full guide.
