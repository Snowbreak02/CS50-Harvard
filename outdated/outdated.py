months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    in_date = input("Date: ")
    try:
        month, date, year = in_date.split("/")
        if (int(month) <= 12 and int(month) >= 1 and int(date) <= 31 and int(date) >= 1):
            break

    except:
        try:
            ol_month, ol_date, year = date.split(" ")

    perc = f * 100

    if perc <= 1:
        print("E")
    elif perc >= 99:
        print("F")
    else:
        print(f"{round(perc)}%")