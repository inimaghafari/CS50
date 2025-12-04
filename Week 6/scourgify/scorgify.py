import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")


before = sys.argv[1]
after = sys.argv[2]

students = []

try:
    with open(before) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(", ")
            house = row["house"]
            students.append({"first": first, "last": last, "house": house})

    with open(after, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(students)
except FileNotFoundError:
    if sys.argv[1] != "before.csv":
        sys.exit(f"Could not read {sys.argv[1]}" )
    if sys.argv[2] != "after.csv":
        sys.exit(f"Could not read {sys.argv[2]}" )
