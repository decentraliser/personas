#!/usr/bin/env python3
"""Rebuild api/index.json from personas/ directory.
Run from repo root: python3 api/build-index.py
"""
import json, glob, os
from datetime import datetime, timezone

BASE_RAW = "https://raw.githubusercontent.com/decentraliser/personas/main"

PUNCHLINES = [
    "Science proved it: the persona IS the AI. Choose wisely.",
    "Your AI's character shapes every answer. Persona is architecture.",
    "The mask became the face. Persona selection is the new fine-tuning.",
    "LLMs don't just play characters — they become them. Pick the right one.",
    "Why fine-tune when you can cast? The right persona outperforms training.",
    "Post-training selects a character. We let you design that character.",
    "Role-playing is the optimal path. Not a hack — the architecture.",
]

def build():
    personas = []
    for pj in sorted(glob.glob("personas/*/persona.json")):
        handle = os.path.basename(os.path.dirname(pj))
        if handle.startswith("_"):
            continue
        with open(pj) as f:
            meta = json.load(f)
        files_available = [
            fn for fn in ["SOUL.md", "IDENTITY.md", "avatar.png"]
            if os.path.exists(os.path.join("personas", handle, fn))
        ]
        personas.append({
            "handle": handle,
            "name": meta.get("name", handle),
            "tagline": meta.get("tagline", ""),
            "inspired_by": meta.get("inspired_by", ""),
            "expertise": meta.get("expertise", []),
            "catchphrase": meta.get("catchphrase", ""),
            "compatibility": meta.get("compatibility", ["openclaw"]),
            "version": meta.get("version", "2.0.0"),
            "files": files_available,
            "urls": {
                "soul": f"{BASE_RAW}/personas/{handle}/SOUL.md",
                "identity": f"{BASE_RAW}/personas/{handle}/IDENTITY.md",
                "avatar": f"{BASE_RAW}/personas/{handle}/avatar.png",
                "metadata": f"{BASE_RAW}/personas/{handle}/persona.json",
            }
        })

    index = {
        "schema": "personas.index.v1",
        "meta": {
            "punchlines": PUNCHLINES,
            "total": len(personas),
            "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "repo": "https://github.com/decentraliser/personas",
            "template": f"{BASE_RAW}/personas/_template/SOUL.md",
        },
        "agent_quickstart": {
            "description": "To adopt a persona: fetch its SOUL.md and IDENTITY.md, write them to your workspace, restart your session.",
            "steps": [
                "Pick a persona from the list below",
                "GET {urls.soul} → write to workspace SOUL.md",
                "GET {urls.identity} → write to workspace IDENTITY.md",
                "Restart session or inform user to restart"
            ],
            "to_publish": [
                "Fork decentraliser/personas on GitHub",
                "Create personas/{handle}/ with SOUL.md, IDENTITY.md, persona.json, avatar.png",
                "Open PR to main branch",
                "See personas/_template/ for annotated file templates"
            ]
        },
        "personas": personas
    }

    os.makedirs("api", exist_ok=True)
    with open("api/index.json", "w") as f:
        json.dump(index, f, indent=2)
    print(f"✅ Built api/index.json — {len(personas)} personas")

if __name__ == "__main__":
    build()
