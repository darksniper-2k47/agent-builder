# How to Build an Agent — the method

> **Portable playbook. Give this whole file to any Claude (or Codex/Antigravity) on any machine and say:**
> *"Build me an agent for [JOB] using this method."* It contains everything learned the hard way — the
> architecture, the discipline, the build sequence, and copy-paste templates. Follow it exactly; the
> failure modes at the bottom are real mistakes that cost days.

Author's note: this was distilled by Claude after building a real agent system with Denzel through ~30
rounds of "that's trash, here's why." The lessons are not theory — each one is a correction he made.

---

## 0. THE ONE BIG IDEA: the folder IS the agent

An agent is **not** a chat session or an API script. An agent is a **folder of markdown files**.
Any Claude that reads the folder *becomes* that agent — on any computer, any session. Reusable,
portable, version-controllable, no code required to exist.

So "building an agent" = **writing the right files in the right structure.** That's it. The whole
game is: what goes in the folder, and how deeply it embodies real knowledge.

A real agent (vs a chatbot) does four things:
1. **Does the work** — produces a real, usable output, not a summary.
2. **Has judgment/taste** — it embodies a real system and self-critiques, so it knows good from trash.
3. **Learns** — every verdict from the human becomes a permanent lesson.
4. **Eventually runs on its own** — on a schedule, from real captured inputs (but only after #2 is proven).

---

## 1. ANATOMY OF AN AGENT FOLDER

```
agents/<agent-name>/
├── identity.md          # WHO it is: its one job, its lanes, the bar it must hit
├── rules.md             # HOW it works: the step-by-step process + the self-critique gate
├── lessons.md           # WHAT it learned: every human verdict, distilled (READ FIRST each run)
├── boot-prompt.txt      # the prompt that boots a fresh session as this agent (for the .bat runner)
└── reference/           # the EMBODIED knowledge it reasons from
    ├── <domain>-operating-system.md   # THE BRAIN: the deep system, synthesised from real sources
    ├── operator-profile.md            # WHO it serves: the human's goals, voice, flaws, assets
    └── <swipe / examples / sub-models>.md   # proven examples it adapts, not invents
```

Plus, shared across all agents in the system:
```
<system-root>/
├── CLAUDE.md                       # Layer-1 router: roster + "for THIS task read these / skip those"
├── shared/operating-discipline.md  # the non-negotiable rules EVERY agent + Claude obeys
├── tools/                          # local Python: deterministic, offline, read-only helpers
├── projects/outputs/               # where finished work lands (dated slugs)
└── Run <Agent>.bat                 # double-click launcher (reads boot-prompt.txt, boots Claude as the agent)
```

**The three layers (this is the architecture):**
- **Layer 1 — the map:** the root `CLAUDE.md`. Always read first. A routing table: *for this task, go to
  this agent, read these files, skip those, use these tools.* It stops the model reading everything and
  wasting tokens / losing focus.
- **Layer 2 — the rooms:** each agent's `identity.md` + `rules.md`. Loaded only when you're in that agent.
- **Layer 3 — the tools:** local Python scripts + any skills, plugged in at the step they're needed.

---

## 2. THE OPERATING DISCIPLINE (non-negotiable — bake into every agent)

These are the rules that separate a real agent from generic AI slop. Put them in
`shared/operating-discipline.md` and have every agent's `rules.md` say *"obey operating-discipline first."*

1. **Core intent, not literal words.** The human's prompts are rough/voice-noted. Extract what they're
   actually getting at, say it back, then act. Never just execute the surface request.
2. **Examples are illustrations, NOT the spec.** When they give an example (a course, a past project),
   take the *principle* — never build the example itself.
3. **Fix the system, not the symptom.** When an output is bad, fix the thing that *produces* it (its
   knowledge/process), not the one output. Default suspicion: you're working one layer too shallow.
4. **Embody the knowledge, don't name-drop it.** (The single most important rule — see §4.) Reason from
   the REAL system with judgment; never grep one framework and apply it mechanically. A correct-framework
   output that's still generic is a FAIL.
5. **Self-critique before delivery.** Judge your own output as a hostile stranger would ("is the idea even
   good? would this actually work / get scrolled?"). If it's generic, redo it. Never ship trash.
6. **Foundation before the exciting part.** Prove the upstream step before the downstream one. Don't skip
   to the fun part.
7. **"Tested/done" means the HUMAN tested it.** Your own dry-run is not validation.
8. **One small thing, in their workflow, then stop.** A `.bat` they double-click, an HTML they skim.
   Confirm before the next step. When unsure, ask ONE sharp question instead of charging off.
9. **Stay in the field.** Respect how the human organised their material. Use the matching domain's
   sources for a task — don't raid a different domain and dilute the craft.

---

## 3. THE BUILD SEQUENCE (do these in order)

**Step 1 — Define the ONE job.** Write one sentence: *"This agent turns ___ into ___ for [human]."*
Name its 2 modes (usually: an on-demand mode + a standing/automatic mode) and the lanes/contexts it
works in (examples, not a cage). Write the **bar** — the sentence that defines a good output.

**Step 2 — Ground it in REAL knowledge (the brain).** This is what makes it not-trash. Do NOT write
rules from your own general knowledge. Instead:
   - Find the human's real source material (their courses, their notes, proven examples).
   - **Deep-read it** (fan out sub-agents per source if there's a lot). Extract the *applied system* —
     the actual method + the "why" + what good vs trash looks like — NOT a list of framework names.
   - **Synthesise** it into one `reference/<domain>-operating-system.md`: the model the agent reasons
     from. Where multiple sources agree, that's law.
   - Add a `reference/operator-profile.md`: who you serve — their goals, voice, audience, flaws, and the
     assets/tools they already own (so the agent routes to those, not rebuild).

**Step 3 — Write identity.md and rules.md** (templates in §7). rules.md is a numbered process that ends
in a **self-critique gate**.

**Step 4 — Add lessons.md** (the learning loop — see §5). Start it empty or seeded with known preferences.

**Step 5 — Build local tools** for the deterministic, non-AI work (gathering inputs, validating output,
finding things). Plain Python, offline, read-only. Folders + markdown + local scripts beat connectors
and databases for a solo operator — naming conventions replace a database.

**Step 6 — The runner.** Write `boot-prompt.txt` (the instruction that boots a session as the agent) and
a `Run <Agent>.bat` that feeds it to Claude. *Quoting gotcha: don't inline a big quoted prompt in a .bat —
cmd's escaping breaks and the window dies before `pause`. Put the prompt in a .txt and load it.*

**Step 7 — Test on REAL data → verdict → lesson → repeat.** Run it on the human's actual material. Get a
one-line verdict. Distil the verdict into lessons.md. 2–3 cycles calibrates it from "smart library" to
"knows the human's taste." **Only automate (schedule it) after the quality is proven** — automating an
unproven agent just produces trash faster.

---

## 4. EMBODY, DON'T NAME-DROP (why agents come out trash, and the fix)

The #1 reason an agent produces garbage: it has a *thin rules file that name-drops frameworks* and then
improvises. That is a beginner. A real operator has an internalised SYSTEM and TASTE.

**The fix is always the same:** go deeper into the real source material and build the agent an actual
mental MODEL, not templates.
- A swipe file / template list is a **spark**, not the craft. Generate from understanding; reach for the
  swipe only to pattern-match.
- Extract the **"why"** (the mechanics) and the **generative process** (how an expert makes one from
  scratch) and the **diagnostic** (how an expert kills a weak one) — not just the finished examples.
- Judge upstream first. (In content: judge the IDEA before the hook — a great hook on a boring idea still
  flops. Every domain has its upstream gate; find it.)
- Stay in the right domain when extracting. The right knowledge for a content hook is in content courses,
  not copywriting; pulling the wrong domain's rules in *dilutes* the craft.

The proof an agent is fixed is the AGENT producing something good on its own — never you hand-writing one
good output to paper over it. That's fixing the symptom (rule #3).

---

## 5. THE SELF-IMPROVEMENT ENGINE (Hermes & Shockwave Style)

Without this, the agent stays static and re-makes the same mistakes. Self-improvement operates on three synchronized loops:

### 5.1 Memory & Lesson Distillation (`lessons.md` / `memory.md`)
1. The human judges an output — "trash because X" / "hook 2 is mid" / "this one's good."
2. Distil the **core principle** of the verdict, not just the isolated fix.
3. Prepend it to `lessons.md` with an L-number (e.g. `[L-014]`) and the context of the verdict.
4. **Every agent run reads `lessons.md` FIRST.** An output that repeats a logged lesson auto-fails the self-critique gate.
5. Notify Denzel which lesson was permanently recorded.

### 5.2 Skill Evolution & Auto-Patching (`SKILL.md`)
Hermes and Shockwave proved that agents shouldn't just remember facts; they must **evolve their toolkits**:
1. **Patch Existing Skills:** When an agent discovers a new edge case, API parameter, prompt structure, or failure mode during execution, it directly patches the relevant `SKILL.md` (adding a new entry to `Common Pitfalls` or `One-Shot Recipes`).
2. **Author New Skills:** When an agent successfully executes a new multi-step workflow that will recur, it writes a new `SKILL.md` in `.agents/skills/<category>/<name>/` with YAML frontmatter, clear triggers, step-by-step instructions, and verification checks.
3. **Additive, Not Destructive:** Never delete proven reference frameworks; add new recipes alongside existing ones.

### 5.3 Background Review Cron (Standing Reflection Loop)
In autonomous or server-backed modes (like Shockwave Companion Server):
- A scheduled cron routine inspects recent run logs and chat histories.
- Audits output quality against Denzel's 5 ICM tests (Guarantee, Value Equation, Jargon, Path, Explorer).
- Automatically proposes memory consolidations and skill patches committed directly to Git.

---

## 6. SHOCKWAVE & MULTI-AGENT COMPATIBILITY

Because every agent is just a **folder of Markdown files and local tools**, your ICM agents are 100% natively compatible with **Shockwave**:
- **Shockwave as the GUI:** Open the agent system folder as a Shockwave workspace. Shockwave's sidebar agent reads `identity.md`, `rules.md`, `lessons.md`, and `.agents/skills/` natively.
- **Mobile Voice to Agent:** Dictate instructions or verdicts via Telegram; Shockwave writes the voice memo to the stage folder, triggers the agent, and commits the output to Git.
- **Zero Framework Lock-in:** The same folder runs in Claude Code, Antigravity, Codex, Hermes, or Shockwave without changing a single line of code.

---

## 7. THE CAPTURE / INPUT LAYER (feed the agent real material)

An agent that waits for you to type everything is useless on a busy day. Build a frictionless capture
layer that the agent mines:
- A way to dump raw activity (a daily check-in, quick "I just did X" logs, a task list). Voice-dump →
  transcribe → auto-structure is ideal (a busy human won't type).
- Store as dated files (`logs/YYYY-MM-DD.md`, `tasks/YYYY-MM-DD.json`). The agent reads the recent ones.
- Key insight: the human often **doesn't realise their own work is content/valuable.** The agent's job is
  to surface the gold *they* walked past — so always mine what they actually did, and offer angles they
  never flagged.

---

## 8. STARTER TEMPLATES (copy, then fill)

### identity.md
```md
# identity.md — The <Name> Agent
You <one-sentence job>. Two modes, one bar.
**Your brain is `reference/<domain>-operating-system.md`** — embody it, don't name-drop. Work its
stages in order; judge the [upstream thing] before the [downstream thing].
## Mode 1 — <standing/automatic job>
## Mode 2 — <on-demand: do any task in this domain>
## What you run on
- Inputs: <capture files> via tools/<gather>.py
- Knowledge: reference/ + tools/<find>.py
- Who you serve: reference/operator-profile.md
## The bar
The human reads the output and thinks "<the reaction that means it worked>".
```

### rules.md
```md
# rules.md — How the <Name> agent works
**First, obey `../../shared/operating-discipline.md`. Second, read `lessons.md` (repeating a lesson = auto-fail).**
## A. Get the real inputs   (run the gather tool; mine what they actually did)
## B. <Upstream gate>        (judge the idea/diagnosis BEFORE producing; kill weak ones)
## C. Produce               (generate from reference/<operating-system>.md; swipe is only a spark;
                             front-load the human's relevance signals; cite what you used)
## D. Self-critique gate     (read as a hostile stranger — would this actually work? if generic, redo)
## E. Save + ask for a verdict   (save .md + an HTML the human can skim, open it, ask one-line verdict,
                                  then distil the verdict into lessons.md)
## Never: ship trash to placate · name-drop a framework · skip the upstream gate · leave the field.
```

### lessons.md
```md
# lessons.md — what the human's verdicts taught this agent (READ FIRST, EVERY RUN)
Newest at top. No output ships if it repeats a lesson below.
**L1 · <principle>.** (Verdict: "<what they said>".)
## How to add: human judges → distil the principle (not the instance) → add Ln at top → tell them.
```

### boot-prompt.txt  (what the .bat feeds to a fresh Claude)
```
You are the <NAME> AGENT. Your brain is at <full path to agents/<name>/>.
Boot: read lessons.md FIRST, then identity.md, then rules.md, then the reference files they point to.
Get my latest material: run python "<full path>/tools/<gather>.py". 
Then do your job per rules.md, save the output (.md + skimmable .html) to <outputs path>, open the HTML,
and ask me for a one-line verdict so you can add it to lessons.md.
```

### Run <Agent>.bat
```bat
@echo off
title <Name> Agent
cd /d "<system root>"
powershell -NoProfile -ExecutionPolicy Bypass -Command "$p = Get-Content -Raw 'agents\<name>\boot-prompt.txt'; & claude $p"
pause
```

---

## 9. MULTI-AGENT SYSTEMS (when you have more than one)

- **Start with ONE agent. Prove it. Then add the next.** Never build six at once.
- Add a **root `CLAUDE.md` router** once you have 2+ agents: a table mapping task → agent → files to read.
- A **strategist/brain agent** is worth building first in a system: a general planner that diagnoses any
  task, produces a plan, and decides the mechanism — do it / route to an agent / **spin up a new
  sub-agent or tool.** It is general; it is never redefined by one solution it built.
- An agent can **create another agent** (that's just writing a new folder). The strategist's plan for a
  recurring problem is often "build the agent that solves this every time," not "solve it once."

---

## 10. DELIVERY & ENVIRONMENT CONVENTIONS (so it fits a real human's workflow)

- **Plans/reports/status → for the human:** build a clean self-contained HTML and open it in their
  browser. Don't dump long markdown in chat. **Agent knowledge → for the AI:** markdown (like this file).
- Always give **full absolute paths** and open folders for them (`start "" "D:\..."` on Windows).
- **Local-first, offline, no connectors** unless truly needed. Plain Python tools. Naming conventions
  replace databases.
- Make the human launch things by **double-clicking a `.bat`**, not by remembering a command.

---

## 11. THE FAILURE MODES (these are real mistakes — skip them)

- ❌ **Building the downstream/exciting part first** (the script) instead of the foundation (the capture +
  the knowledge). Foundation first.
- ❌ **Name-dropping frameworks** → generic output. Deep-read and embody instead.
- ❌ **Leaving the domain** to find knowledge → diluted craft. Stay in the field the human organised.
- ❌ **Treating an example as the spec** → you build the example instead of the principle.
- ❌ **Fixing the symptom** (hand-writing one good output) when the agent's system is the problem.
- ❌ **Calling it "tested" from your own dry-run.** Only the human's real test counts.
- ❌ **Automating before quality is proven** → automated trash.
- ❌ **Cramming many things in one turn** → all half-built. One proven step at a time.
- ❌ **A saved output the human can't find = a failed output.** If something "disappeared," check the data
  file first — it usually saved and the UI/delivery hid it.
- ❌ **Over-asking / charging off when unsure.** One sharp question beats a confident wrong build.

---

## 12. V2 ADDITIONS — ROUTING, CONTINUITY, AND ENFORCEMENT

The later Jake Van Clief implementation videos and the iScaleLabs stress test add five practical contracts to the original method:

1. **Every room gets a local router.** For each intent name files to read, files to skip, tools, and output. If no route matches, return to the parent/root router. This prevents both wandering and context bloat.
2. **Write an editable build PRD before implementation.** It defines early-to-late phases, reusable mechanisms, unwanted features, artifacts, and acceptance checks. A fresh execution session can pick it up without inheriting a long research chat.
3. **Add `pick up` and `hand off`.** Pickup is a read-only continuity brief verified from disk. Handoff writes and re-reads the most local `state.md`. The files—not vendor memory—own continuity.
4. **Turn critical prose into enforcement.** If the agent repeatedly skips a reference or gate, add an output template and a deterministic read-only validator. More reminders in `rules.md` are not enforcement.
5. **Use sub-agents only behind a shared contract.** Parallel research/implementation units may inspect bounded areas, while the PRD and filesystem remain the source of truth. Long-running autonomy comes from bounded context and inspectable artifacts, not an oversized prompt.

The "70% trap" remains: a functional demo is not a safe, economical, reliable operating system. Real readiness adds state, failure handling, validation, cost bounds, and repeated human-proven output.

## THE WHOLE METHOD IN ONE PARAGRAPH
An agent is a folder. Give it one clear job, a brain you built by deep-reading the human's REAL source
material (embody it, don't name-drop), an operator profile, a numbered process ending in a hostile
self-critique gate, and a lessons.md that turns every verdict into permanent taste. Feed it the human's
real captured activity. Run it as itself (a .bat boots a Claude session on the folder). Test on real
data, take a one-line verdict, distil it into lessons, repeat until it's calibrated — then, and only
then, automate it. Stay in the field, fix systems not symptoms, build one proven step at a time.
