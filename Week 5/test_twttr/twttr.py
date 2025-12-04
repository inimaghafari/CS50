def main():
    word = input("Input: ")
    print("Output:", shorten(word))

def shorten(word):
    result = ""
    for char in word:
        if char not in "AEIOUaeiou":
            result += char
    return result

if __name__ == "__main__":
    main()
