def main():
    x = get_frac("Fraction: ")
    print(f"x is {x}")

def get_frac(prompt):
    while True:
        try:
            x = int(input(prompt))
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break



main()