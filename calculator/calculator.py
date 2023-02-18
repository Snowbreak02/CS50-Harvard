def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dolla = d.replace("$","")
    return float(dolla)

def percent_to_float(p):
    perc = p.replace("%","")
    per_dec = float(perc)/100
    return per_dec

main()