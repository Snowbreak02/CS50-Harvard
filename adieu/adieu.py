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

print("Adieu, adiue, to " + p.join(names))






