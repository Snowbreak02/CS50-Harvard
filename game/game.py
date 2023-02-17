import random

while True:
    lvl = int(input("Level: "))
    try:
        print("value is ", lvl)

    except (ValueError or lvl < 0):
        pass