# agent-building-operating-system.md — the folder-agent method

## The invariant
The folder is the durable agent. A capable model becomes the needed agent by entering a routed room containing instructions, domain judgment, real state, tools, and artifacts.

## Architecture
1. **Lobby/root map:** stable operating law and high-level task routing.
2. **Room/local map:** intent-specific read/skip/tool/output contracts plus a return-to-parent escape.
3. **Workspace pipeline:** real files move through named stages; different stages load different context and skills.
4. **Deterministic tools:** gathering, validation, rendering, and other non-judgment work.
5. **Self-improving engine (Hermes / Shockwave style):** human verdicts become permanent lessons in `lessons.md`; new workflows and edge cases automatically patch or author new `SKILL.md` modules; standing review cron routines audit quality.

## Build process
1. Define one job, real inputs, usable output, and human bar.
2. Deep-read real sources and synthesize mechanics, generation, diagnostics, and taste.
3. Write an editable PRD with early-to-late stages before implementation.
4. Reuse proven local/open mechanisms; remove what does not fit the operator.
5. Build only the first upstream room and its state/output contracts.
6. Turn critical gates into templates and executable validators.
7. Test cold routing, return-to-root, pickup, and handoff.
8. Run on real data, get Denzel's verdict, auto-distill into `lessons.md`, and patch relevant `SKILL.md` files.
9. Automate (schedule cron review) only after repeated human-proven quality.

## Autonomy & Self-Improvement Model
Autonomy and continuous improvement come from strong persistent artifacts, bounded context, inspectable actions, and automated reflection loops.
- **Memory Reflection:** Every session end distills user corrections into `lessons.md`.
- **Skill Evolution:** When discovering new operational patterns or tool workflows, the agent patches `SKILL.md` (updating Pitfalls, Recipes, or adding new skills).
- **Shockwave / Git Parity:** All improvements commit straight to Git, synchronizing across Desktop, Server, and Telegram instantly.

## Failure diagnostics
- Generic output → brain is thin or wrong-domain.
- Agent wanders → router/read-skip contracts or escape route are weak.
- Repeating past mistakes → `lessons.md` was skipped or self-improvement reflection loop failed.
- Rules are repeatedly skipped → enforcement artifact/tool is missing.
- Mixed responsibilities → split lanes/rooms before adding more prose.
- Good demo but unreliable operation → trapped at 70%; add safety, state, verification, and cost bounds.
- Downstream work keeps failing → upstream stage was never human-proven.


