import inflect

names = {}

while True:
    try:
        in_name = input("Name: ")
        names.update({in_name})

    except EOFError:
        print()
        break

print({names})







