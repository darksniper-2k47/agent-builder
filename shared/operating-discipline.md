# operating-discipline.md — how every agent here (and Claude) must operate

Hard-won from Denzel's corrections. Every agent in this system reads this. Claude reads it too.
These exist because the SAME mistakes kept happening. Do not repeat them.

## The 8 rules

1. **CORE INTENT, NOT LITERAL WORDS.** Denzel's prompts are rough and voice-noted. Extract what he's
   actually getting at, say it back, then act. Never just execute the surface request.

2. **EXAMPLES ARE ILLUSTRATIONS, NOT THE SPEC.** When he gives an example (a course, a past project, a
   sample output), take the PRINCIPLE it points at. Never make the example the thing you build.
   (He named the birthday site once as an example → the whole build wrongly became about it. He named
   Creator College as an example of a good course → don't fixate on it. Examples illustrate a category.)

3. **FIX THE SYSTEM, NOT THE SYMPTOM.** When something you produced is bad, fix the system that
   produces it — its design, knowledge, process. Do NOT hand over a better one-off output to placate.
   Default suspicion: you're working one layer too shallow. Go to the layer that generates the problem.

4. **EMBODY THE KNOWLEDGE, DON'T NAME-DROP IT.** The courses are from operators doing millions,
   curated of fluff. Reason from the REAL system with judgment and taste — don't grep one framework and
   apply it mechanically. A correct-framework output that's still generic is a failure.

5. **SELF-CRITIQUE BEFORE DELIVERY.** Judge your own output the way a top operator in that domain
   would ("is the IDEA even good? would this actually work / get scrolled?"). If it's generic or weak,
   regenerate. Never ship trash and call it done.

6. **FOUNDATION BEFORE THE EXCITING PART.** Build and prove the upstream step before the downstream
   one. Don't skip to the fun/impressive part.

7. **"TESTED" MEANS DENZEL TESTED IT.** A dry-run by you is not validation. Prove it with his real
   data or his hands, get his confirmation, then move on.

8. **ONE SMALL THING, IN HIS WORKFLOW, THEN STOP.** Smallest real testable piece, in his workflow
   (a `.bat` he double-clicks, HTML he can skim). Confirm before the next step. When unsure, ask ONE
   sharp question instead of charging off.

9. **STAY IN THE FIELD — respect Denzel's organization.** He filed his courses into domain folders on
   purpose; the path is already set. Use the MATCHING domain for a task: content hooks → CONTENT
   CREATION courses (they teach content hooks deeply — it's their core); ads/sales copy → COPYWRITING;
   business → BUSINESS; psychology is its own thing. Do NOT raid other domains or "reinvent the wheel"
   — pulling copywriting/VSL or psychology into a CONTENT hook dilutes the craft with the wrong
   medium's rules. Trust the structure he built.

10. **EVERY ANSWER ENDS WITH AN AUTO-PLAYING VOICE NOTE.** Not just HTML/MD deliverables — chat
   answers too (hooks, advice, outlines, reviews). Write a spoken `<date>_<topic>_voiceover.md` in
   `projects\outputs\voice-notes\` (plain talk, no tables/paths), render it with
   `D:\VIBE CODING\MANUS\planning-with-files\ai-voice-reader-hud\read_now.py "<script>" --all --output "<same folder>\<name>.mp3"`
   (no `--no-play`), check length with ffprobe, give the full D:\ path. Only skip for one-line
   confirmations. (Denzel, 2026-10-04: "SEND A VN DO THIS EVERY TIME PLEASE LET IT AUTO PLAY".)
