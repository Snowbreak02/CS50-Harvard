import inflect

p = inflect.engine()

names = []

while True:
    try:
        in_name = input("Name: ")
        names.append(in_name)

    except EOFError:
        print()
        break

print(names)







