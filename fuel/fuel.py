def main():
    x = get_int("Fraction ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            pass
        else:
            return x    #return will break out of the loop


main()