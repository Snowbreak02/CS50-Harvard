import inflect

p = inflect.engine()

names = []

while True:
    try:
        in_name = input("Name: ").strip()
        names.append(in_name)

    except EOFError:
        print()
        break

for name in names:
    mylist = p.join((names), final_sep=",")
print(f"Adieu, adieu, to {mylist}")






