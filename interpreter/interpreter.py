exp = input("Expression: ")
exp = exp.split(" ")

x = float(exp[0])
z = float(exp[2])
y = exp[1]

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/" and z != 0:
    print(x / z)
