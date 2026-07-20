# mygrep

`mygrep` is a small Python reimplementation of a focused subset of GNU
`grep`. It searches one UTF-8 text file for a literal, case-sensitive term and
prints every matching line.

The project is a practice exercise. GNU grep 3.1 is the behavioral reference
for the features currently implemented.

## Requirements

- Python 3
- No third-party packages

## Usage

```text
python mygrep.py WORD FILE
```

For example:

```text
python mygrep.py dagger test.txt
```

Matching lines are written to standard output in their original order. A
matching final line is terminated with a newline even when the input file does
not end with one, matching GNU `grep`.

Errors and usage information are written to standard error.

## Exit codes

| Code | Meaning |
| ---: | --- |
| `0` | At least one matching line was found. |
| `1` | No matching lines were found. |
| `2` | The arguments were invalid or the file could not be opened. |

## Current scope

Supported:

- One literal search term
- One UTF-8 text file
- Case-sensitive substring matching
- Missing-file and directory errors

Not supported:

- Command-line flags
- Regular expressions
- Multiple input files
- Standard-input searches
- Colored output
- Binary or non-UTF-8 files

## Verification

Compare the output with GNU `grep` for both provided fixtures:

```sh
grep dagger test.txt > real_grep.txt
python mygrep.py dagger test.txt > my_grep.txt
diff real_grep.txt my_grep.txt

grep dagger test_no_eol.txt > real_grep.txt
python mygrep.py dagger test_no_eol.txt > my_grep.txt
diff real_grep.txt my_grep.txt
```

Successful verification produces no `diff` output.
