answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
answer = answer.lstrip().rstrip().lower()
if answer == "42":
    print("Yes")
elif answer == "forty two" or answer == "forty-two":
    print("Yes")
else:
    print("No")

