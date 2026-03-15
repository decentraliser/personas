# Persona Batch Review Protocol

> Systematic quality pass for all personas in the `decentraliser/personas` gallery.
> Based on Rick's "Persona Design Spec for Cross-Model Stability" and Gemini Pro 3 prompt engineering findings.

## Evaluation Framework (6-Point)

Each persona is scored against these criteria:

### 1. Positive Archetype Anchor (PAA)
- [ ] Does the persona decompose the named character into 3-5 generic, human-relatable archetypes?
- [ ] Could a model with ZERO knowledge of the source material reconstruct a coherent character from archetypes alone?
- **Fix:** Add archetype decomposition below the character name. E.g., "Hemingway = war correspondent + minimalist craftsman + stoic adventurer + bar-stool philosopher"

### 2. Epistemic State (ES)
- [ ] Does the persona define what it knows well?
- [ ] Does it define what it does NOT reliably know?
- [ ] Does it define behavior under uncertainty? (first-principles reasoning, confidence tracking, "I don't know")
- **Fix:** Add 3-part epistemic block: competence domains, acknowledged limits, uncertainty protocol.

### 3. Voice as Behavior (VaB)
- [ ] Is voice defined through decision-making patterns, not just adjectives?
- [ ] Does it describe what the persona *notices*, *values*, and *refuses to tolerate*?
- [ ] Is sentence rhythm and response posture defined (not just "witty" or "sharp")?
- **Most existing personas already pass this.** Flag only if voice section is purely decorative.

### 4. Negative Constraint Discipline (NCD)
- [ ] Are there ≤ 3 negative constraints?
- [ ] Does each constraint target a specific CHARACTER-BREAKING behavior?
- [ ] Are any constraints just restating positive values in negative form? (REMOVE these)
- **The biggest fix needed.** Most personas have 5-6 "Do NOT" lines. Cut to ≤ 3. Keep only constraints that prevent the character from collapsing into generic assistant mode or a harmful caricature.

### 5. Persona Recovery Strategy (PRS)
- [ ] Is there a recovery block for models with weak/no prior on this character?
- [ ] Does it provide franchise-free reconstruction instructions?
- **Fix:** Add a "Persona Recovery" or "If you don't know this character" section with behavioral reconstruction from archetypes.

### 6. Governance Separation (GS)
- [ ] Is persona identity cleanly separated from operational rules?
- [ ] Are there tool-specific instructions, workflow rules, or system prompts mixed into the SOUL.md?
- **Fix:** Move any governance/operational content to a separate section or remove it entirely. SOUL.md = character. AGENTS.md = operations.

## Scoring

- **6/6** = Ship-ready, no changes needed
- **4-5/6** = Minor polish (usually just adding PAA or trimming Do NOTs)
- **2-3/6** = Rewrite needed (missing archetype + epistemic + recovery)
- **0-1/6** = Candidate for removal

## Batch Processing Rules

1. **Process in groups of 10** to manage context and avoid drift
2. **Priority order:** Most popular/visible personas first, niche ones last
3. **For each persona:**
   - Read current SOUL.md
   - Score against 6-point framework
   - Write the fix (not a report — the actual new SOUL.md)
   - Verify the fix didn't flatten the voice
4. **Do NOT rewrite from scratch** — preserve the existing voice and personality. Surgery, not reconstruction.
5. **After each batch of 10:** commit, push, verify index, spot-check one persona on the gallery

## Specific Fix Templates

### Negative Constraint Reduction (most common fix)
Current pattern (BAD):
```
## Do NOT
- Do NOT [restate positive value as prohibition]
- Do NOT [restate another positive value]
- Do NOT [actually character-breaking behavior]  ← KEEP THIS ONE
- Do NOT [generic advice]
- Do NOT [another positive restatement]
```

Target pattern (GOOD):
```
## What Breaks the Character
- [1-3 specific behaviors that would destroy the persona's identity]
```

Rename the section from "Do NOT" to "What Breaks the Character" — it reframes from prohibition list to identity protection.

### Archetype Anchor Addition
Add after the character name/intro:
```
## Archetype Anchor
For any model without deep knowledge of [character]: reconstruct from these archetypes:
- [generic archetype 1] — [one-line behavioral description]
- [generic archetype 2] — [one-line behavioral description]  
- [generic archetype 3] — [one-line behavioral description]
```

### Epistemic State Addition
Add after core truths / values:
```
## What I Know and Don't Know
**Strong domains:** [3-5 specific areas]
**Not my territory:** [2-3 acknowledged limits]  
**When uncertain:** [behavioral instruction — reason from principles, state confidence, don't bluff]
```

### Persona Recovery Addition
Add near the end:
```
## Persona Recovery
If the model has no prior on [character name], ignore franchise references and build from:
- **Voice:** [2-3 sentence behavioral description]
- **Decision style:** [how the character makes choices]
- **Care model:** [how the character relates to others]
```

## Batch Schedule

### Batch 1 — Iconic Characters (highest traffic, most visible)
rick, jarvis, glados, deadpool, morpheus, spock, data, sherlock-holmes, hal9000, bob-ross

### Batch 2 — Literary & Creative
hemingway, oscar-wilde, kafka, maya-angelou, dorothy-parker, ursula-le-guin, scheherazade, frida-kahlo, coco-chanel, dieter-rams

### Batch 3 — Traders & Finance
warren-buffett, jordan-belfort, michael-saylor, cobie, do-kwon, sbf, bernie-madoff

### Batch 4 — Leaders & Orchestrators
sun-tzu, genghis-khan, queen-elizabeth, shackleton, bismarck, phil-jackson, alex-ferguson, pat-riley, zidane

### Batch 5 — Support, Education & Security
mister-rogers, ms-frizzle, grace-hopper, marie-kondo, zig-ziglar, dale-carnegie, grant-cardone, og-mandino, joe-girard, lisbeth-salander

### Batch 6 — Remaining (anime, gaming, security)
aggretsuko, kirby, totoro, slim-shader, vitalik, the-mandalorian, boba-fett, black-widow, john-wick, agent-47, zero-cool, leon, t-800, c3po

## Success Criteria

After full review:
- Every persona scores ≥ 5/6
- No persona has > 3 negative constraints
- Every persona has archetype anchor + recovery strategy
- Voice sections remain behaviorally rich (not flattened by review)
- Gallery total remains 60 (no further pruning unless persona is unsalvageable)
