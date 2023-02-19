"""
while True:
    fuel = input("Fraction: ")
    try:
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
    print(f"{round(perc)}%")
"""

def main():
    fuel = input("Fraction: ")
    frac_conv = convert(fuel)
    output = gauge(frac_conv)
    print(output)

def convert(fuel):
      while True:
        try:
            numerator, denominator = fuel.split("/")
            new_num = int(numerator)
            new_deno = int(denominator)
            f = new_num/new_deno
            if f <= 1:
                p = float(f*100)
                return p
            else:
                fuel = input("Fraction: ")
                pass

        except (ValueError, ZeroDivisionError):
            raise


def gauge(perc):

    if perc <= 1:
        return "E"
    elif perc >= 99:
        return "F"
    else:
        return (f"{round(perc)}%")


if __name__ == "__main__":
    main()