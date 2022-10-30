"""
    One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David 
    to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , 
    David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for 
    the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

    In a file called professor.py, implement a program that:

    Prompts the user for a level, . If the user does not input 1, 2, or 3, the program should prompt again.
    Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with  digits. No need to support 
    operations other than addition (+).
    Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt the 
    user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should output 
    the correct answer.
    The program should ultimately output the user’s score, a number out of 10.
    Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, 
    and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
"""

import random


def main():

    level = get_level()
    count = 0
    incorrect = 0
    for i in range(10):
        x, y = generate_integer(level)

        while True:

            try:
                for i in range(3):
                    print(f"{x} + {y} = ", end = "")
                    answer = int(input())
                    if answer == (x +y):
                        count += 1
                        break
                    else: print("EEE")
                else:
                    print(f"{x} + {y} = {x + y}")
                break
            except ValueError:
                print("EEE")
                incorrect += 1
                if(incorrect == 3):
                    print(f"{x} + {y} = {x + y}")
                    break
                continue
    print(f"Score: {count}")





def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
            continue
        except ValueError:
            continue


def generate_integer(level):

    if level == 1:
        x = random.randrange(0, 10)
        y = random.randrange(0, 10)
    elif level == 2:
        x = random.randrange(10, 100)
        y = random.randrange(10, 100)
    else:
        x = random.randrange(100, 1000)
        y = random.randrange(100, 1000)

    return x, y


if __name__ == "__main__":
    main()