import random

while True:
    try:
        lvl = int(input("Level: "))
        if lvl > 0:
            break
    except:
        pass

rng = random.randint(1,lvl)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess > rng:
                print("Too large!")
            elif guess < rng:
                print("Too Small!")
            else:
                print("Just Right!")
                break

    except:
        pass