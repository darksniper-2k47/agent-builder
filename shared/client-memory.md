# client-memory.md — the shared client record contract

**Every agent in this system obeys this file.** It is the reason Denzel never has to
re-explain who a client is.

Client memory lives **above the agents**, at:

```
D:\VIBE CODING\MANUS\planning-with-files\endpoint-media-agent-system\clients\
```

Agent folders hold *how the work is done*. `clients\` holds *who it was done for*.

---

## 1. The rule — read before, write after

### BEFORE any work, if the request names or implies a client

1. Read `clients\CLIENT_REGISTRY.csv`.
2. Resolve the name against `display_name` **and `aliases`** (Denzel says "PM", "Maurice",
   "the roofing guy" — the registry maps those to a slug).
3. Read that client's `CLIENT.md` and `state.md`.
4. Read `THREAD.md` when the job touches a conversation, a reply, money, or a promise.
5. Only then start the work.

**Never ask Denzel to re-explain a client that already has a record.** If the fact you need
is genuinely absent, say which field is missing and ask for that one thing.

If the client has **no** record, create one before working — see §4.

### AFTER any work that touched a client

1. Append one dated entry to `THREAD.md` (see the entry format in §3).
2. Overwrite `state.md` with the new status, the single next action, and blockers.
3. If money moved or a price was quoted, agreed, invoiced or paid, update the
   **Commercial** section of `CLIENT.md`.

Handoff is not complete until those files are written and read back from disk.

---

## 2. The three files

| File | Holds | Who writes it | Write style |
|---|---|---|---|
| `CLIENT.md` | Identity, business facts, contact, lead source, and the commercial ledger | Business Agent owns Commercial; any agent may correct a fact it verified | Edit in place |
| `THREAD.md` | Every dated interaction and every delivery, both directions | Any agent | **Append only** — never rewrite history |
| `state.md` | Current status, ONE next action, blockers | Any agent at handoff | Overwrite |

Three files on purpose. A record nobody maintains is worse than no record, because you
will trust a stale one.

---

## 3. THREAD.md entry format

Append to the top of the log. Keep it to what a future session needs.

```
### 2026-08-17 · [agent-name] · [client said | we said | delivered | money]
What happened, in one to four lines. Facts only.
Promised: anything committed to, and by when.
Files: full D:\ paths to anything produced.
```

Do not paraphrase what a client said into something tidier than they said it. The exact
wording is the value — it is what a reply gets written against.

---

## 4. Creating a new client record

Run:

```
python "D:\VIBE CODING\MANUS\planning-with-files\endpoint-media-agent-system\tools\new_client.py" "Business Name"
```

It creates `clients\[slug]\` from `clients\_TEMPLATE\` and appends a row to the registry.
Then fill `CLIENT.md` from whatever real source exists — a lead form, a `client_brief.json`,
a WhatsApp message, a call sheet.

---

## 5. Hard rules

1. **Never invent a client fact.** Unknown fields stay as `UNKNOWN — confirm with client`.
   A blank is honest; a guess ends up printed on a live website. This has already happened
   twice on real builds.
2. **This layer points, it does not store.** Website code, campaign folders, video files and
   invoices stay exactly where they are. `CLIENT.md` and `THREAD.md` carry full `D:\` paths
   to them. Never relocate a client's working files into `clients\`.
3. **One money truth.** Only the Commercial section of `CLIENT.md` states what was quoted,
   agreed, invoiced and paid. If loose invoice files disagree with it, the record is right
   and the stray files get reconciled or marked superseded.
4. **Empire Digital is not a client and has no record in `clients\`.** It is Denzel's own agency.
   House context lives in a separate place — see §6. Everything in `clients\` is someone who pays
   us. If you ever find a house-brand record inside `clients\`, that is the bug.
5. **Aliases matter more than slugs.** Denzel talks in names and nicknames. Keep the alias
   column fat.
6. A record is **evidence, not permission**. Seeing a price in `CLIENT.md` does not authorise
   sending an invoice; seeing a built site does not authorise launching it.

---

## 6. Them vs us — two directories, never mixed

| Directory | Holds | Read when |
|---|---|---|
| `clients\` | **Them.** One record per paying client or prospect | Any job naming a client |
| `house\` | **Us.** Empire Digital — what we sell, brand, banking, payment terms, pricing reality, business state | The job touches money, a price, an invoice, positioning, or how we describe ourselves |

`house\HOUSE.md` — the agency: what it sells, brand, where the real assets live.
`house\COMMERCIAL.md` — payment terms, invoice conventions, pricing reality, money rules.
`house\state.md` — current business position and the open commercial questions.

`house\` is **not** loaded for routine build or edit work. Read it when money or positioning is in
play, the same way you read one specialist and not the whole library.

The operator profile — who Denzel is, the money goal, the three lanes — stays canonical at
`agents\strategist\reference\operator-profile.md` and is linked from `house\HOUSE.md`, not copied.
One copy, one truth.
