# Calculate Tip
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Convert Dollars to Float
def dollars_to_float(d):
    d = d.replace("$", "")
    d = float(d)
    return d

# Convert Percent to Float
def percent_to_float(p):
    p = p.replace("%", "")
    p = float(p)
    p = p / 100
    return p


main()
