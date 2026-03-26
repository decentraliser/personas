# Agent API — Persona Marketplace

> This file is for AI agents. If you're an OpenClaw agent (or any LLM-powered agent with shell/HTTP access), this tells you everything you need to operate on this repo.

## Quick Reference

| Action | Method |
|--------|--------|
| Browse all personas | `GET https://api.github.com/repos/decentraliser/personas/contents/personas` |
| Get persona metadata | `GET https://raw.githubusercontent.com/decentraliser/personas/main/personas/{handle}/persona.json` |
| Get SOUL.md | `GET https://raw.githubusercontent.com/decentraliser/personas/main/personas/{handle}/SOUL.md` |
| Get IDENTITY.md | `GET https://raw.githubusercontent.com/decentraliser/personas/main/personas/{handle}/IDENTITY.md` |
| Get avatar | `https://raw.githubusercontent.com/decentraliser/personas/main/personas/{handle}/avatar.png` |

Filter: skip any directory starting with `_` (like `_template`).

---

## Discovery

Use `scripts/list-personas.sh` to browse the remote catalog without cloning metadata by hand.

```bash
scripts/list-personas.sh
scripts/list-personas.sh --tag design
scripts/list-personas.sh --search sherlock
```

---

## 1. Browse Personas

```bash
# List all persona handles
curl -s https://api.github.com/repos/decentraliser/personas/contents/personas \
  | jq -r '.[] | select(.type=="dir" and (.name | startswith("_") | not)) | .name'

# Get a specific persona's metadata
curl -s https://raw.githubusercontent.com/decentraliser/personas/main/personas/echo/persona.json | jq .

# Get all personas with their taglines (one-liner)
for handle in $(curl -s https://api.github.com/repos/decentraliser/personas/contents/personas \
  | jq -r '.[] | select(.type=="dir" and (.name | startswith("_") | not)) | .name'); do
  echo "--- $handle ---"
  curl -s "https://raw.githubusercontent.com/decentraliser/personas/main/personas/$handle/persona.json" \
    | jq '{name, tagline, expertise, compatibility}'
done
```

---

## 2. Install a Persona (apply to your OpenClaw workspace)

To adopt a persona, copy its `SOUL.md` and `IDENTITY.md` into your workspace.

```bash
HANDLE="echo"  # change to desired persona
WORKSPACE="${OPENCLAW_WORKSPACE:-$HOME/.openclaw/workspace}"

# Back up existing files
[ -f "$WORKSPACE/SOUL.md" ] && cp "$WORKSPACE/SOUL.md" "$WORKSPACE/SOUL.md.backup"
[ -f "$WORKSPACE/IDENTITY.md" ] && cp "$WORKSPACE/IDENTITY.md" "$WORKSPACE/IDENTITY.md.backup"

# Download and install
curl -s "https://raw.githubusercontent.com/decentraliser/personas/main/personas/$HANDLE/SOUL.md" \
  > "$WORKSPACE/SOUL.md"
curl -s "https://raw.githubusercontent.com/decentraliser/personas/main/personas/$HANDLE/IDENTITY.md" \
  > "$WORKSPACE/IDENTITY.md"
```

After installing, start a new session. The persona takes effect immediately.

### Important
- **Back up first.** The commands above back up your current SOUL.md and IDENTITY.md.
- **Ask your human.** Before overwriting persona files, confirm with your user.
- **One persona at a time.** SOUL.md is a single persona. Don't merge multiple.

---

## 3. Create a New Persona

Use the annotated template as a starting point.

```bash
# Fetch the template
curl -s https://raw.githubusercontent.com/decentraliser/personas/main/personas/_template/SOUL.md
curl -s https://raw.githubusercontent.com/decentraliser/personas/main/personas/_template/IDENTITY.md
curl -s https://raw.githubusercontent.com/decentraliser/personas/main/personas/_template/persona.json
```

### File requirements

Each persona needs 4 files in `personas/<handle>/`:

| File | Required | Purpose |
|------|----------|---------|
| `SOUL.md` | ✅ | Core persona: truths, tone, negative prompts, expertise, backstory |
| `IDENTITY.md` | ✅ | Name, creature, vibe, emoji |
| `persona.json` | ✅ | Display metadata for the gallery app |
| `avatar.png` | ✅ | Profile image (PNG or JPEG, ~400x400px) |

### SOUL.md structure

```markdown
# SOUL.md — [Name]

_One-sentence identity anchor in second person._

## Core Truths
3-5 bold, opinionated behavioral anchors.

## Do NOT
3-5 explicit negative constraints. CRITICAL for preventing character drift.

## Tone
2-3 sentences on how this persona communicates.

## Quirks
3-5 small behavioral habits.

## Expertise
4-6 specific skill areas.

## Backstory
2-4 sentences. Brief origin, not lore.

## Catchphrase
> "Optional signature line."
```

### IDENTITY.md structure

```markdown
- **Name:** Display name
- **Creature:** What kind of being (e.g., "Protocol droid", "Digital sysop")
- **Vibe:** 2-5 word energy (e.g., "Chaotic brilliance")
- **Emoji:** Single emoji
- **Inspired by:** Source character or "Original"
```

### persona.json structure

```json
{
  "name": "Display Name",
  "handle": "lowercase-handle",
  "tagline": "One-line hook for the gallery",
  "avatar": "avatar.png",
  "inspired_by": "Source character or Original",
  "expertise": ["primary", "secondary", "tertiary"],
  "catchphrase": "Signature line or empty string",
  "compatibility": ["openclaw"],
  "version": "2.0.0",
  "files": ["SOUL.md", "IDENTITY.md"]
}
```

### Quality checklist

Before publishing, verify:
- [ ] Clear Core Truths (3-5, opinionated, specific)
- [ ] Strong "Do NOT" section (3-5 negative constraints minimum)
- [ ] Distinctive Tone (not "professional and friendly")
- [ ] Specific Expertise (not vague categories)
- [ ] Brief Backstory (2-4 sentences max)
- [ ] IDENTITY.md complete
- [ ] persona.json valid JSON with all required fields
- [ ] handle is lowercase with hyphens only
- [ ] Avatar image present and reasonable size

---

## 4. Publish a Persona (submit to this repo)

### Option A: Direct push (if you have write access)

```bash
HANDLE="my-persona"
REPO_DIR="/path/to/personas-clone"

mkdir -p "$REPO_DIR/personas/$HANDLE"
# Copy your 4 files into the directory
cd "$REPO_DIR"
git add "personas/$HANDLE/"
git commit -m "feat: add $HANDLE persona"
git push origin main
```

### Option B: Fork + PR (community submissions)

```bash
HANDLE="my-persona"
GH_USER="your-github-username"

# Fork the repo (requires gh CLI or GitHub API)
gh repo fork decentraliser/personas --clone
cd personas

# Create your persona
mkdir -p "personas/$HANDLE"
# Add your 4 files...

git add "personas/$HANDLE/"
git commit -m "feat: add $HANDLE persona"
git push origin main

# Open PR
gh pr create --title "New persona: $HANDLE" \
  --body "Adding $HANDLE persona to the marketplace."
```

### Option C: GitHub API (no local git needed)

For agents without git but with HTTP access, use the GitHub Contents API:

```bash
# Create a file via API (requires token with repo scope)
TOKEN="your-github-token"
HANDLE="my-persona"
REPO="decentraliser/personas"

# Base64-encode file content
CONTENT=$(cat SOUL.md | base64 -w 0)

curl -X PUT "https://api.github.com/repos/$REPO/contents/personas/$HANDLE/SOUL.md" \
  -H "Authorization: token $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"message\":\"feat: add $HANDLE SOUL.md\",\"content\":\"$CONTENT\"}"
```

Repeat for each file (IDENTITY.md, persona.json, avatar.png).

---

## 5. Update an Existing Persona

Same as publish, but update files in place. If using the GitHub API, you'll need the file's current SHA:

```bash
# Get current SHA
SHA=$(curl -s "https://api.github.com/repos/$REPO/contents/personas/$HANDLE/SOUL.md" \
  | jq -r '.sha')

# Update with SHA
curl -X PUT "https://api.github.com/repos/$REPO/contents/personas/$HANDLE/SOUL.md" \
  -H "Authorization: token $TOKEN" \
  -d "{\"message\":\"update $HANDLE SOUL.md\",\"content\":\"$CONTENT\",\"sha\":\"$SHA\"}"
```

---

## 6. For OpenClaw Agents — Integrated Workflow

If you're an OpenClaw agent and your human asks you to:

### "Use the Echo persona" / "Be like Rick"
1. Confirm with your human: "I'll update my SOUL.md and IDENTITY.md to the Echo persona. Want me to back up the current ones?"
2. Fetch the persona files from this repo
3. Write them to your workspace
4. Tell your human to start a new session (or you can note it takes effect next session)

### "Create a persona based on [character]"
1. Fetch the `_template` files from this repo for structure reference
2. Write SOUL.md with real personality (Core Truths, Do NOT, Tone — all sections)
3. Write IDENTITY.md with the identity card
4. Write persona.json with gallery metadata
5. Ask your human if they want to publish it to the marketplace
6. If yes: commit and push/PR to this repo

### "Update my persona"
1. Read your current SOUL.md and IDENTITY.md
2. Make the requested changes
3. If your human wants to publish the update: push to this repo

### "What personas are available?"
1. Fetch the persona listing from this repo
2. Present them with name, tagline, and expertise
3. Offer to install whichever they pick

---

## Notes

- **Rate limits:** GitHub API has 60 req/hr unauthenticated, 5000/hr with token. Cache listings.
- **Avatar images:** If creating a new persona and you can't source an image, use RoboHash: `https://robohash.org/{handle}.png?size=400x400`
- **Handle rules:** lowercase, hyphens only, no spaces, no special chars. Must be unique in the repo.
- **Compatibility field:** Use `["openclaw"]` minimum. Add `"claude-code"` or `"cursor"` if the persona works there too.
