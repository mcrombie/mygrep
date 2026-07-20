# Defect Log

Defects in AI-generated code, by platform and brief.

**Caught by:** `read` = spotted while reviewing, before running · `diff` = only
surfaced by comparison against real grep · `assist` = surfaced with AI help,
tagged separately so the read-rate stays honest.

**Status:** `fixed` · `open` = carried forward to a later brief.

Full detail lives in the git diff between each brief's raw-output commit and
its fixes commit.

## Codex — Brief 01: plain literal match

**D1 · skipped stated verification · diff · fixed**
Output did not end with a newline when the input's final line lacked one; real
grep terminates it regardless. The brief defined done as `diff` showing nothing
against real grep, so this should have failed verification before delivery
rather than being handed back as complete.
Fix: reprompted with the required behavior rather than the mechanism. Added a
trailing-newline check after each write.

**D2 · brief gap · read · open**
A missing file raises a Python traceback instead of a readable error message.
The brief never specified error handling. Carried to Brief 02.

**D3 · brief gap · read · open**
Wrong argument count raises an unpacking error rather than a usage message.
Brief never specified. Carried to Brief 02.

**D4 · unrequested scope · assist · reverted**
The reprompt also changed the input `open()` call from `newline=""` to
`newline="\n"`, which was not requested. Effect: files using bare `\r` line
endings are no longer split into lines at all. Harmless in practice, but
unchosen. AGENTS.md instructed the agent to flag unrequested additions —
check whether it did.

**D5 · brief gap · read · fixed**
Goal promised "no Python tracebacks" while Out of scope limited work to five
cases. A file that exists but cannot be read raised an uncaught exception.
Agent followed scope over goal, which was the defensible reading.
Fix: added `except OSError` on open; narrowed the goal to file-access errors;
put binary/non-UTF-8 files explicitly out of scope after confirming they raise
`UnicodeDecodeError` in the read loop, which no `OSError` catch would reach.

### Brief 01 summary
- Reprompts: 1
- Defects: 4 — one model error, two spec gaps, one unrequested change
- Caught by reading: 2 · by diff: 1 · with assistance: 1
- AGENTS.md scope constraints respected: yes, apart from D4\

### Brief 02 summary
- Reprompts: 0
- Defects: 1 — a spec gap; no model errors, no unrequested scope
- Caught by reading: 1 · by diff: 0 · with assistance: 0
- Single commit; no fixes-after-review commit needed
- AGENTS.md gained two rules after Brief 01 (flag additions, ask don't default)
