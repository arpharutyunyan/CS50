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