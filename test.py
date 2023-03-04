
def main():
    p1_name = input("\nName of first player: ").strip()
    p2_name = input("\nName of second player: ").strip()
    p1_named, p2_named = check_player_names(p1_name, p2_name)

def check_player_names(p1_name, p2_name):
    while True:
            if p1_name.isalpha():
                p1_named = p1_name
                break
            else:
                print("Please use only letters, try again")
                pass

    while True:
            if p2_name.isalpha() and p2_name != p1_name:
                p2_named = p2_name
                break
            if p2_name == p1_name:
                print("Please do not use the same names!")
                pass
            else:
                print("Please use only letters, try again")
                pass

    print(f"\n'{p1_named}' and '{p2_named}' will be playing against each other!⚔️")
    return p1_named, p2_named

if __name__ == "__main__":
      main()