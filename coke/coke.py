amt_due = 50

while amt_due >0:
    print("Amount due: ", amt_due)
    inserted = int("Insert coin: ")
    if inserted in [5, 10, 25]:
    change_owed = amt_due - inserted
