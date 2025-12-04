text = input("write something: ")
result = ""

for i in text:
    if i.isupper() and result:
        result += "_"
    result += i

print(result.lower())
