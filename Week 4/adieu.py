import inflect

p = inflect.engine()

def main():
    names = []

    while True:
        try:
            name = input().strip()
        except EOFError:
            break

        if name == "":
            continue

        names.append(name)

    result = p.join(names)
    print("Adieu, adieu, to " + result)


main()
