text = input("hello: ")

first_word = text.replace(",", "").lower().split()[0]

# Identifying the letter (h)
def word(text) :
    return text.lower().strip().startswith("h")


if first_word == "hello" :
    print("$0")
elif word(text) :
    print("$20")
else:
    print("$100")
