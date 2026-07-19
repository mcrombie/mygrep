import sys


def main() -> None:
    word, filename = sys.argv[1:]
    sys.stdout.reconfigure(encoding="utf-8", newline="")

    with open(filename, encoding="utf-8", newline="") as file:
        for line in file:
            if word in line:
                sys.stdout.write(line)


if __name__ == "__main__":
    main()
