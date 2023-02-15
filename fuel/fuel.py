while True:
    fuel = input("Fraction: ")
    try:
        numerator, denominator = fuel.split("/")
        new_num = float(numerator)
        new_deno = float(denominator)
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
    print(f"{int(perc)}%")

