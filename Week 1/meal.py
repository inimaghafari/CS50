# Mealtime schedule
def main():
    time = input("What time is it? ")
    t = convert(time)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")


# Clock detection
def convert(time):
    t = time.lower()
    is_pm = "p.m." in t
    is_am = "a.m." in t
    t = t.replace(" a.m.", "").replace(" p.m.", "")
    hours, minutes = t.split(":")
    hours = float(hours)
    minutes = float(minutes)
    if is_pm and hours < 12:
        hours += 12
    if is_am and hours == 12:
        hours = 0
    time_in_hours = hours + minutes / 60
    return time_in_hours



if __name__ == "__main__":
    main()
