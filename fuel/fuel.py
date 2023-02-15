def main():
    x = get_frac("Fraction: ")
    print(f"x is {}")

def get_frac(prompt):
    while True:
        try:
            fuel = input(prompt)
            numerator, denominator = fuel.split("/")
            new_num = int(numer)
            new_deno = int(deno)
            f = new_num/new_deno
            if f <= 1:
                break

        except (ValueError, ZeroDivisionError):
            pass




main()