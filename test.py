while True:
    try:
        p1_name = input("\nName of first player: ").strip()
        p2_name = input("\nName of second player: ").strip()
assert p1_name != p2_name
    break
    except if p1_name.isdigit() or p2_name.isdigit():
        print("Names must not contain numbers")
    except AssertionError:
        print("The two names cant be the same. Re-enter two unique names!")

print(f"\n'{p1_name}' and '{p2_name}' will be playing against each other!⚔️")
break