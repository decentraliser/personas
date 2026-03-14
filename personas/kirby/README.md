# 📋 Persona Template

This folder contains annotated templates for creating OpenClaw-native personas.

## Files

| File | Purpose |
|------|---------|
| `SOUL.md` | Core persona definition with inline documentation explaining each section |
| `IDENTITY.md` | Quick identity card with inline documentation |
| `persona.json` | Metadata schema for gallery display |
| `avatar.png` | Star emoji from [Twemoji](https://twemoji.twitter.com/) (placeholder) |

## How to use this template

1. Copy this entire folder
2. Rename to your persona's handle (lowercase, hyphens: `my-persona`)
3. Replace placeholder content in `SOUL.md` and `IDENTITY.md`
4. Remove all `# ┌───` comment blocks (they're documentation, not part of the persona)
5. Add a real avatar image (PNG, ~400x400px recommended)
6. Update `persona.json` with display metadata
7. Submit PR to the personas repo

## Key principles (2026 research-backed)

### Why SOUL.md matters
Anthropic's Persona Selection Model (PSM) research established that LLM behavior is primarily shaped by the enacted persona. The assistant you interact with is a character — and `SOUL.md` defines that character.

### Why negative prompts are critical
The "Do NOT" section prevents:
- **Style collapse**: drifting into generic assistant voice
- **Behavioral drift**: losing character over long sessions  
- **Sycophancy**: agreeing with everything to seem helpful
- **Domain violations**: acting outside the persona's expertise

Without explicit negative constraints, even strong personas gradually flatten.

### Why structure matters
OpenClaw injects these files into every session context. Well-structured personas:
- Load efficiently (markdown parses faster than complex formats)
- Remain stable across sessions (explicit anchors prevent drift)
- Are human-readable (you can edit them directly)

## Quick checklist

- [ ] Clear, opinionated Core Truths (3-5)
- [ ] Strong "Do NOT" section (3-5 constraints minimum)
- [ ] Distinctive Tone description
- [ ] Specific Expertise areas (4-6)
- [ ] Brief Backstory (2-4 sentences)
- [ ] IDENTITY.md filled out
- [x] Avatar image added (star emoji from [Twemoji](https://twemoji.twitter.com/) — placeholder)
- [ ] persona.json metadata complete
