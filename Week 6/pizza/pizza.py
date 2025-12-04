from tabulate import tabulate
import csv
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

menu = []

try:

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if sys.argv[1] == "sicilian.csv":
                menu.append([row["Sicilian Pizza"], row["Small"], row["Large"]])
                header = ["Sicilian Pizza", "Small", "Large"]

            if sys.argv[1] == "regular.csv":
                menu.append([row["Regular Pizza"], row["Small"], row["Large"]])
                header = ["Regular Pizza", "Small", "Large"]
                

except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(menu, headers=header, tablefmt="grid"))
