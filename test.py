while True:
        p1_name = input("Name of first player: ")
        if p1_name.isalpha():
            break
        else:
            print("Please use only letters, try again")

while True:
        p2_name = input("Name of second player: ")
        if p2_name.isalpha() and p2_name != p1_name:
            break
        if p2_name == p1_name:
            print("Please use a different name, try again")
        else:
            print("Please use only letters, try again")


print(f"\n'{p1_name}' and '{p2_name}' will be playing against each other!⚔️")