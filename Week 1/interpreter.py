text = input("Enter expression (x y z): ")

x, y, z = text.split()
x = int(x)
z = int(z)

if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z
else:
    print("Invalid operator!")
    exit()

print(float(round(result, 1)))
