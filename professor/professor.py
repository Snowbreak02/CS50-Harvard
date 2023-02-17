import random


def main():
    level = get_level()
    score_T = score_total(level)
    print("Score: ",score_T)

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

def rounds(rng_x,rng_y)L
    tries = 1
    while tries < 4:
        try:
            ans = int(input(f"{rng_x} + {rng_y} = "))
            if ans == (rng_x+rng_y):
                return True
            else:
                tries +=1
                print("EEE")
        except:
            tries +=1
            print("EEE")
    print (f"{rng_x} + {rng_y} = {rng_x+rng_y}")
    return False

def score_total(level):
    round = 1
    score = 0
    while round < 11:
        rng_x,rng_y = generate_integer(level)
        output = rounds(rng_x,rng_y)
        if output ==True :
            score+=1
        round +=1
    return score

if __name__ == "__main__":
    main()