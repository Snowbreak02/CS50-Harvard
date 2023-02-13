amt_due = 50

while amt_due >0:
    print("Amount Due:", amt_due)
    inserted = int(input("Insert coin: "))

    if inserted in [5, 10, 25]:
        amt_due -= inserted

change_owed = abs(amt_due)
print("Change Owed:",change_owed)