text = input("write: ")

result = text.lower()
result2 = result.strip()

match result2:
    case "42" | "forty two" | "forty-two" :
        print("Yes")
    case _:
        print("No")
