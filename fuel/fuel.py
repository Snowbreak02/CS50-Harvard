def main():
    f = get_frac("Fraction: ")
    perc = f * 100

    if perc <= 1:
        print("E")
    elif perc >= 99:
        print("F")
    else:
        print(f"{perc}")

def get_frac(prompt):
    while True:
        try:
            fuel = input(prompt)
            numerator, denominator = fuel.split("/")
            new_num = int(numerator)
            new_deno = int(denominator)
            f = new_num/new_deno
            if f <= 1:
                return f

        except (ValueError, ZeroDivisionError):
            pass



main()