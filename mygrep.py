import os
import sys


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", newline="")
    sys.stderr.reconfigure(encoding="utf-8", newline="")

    program = os.path.basename(sys.argv[0])
    if len(sys.argv) != 3:
        print(f"Usage: {program} WORD FILE", file=sys.stderr)
        return 2

    word, filename = sys.argv[1:]

    if os.path.isdir(filename):
        print(f"{program}: {filename}: Is a directory", file=sys.stderr)
        return 2

    try:
        file = open(filename, encoding="utf-8", newline="")
    except FileNotFoundError:
        print(f"{program}: {filename}: No such file", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"{program}: {filename}: {exc.strerror}", file=sys.stderr)
        return 2

    found_match = False
    with file:
        for line in file:
            if word in line:
                found_match = True
                sys.stdout.write(line)
                if not line.endswith("\n"):
                    sys.stdout.write("\n")

    return 0 if found_match else 1


if __name__ == "__main__":
    raise SystemExit(main())
