import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.lower().endswith(".py"):
    sys.exit("Not a Python file")

count = 0
in_docstring = False

try:
    with open(filename) as file:
        for line in file:
            stripped = line.strip()

            if stripped.startswith("#"):
                continue

            if not stripped:
                continue

            count += 1

except FileNotFoundError:
    sys.exit("File does not exist")

print(count)
