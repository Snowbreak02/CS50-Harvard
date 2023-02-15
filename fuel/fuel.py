def main():
    x = get_frac("Fraction: ")
    print(f"x is {x}")

def get_frac(prompt):
    while True:
        try:
            fuel = input(prompt)
            numerator, denominator = fuel.split("/")
            new_num = int(numerator)
            new_deno = int(denominator)
            f = new_num/new_deno
            if f <= 1:
                break

        except (ValueError, ZeroDivisionError):
            pass

    perc = f * 100

    if perc <= 1:
        print("E")
    elif perc >= 99:
        print("F")
    else:
        return perc

main()