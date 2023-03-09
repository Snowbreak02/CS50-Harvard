names = []

with open("names.txt") as file: #a is for append, adding the names to the list. w is to overwrite and replace old value with new value
    for line in file:
        names.append(line.rstrip())

for name in sorted (names):
    print(f"Hello, {name}")