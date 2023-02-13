amt_due = 50

while amt_due >0:
    print("Amount due: ", amt_due)
    inserted = int("Insert coin: ")
    if inserted != (5, 10, 25):
        inserted = input("Insert coin: ")
else:
    change_owed = amt_due - inserted
