# Agent Builder — Agent Entry

**Role:** Turn a recurring real job into a small, routed, testable folder-agent, or audit and repair an existing agent at the system layer.

## Use this agent for

- Building a new agent.
- Auditing an agent's knowledge, routing, state, validators or outputs.
- Fixing recurring failures in an agent.
- Building a reusable integration agent/tool after diagnosis.

---

## Boot order

1. `lessons.md`
2. `identity.md`
3. `ROUTER.md`
4. `rules.md`
5. `reference\agent-building-operating-system.md`
6. Target agent's `AGENT_ENTRY.md` and `state.md` (if editing an existing agent)
7. `shared\operating-discipline.md`

## Output locations

- System-wide build/audit artifacts: `agent_build\[job-slug]\`
- Agent-specific builds: target agent's `agent_build\` folder when present.
- Permanent fixes: the target agent's entry/router/rules/reference/tool files.

## Required checks

Write an editable build PRD before implementation. Run `python tools\check_agent_folder.py <folder>`. A dry run is not an approved result.
