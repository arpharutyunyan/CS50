"""
    In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
    outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

    Hints
        No need to convert the user’s input to an int if you check for equality with "42", a str, rather than 42, an int!
        It’s okay if your output or the user’s wraps onto multiple lines.
"""

answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
answer = answer.lstrip().rstrip().lower()
if answer == "42":
    print("Yes")
elif answer == "forty two" or answer == "forty-two":
    print("Yes")
else:
    print("No")

