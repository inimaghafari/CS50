months_dict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    user_input = input("Date: ").strip()

    try:
        if "/" in user_input:
            parts = user_input.split("/")
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])

        else:
            if "," not in user_input:
                continue

            cleaned = user_input.replace(",", "")
            parts = cleaned.split()

            month_text = parts[0].capitalize()
            day = int(parts[1])
            year = int(parts[2])
            month = months_dict[month_text]


        if not (1 <= month <= 12) or not (1 <= day <= 31) or year <= 0:
            continue

    except (ValueError, KeyError, IndexError):
        continue
    else:
        break

print(f"{year}-{month:02}-{day:02}")
