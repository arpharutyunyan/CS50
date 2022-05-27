camel = input("CamelCase: ")

snake = ""
for i in camel:
    if i.isupper():
        snake = snake + "_" + i.lower()
    else:
        snake += i

print("snake_case: ", snake)