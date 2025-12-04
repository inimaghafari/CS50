import string

def main():
    text = input("hello: ")
    result = value(text)
    print(f"${result}")

def value(greeting):
    cleaned = greeting.strip().translate(str.maketrans("", "", string.punctuation)).lower()

    if cleaned == "hello":
        return 0
    elif cleaned.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":

    main()
