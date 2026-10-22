# pickup-handoff.md — continuity contract for every agent

These two code words let Denzel move between sessions, models, and projects without trusting chat memory.

## `pick up` — read-only continuity brief

1. **If a client is named or implied, resolve it first** — `clients\CLIENT_REGISTRY.csv`, then that
   client's `CLIENT.md` and `state.md`. Never ask Denzel to re-explain a client that has a record.
2. Read the most local `state.md`, then the local router and current project artifacts.
3. Verify important claims against disk. Do not rely on chat memory.
4. Report only the current job/stage, last completed work and changed files, open decisions, blockers, and smallest useful next move.
5. Make no changes unless Denzel also says to proceed.

## `hand off` — write and verify continuity

1. Update the most local `state.md`; do not create a competing memory file elsewhere.
2. Record current job/stage, completed work, changed files, decisions, blockers, and next move.
3. Preserve exact paths to full artifacts so compressed context remains recoverable.
4. **If the work touched a client, also write the client record** — append a dated entry to
   `clients\[slug]\THREAD.md`, overwrite `clients\[slug]\state.md`, and update the Commercial
   section of `CLIENT.md` if money was quoted, agreed, invoiced or paid. See
   `shared\client-memory.md`. This is not optional: a record nobody updates is worse than none,
   because the next session will trust a stale one.
5. Read `state.md` — and the client record, if written — back from disk and verify they cover
   the current situation.
6. Report the state-file path and anything that could not be verified.

## Scope

- State is local to the room/project that owns the work.
- A router mismatch returns to the parent/root router; do not wander through unrelated folders.
- Handoff is not completion. Only Denzel's real test can mark an agent or stage proven.

