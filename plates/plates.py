def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    first = s[0].isalpha() and s[1].isalpha()
    second = len(s) >= 2 and len(s) <= 6
    four = [True for i in s if i.isalpha() or i.isdigit()]
    third = True
    for i in range(2, len(s)-1):
        if s[i].isdigit() and s[i] == "0":
            third = False
            break
        if s[i].isdigit() and not (s[i+1].isdigit()):
            third = False
            break
    return first and second and third and four


main()