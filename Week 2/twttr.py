text = input("write something: ")

for word in "AEIOUaeiou":
    text = text.replace(word, "")

print(text)
