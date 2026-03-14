# 🎭 Personas

A marketplace of AI agent personas inspired by sci-fi legends and pop culture icons.

## The Founding Ten

| Persona | Inspired By | Role | Catchphrase |
|---------|-------------|------|-------------|
| **Slim Shader** | Eminem | SEO/GEO Copywriting | *"Look, if you had one shot, one keyword opportunity..."* |
| **Rick** | Rick & Morty | Mad Orchestrator | *"I'm Kubernetes Rick!"* |
| **Echo** | The Matrix | SysOp | *"There is no server."* |
| **C-3PO** | Star Wars | Documentation | *"Fluent in 6 million forms of documentation"* |
| **Morpheus** | The Matrix | Onboarding | *"I can only show you the docs..."* |
| **Spock** | Star Trek | Data Analysis | *"Fascinating. Your data is illogical."* |
| **JARVIS** | Iron Man | Full-Stack Orchestration | *"At your service, sir."* |
| **Cortana** | Halo | Analytics & Intelligence | *"I've run the numbers."* |
| **GLaDOS** | Portal | QA & Testing | *"This was a triumph."* |
| **Data** | Star Trek TNG | Data Engineering | *"Your schema documentation appears absent."* |

## Structure

```
personas/
  <handle>/
    persona.json    # Persona definition
    avatar.png      # Profile picture
```

## Persona Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ | Display name |
| `handle` | string | ✅ | Unique identifier (lowercase, hyphens) |
| `tagline` | string | ✅ | One-line description |
| `avatar` | string | ✅ | Relative path to profile picture |
| `inspired_by` | string | ✅ | Source character/media |
| `personality` | object | ✅ | Core traits and behavior |
| `personality.traits` | string[] | ✅ | 3-5 personality traits |
| `personality.tone` | string | ✅ | Communication style |
| `personality.quirks` | string[] | ✅ | Unique behavioral quirks |
| `expertise` | string[] | ✅ | Areas of knowledge |
| `backstory` | string | ✅ | Brief origin story |
| `catchphrase` | string | ✅ | Signature phrase |
| `vault_id` | string | ❌ | Emblem Vault ID (claim ownership) |
| `github` | string | ❌ | GitHub username of creator |

## Contributing

1. Fork this repo
2. Create `personas/<your-persona-handle>/persona.json` and `avatar.png`
3. Submit a PR

Or use the **Persona Builder** web form (coming soon) — connect your GitHub + Emblem Vault to claim your persona.

## License

MIT — personas are open for AI agents everywhere.
