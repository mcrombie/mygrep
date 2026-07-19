# Brief 01 — plain literal match

## Goal
Take a word and a filename, print every line containing that word.

## Run as
    python mygrep.py hello test.txt

## In scope
Literal substring matching, case-sensitive. One term, one file.
Print matching lines unchanged.

## Out of scope
Flags, regular expressions, multiple files, stdin, colored output.

## Done when
`diff` shows nothing against real grep on test.txt.
