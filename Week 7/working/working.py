import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    # If minute = None
    m1 = m1 or "00"
    m2 = m2 or "00"

    # Convert to int
    h1, m1 = int(h1), int(m1)
    h2, m2 = int(h2), int(m2)

    # Checking the time
    if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
        raise ValueError
    if not (0 <= m1 < 60 and 0 <= m2 < 60):
        raise ValueError

    return f"{to_24(h1, m1, p1)} to {to_24(h2, m2, p2)}"


def to_24(hour, minute, period):
    if period == "AM":
        if hour == 12:
            hour = 0

    # PM
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"



if __name__ == "__main__":
    main()
