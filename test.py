p1_name = input("\nName of first player: ").strip()
p2_name = input("\nName of second player: ").strip()
while True:
        p1_name = input("\nName of first player: ").strip()
        p2_name = input("\nName of second player: ").strip()
        if p1_name.isalpha() and p2_name.isalpha():
            break
        else:
            print("Please use only letters, try again")


print(f"\n'{p1_name}' and '{p2_name}' will be playing against each other!⚔️")
