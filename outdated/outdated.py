while True:
    in_date = input("Date: ")
    try:
        month, date, year = in_date.split("/")
        if (month <= 12, month >= 1, date<= 31, date >= 1)

    except (ValueError):
        pass

    perc = f * 100

    if perc <= 1:
        print("E")
    elif perc >= 99:
        print("F")
    else:
        print(f"{round(perc)}%")