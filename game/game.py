import random

while True:
    try:
        lvl = int(input("Level: "))
        if lvl > 0:
            rng = random.randint(1,lvl)
            print(rng)
    except:
        pass