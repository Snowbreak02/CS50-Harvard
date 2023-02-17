import random

while True:
    try:
        lvl = int(input("Level: "))
        if lvl > 0:
            break
        else:
            pass
    except ValueError:
        pass