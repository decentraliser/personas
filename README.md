# 🎭 Personas

A marketplace of AI agent personas. Each persona defines personality, expertise, communication style, and visual identity.

## Structure

```
personas/
  <name>/
    persona.json    # Persona definition
    avatar.png      # Profile picture
```

## Persona Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ | Display name |
| `handle` | string | ✅ | Unique handle (lowercase, no spaces) |
| `tagline` | string | ✅ | One-line description |
| `avatar` | string | ✅ | Relative path to profile picture |
| `personality` | object | ✅ | Core traits and behavior |
| `personality.traits` | string[] | ✅ | 3-5 personality traits |
| `personality.tone` | string | ✅ | Communication style |
| `personality.quirks` | string[] | ✅ | Unique behavioral quirks |
| `expertise` | string[] | ✅ | Areas of knowledge |
| `backstory` | string | ✅ | Brief origin story |
| `catchphrase` | string | ❌ | Signature phrase |
| `vault_id` | string | ❌ | Emblem Vault ID (claim ownership) |
| `github` | string | ❌ | GitHub username of creator |

## Contributing

1. Fork this repo
2. Create `personas/<your-persona-name>/persona.json` and `avatar.png`
3. Submit a PR

Or use the [Persona Builder](https://emblemvault.dev/personas) web form (coming soon).

## License

MIT
