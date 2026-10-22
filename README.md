# Agent Builder OS

> **Turn any real, recurring job into a structured, testable, portable folder-agent.**  
> Built by Denzel Chirinda ([@darksniper-2k47](https://github.com/darksniper-2k47)).

---

## ⚡ The Big Idea: The Folder IS The Agent

An agent is **not** a chat session, a black-box API script, or an external SaaS.  
**An agent is a folder of markdown files.**

Any modern AI (Claude Code, Cursor, Antigravity, Codex, ChatGPT) that reads the folder **becomes** that agent—on any computer, in any session, completely offline and version-controllable.

A real agent:
1. **Does the work** — produces finished assets, not conversational fluff.
2. **Has real judgment/taste** — embodies a proven operating system and self-critiques before delivery.
3. **Learns permanently** — human feedback is saved to memory (`lessons.md`) and obeyed forever.
4. **Validates its own structure** — runs deterministic contracts (`check_agent_folder.py`) before shipping.

---

## 🚀 Quick Setup On Your PC

### 1. Clone this repository
```bash
git clone https://github.com/darksniper-2k47/agent-builder.git
cd agent-builder
```

### 2. Launch It

#### Option A: 1-Click Launcher (Windows)
Double-click `Run Agent Builder.bat`. It boots Claude Code with the exact boot prompt.

#### Option B: Terminal / Mac / Linux
```bash
chmod +x run_agent_builder.sh
./run_agent_builder.sh
```

#### Option C: In Claude Code / Cursor / Antigravity
Open this folder in your IDE, start a session, and run:
```text
You are the AGENT BUILDER. Boot in this order: read AGENT_ENTRY.md, lessons.md, identity.md, ROUTER.md, rules.md, and reference/agent-building-operating-system.md. Obey shared/operating-discipline.md.
```

---

## 📁 Repository Structure

```
agent-builder/
├── README.md                           # Quickstart & architecture guide
├── HOW-TO-BUILD-AN-AGENT.md            # The master playbook (give to any AI)
├── Run Agent Builder.bat               # Windows double-click launcher
├── run_agent_builder.sh                # Mac/Linux launcher script
├── boot-prompt.txt                     # Startup boot prompt
├── AGENT_ENTRY.md                      # Entry point, role contract & routing
├── identity.md                         # Who the agent is & the standard it holds
├── rules.md                            # Process, gatekeeping & self-critique rules
├── ROUTER.md                           # File routing & token optimization
├── lessons.md                          # Lessons learned & operational corrections
├── state.md                            # Live runtime state
├── reference/
│   └── agent-building-operating-system.md  # The deep knowledge engine
├── shared/
│   └── operating-discipline.md         # 10 non-negotiable operating laws
├── tools/
│   └── check_agent_folder.py           # Verification script for created agents
└── visualizers/
    ├── business-agents-proposal.html   # Interactive visual agency proposal
    └── client-memory-architecture.html # Client memory system blueprint
```

---

## 🛠️ How to Build Your Own New Agent

Read the full manual in [`HOW-TO-BUILD-AN-AGENT.md`](./HOW-TO-BUILD-AN-AGENT.md).

The 4 core files every folder-agent requires:
1. **`identity.md`**: Its one specific job, the exact inputs it accepts, and the bar it must clear.
2. **`rules.md`**: Step-by-step execution protocol + self-critique gate.
3. **`lessons.md`**: What the operator corrected in past runs.
4. **`reference/<domain>-operating-system.md`**: The deep domain knowledge (curated frameworks, not high-level buzzwords).

### Verify Any Agent Folder:
```bash
python tools/check_agent_folder.py path/to/your-agent-folder
```
Checks all required files, contract markers, and references before running real tasks.

---

## 📜 The Operating Discipline
Every agent built with this system obeys the **10 Golden Rules** in [`shared/operating-discipline.md`](./shared/operating-discipline.md):
- Core intent over literal words.
- Fix the system, not the symptom.
- Embody the knowledge; do not name-drop it.
- Self-critique before delivery.
- "Tested" means the human operator tested it.

---

## 👤 Author & License
Crafted by **Denzel Chirinda** ([Empire Digital](https://github.com/darksniper-2k47)).  
Open source under the MIT License. Feel free to clone, build upon, and adapt for your own workflows!
