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
    while True:
        fuel = input("Fraction: ")
        fraction = convert(fuel)


def convert(fraction):
     try:
        numerator, denominator = fuel.split("/")
        new_num = int(numerator)
        new_deno = int(denominator)
        f = new_num/new_deno
        if f <= 1:
            break

    except (ValueError, ZeroDivisionError):
        pass


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()