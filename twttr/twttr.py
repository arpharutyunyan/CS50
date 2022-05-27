letter = ("a", "e", "i", "o", "u")

phrase = input("Input: ")
for i in phrase:
    if i.lower() in letter:
        phrase = phrase.replace(i, "")
print(f"Output: {phrase}")