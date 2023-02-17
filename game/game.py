import random

while True:
    try:
        lvl = int(input("Level: "))
        print("value is", lvl)
        break
    
    except (ValueError or lvl < 0):
        pass