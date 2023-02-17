import random

while True:
    try:
        lvl = input(int("Level: "))
        if lvl > 0:
            break
        else:
            pass
    except EOFError:
        pass