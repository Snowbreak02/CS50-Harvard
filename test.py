p1_name = input("\nName of first player: ").strip()
p2_name = input("\nName of second player: ").strip()


while True:
    p1_name = input("\nName of first player: ").strip()
    p2_name = input("\nName of second player: ").strip()
    try:

    except:
        if p1_name == p2_name:
            print("Enter names again")
        break

print(f"\n'{p1_name}' and '{p2_name}' will be playing against each other!⚔️")
