menu = {"Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00}

total_amt = 0

while True:
    try:
        item = input("Item: ").lower().title().strip()
        if item in menu:
            total_amt += menu[item]
            formated = "{:.2f}".format(total_amt)
            print(f"Total: $",formated,sep="")

    except EOFError:
        print()
        break
