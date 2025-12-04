import random

# Determine the level
while True:
    try:

        level = int(input("Level: "))
        if level < 1:
            continue
        else:
            break

    except ValueError:
        continue

# Randomize level
r = random.randint(1, level)

# Game code
while True:
    try:

        guess = int(input("Guess: "))

        if guess < 1:
            continue
        elif guess > r:
            print("Too large!")
            continue
        elif guess < r:
            print("Too small!")
            continue
        elif guess == r:
            print("Just right!")
            break

    except ValueError:
        continue
