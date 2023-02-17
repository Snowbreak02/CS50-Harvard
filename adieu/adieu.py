import inflect

names = {}

while True:
    try:
        in_name = input("Name: ")
        if in_name in names:
            break
        else:
            in_name += names

    except EOFError:
        print()
        break

print({names})







