def main():
    while True:
        try:
            fraction = input("Give me fuel: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                continue
            if x > y:
                continue
            if (x or y) < 0:
                continue

            percent = round(x / y * 100)
            break

        except (ValueError, ZeroDivisionError):
            continue

    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")


main()
