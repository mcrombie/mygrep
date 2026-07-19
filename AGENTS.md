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

## How to verify
    grep <word> test.txt > real.txt
    python mygrep.py <word> test.txt > mine.txt
    diff real.txt mine.txt

Done means `diff` prints nothing.

## Before finishing
State which rules above you followed, and flag anything you added that the
brief did not ask for.