from random import randint

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        continue


rand = randint(1, int(level) + 1)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 0:
            continue
        if guess > rand:
            print("Too large!")
        elif guess < rand:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue



