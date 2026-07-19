# AGENTS.md

## Project
mygrep — a simplified reimplementation of the Unix `grep` command, built as a
practice exercise. Correctness is defined by matching real GNU grep 3.1 output,
not by my judgment.

## Constraints
- Python 3, standard library only. No third-party packages.
- Single file: `mygrep.py`. Do not split into modules.
- Open files with `encoding="utf-8"` explicitly.
- Write `\n` line endings, not `\r\n`. This is a Windows machine.

## Scope
Build only what the current brief asks for. Do not add flags, colored output,
regular-expression support, or multi-file handling unless asked.

If the brief does not say what should happen in some case, ask rather than
choosing. Do not fill gaps with reasonable defaults.

## How to verify
Both files must pass. `test.txt` ends with a newline; `test_no_eol.txt`
deliberately does not.

    grep dagger test.txt > real_grep.txt
    python mygrep.py dagger test.txt > my_grep.txt
    diff real_grep.txt my_grep.txt

    grep dagger test_no_eol.txt > real_grep.txt
    python mygrep.py dagger test_no_eol.txt > my_grep.txt
    diff real_grep.txt my_grep.txt

Done means `diff` prints nothing for both.

## Before finishing
- Run the verification commands above and paste their output. If you did not
  run them, say so explicitly.
- State which constraints above you followed.
- Flag anything you added that the brief did not ask for.