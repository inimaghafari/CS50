def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# Checking the plate
def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s.isalnum():
        return False
    if not s[0:2].isalpha():
        return False

    first_number = None

    for i, word in enumerate(s):
        if word.isdigit():
            first_number = i
            break

    if first_number is None:
        return True

    for word in s[first_number:]:
        if not word.isdigit():
            return False

    if s[first_number] == "0":
        return False

    return True


if __name__ == "__main__":
    main()
