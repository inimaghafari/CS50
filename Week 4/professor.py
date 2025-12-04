import random

def main():
    level = get_level()
    score = 0

    #Give score
    for _ in range(10):
        if ask_question(level):
            score += 1

    print(f"Score: {score}")

#Get level
def get_level():
    while True:
        try:
            user_input = input("Level: ").strip()
            level = int(user_input)
            if level not in [1, 2, 3]:
                raise ValueError
            return level
        except ValueError:
            continue

#Get random number & choice level
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

#Calculate
def ask_question(level):
    x = generate_integer(level)
    y = generate_integer(level)
    answer = x + y

    for _ in range(3):
        try:
            user_input = input(f"{x} + {y} = ").strip()
            user_answer = int(user_input)
            if user_answer == answer:
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")


    print(f"{x} + {y} = {answer}")
    return False


if __name__ == "__main__":
    main()
