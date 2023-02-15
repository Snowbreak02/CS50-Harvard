def main():
    x = get_int("Fraction: ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break



main()