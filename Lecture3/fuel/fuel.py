"""
    Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that 
    a tank is 50% full, and 3/4 indicates that a tank is 75% full.

    In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, 
    and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead 
    to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

    If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) 
    Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""

while True:

    try:
        exp = input("Fraction: ").split("/")

        if len(exp) > 1:
            if "." in exp[0] or "." in exp[1]:
                raise ValueError

        exp[0] = float(exp[0])
        exp[1] = float(exp[1])

        if exp[0] > exp[1] and exp[1] != 0:
            raise ValueError

        res = round(exp[0] / exp[1] * 100)

        if res >= 99:
            print("F")
            break
        elif res <= 1:
            print("E")
            break
        else:
            print(str(int(res)) + "%")
            break

    except ValueError:
        continue

    except ZeroDivisionError:
        continue

################## test_fuel###############
# def main():
#     while True:
#         try:
#             fraction = input("Fraction: ")
#             percentage = convert(fraction)
#             res = gauge(percentage)
#             print(res)

#         except ValueError:
#             continue

#         except ZeroDivisionError:
#             continue


# def convert(fraction):

#     fraction = fraction.split("/")

#     fraction[0] = int(fraction[0])
#     fraction[1] = int(fraction[1])

#     if fraction[0] > fraction[1] and fraction[1] != 0:
#         raise ValueError

#     res = int(round(fraction[0] / fraction[1] * 100))

#     return res



# def gauge(percentage):
#     if percentage >= 99:
#         return "F"
#     if percentage <= 1:
#         return "E"
#     return f"{percentage}%"


# if __name__ == "__main__":
#     main()