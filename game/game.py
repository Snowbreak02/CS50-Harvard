import random

while True:
    try:
        lvl = int(input("Level: "))
        if lvl > 0:
            rng = random.randint(1,lvl)
            while True:
                guess = int(input("Guess: "))
                if guess > rng:
                    print("Too large!")
                elif guess < rng:
                    print("Too Small!")
            except guess == rng:
                print("Just right!")
                break
    except:
        pass