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
    in_date = input("Date: ").replace("/n","")
    try:
        month, date, year = in_date.split("/")
        if (int(month) <= 12 and int(month) >= 1 and int(date) <= 31 and int(date) >= 1):
            break

    except:
        try:
            ol_month, ol_date, year = date.split(" ")
            for i in range(len(months)):
                if ol_month == months[i]:
                    month = i + 1
            day = ol_date.replace(",","")
            if (int(month) <= 12 and int(month) >= 1 and int(date) <= 31 and int(date) >= 1):
                break
        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(date):02}")


