import random


def main():
    level = get_level()


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl = [1,2,3]:
                return lvl
        except:
            pass

def generate_integer(level):
    if level == 1:
        rng_x = random.randint(0,9)
        rng_y = random.randint(0,9)
    elif level == 2:
        rng_x = random.randint(10,99)
        rng_y = random.randint(10,99)
    else:
        rng_x = random.randint(100,999)
        rng_x = random.randint(100,999)
        
    return rng_x,rng_y


if __name__ == "__main__":
    main()