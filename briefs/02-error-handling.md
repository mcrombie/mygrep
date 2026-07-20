# Brief 02 — error handling

## Goal
Handle failure cases the way real grep does: correct exit codes, messages on
the correct stream, and no Python tracebacks reaching the user.

## Cases

**1. File does not exist** — `python mygrep.py dagger nosuchfile.txt`
- stdout: empty · stderr: message naming program and file · exit: 2

**2. Wrong number of arguments** — `python mygrep.py` or `python mygrep.py dagger`
- stdout: empty · stderr: usage message · exit: 2

**3. Path is a directory** — `python mygrep.py dagger .`
- stdout: empty · stderr: message that it is a directory · exit: 2

**4. No matches found** — `python mygrep.py zzzznotfound test.txt`
- stdout: empty · stderr: empty · exit: 1

**5. Matches found** (regression) — `python mygrep.py dagger test.txt`
- stdout: matching lines · stderr: empty · exit: 0

## In scope
The five cases above. Exit codes and stream routing must match real grep exactly.

## Out of scope
- Reading from stdin when no file is given. Real grep does this; mygrep instead
  prints usage and exits 2, per case 2. **Deliberate divergence from the oracle,
  recorded here so it isn't later mistaken for a bug.**
- Matching grep's exact error wording — varies by build. The message must be
  non-empty and on stderr; contents are not compared.
- Any case not listed above. If another failure mode arises, ask rather than
  choosing a default.

## Notes
On Windows, opening a directory may raise `PermissionError` rather than
`IsADirectoryError`. Case 3 must pass on Windows.

## Done when
For each of the five cases, compared against real grep:
- stdout matches exactly
- exit code matches exactly
- stderr is non-empty where the case requires a message, empty where it does not

    grep dagger nosuchfile.txt > real_out.txt 2> real_err.txt ; echo $? > real_code.txt
    python mygrep.py dagger nosuchfile.txt > my_out.txt 2> my_err.txt ; echo $? > my_code.txt
    diff real_out.txt my_out.txt
    diff real_code.txt my_code.txt

Repeat for each case, substituting its arguments. Both `diff`s must print
nothing every time.

Note: case 2 has no real-grep equivalent to compare against, since real grep
reads stdin there. Verify it directly: stderr non-empty, exit code 2.

Brief 01's verification must still pass unchanged.