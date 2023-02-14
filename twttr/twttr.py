x = str(input("Greeting: "))
x = x.strip().title()

for char in ["A", "E", "I", "O", "U","a", "e", "i", "o", "u"]:
    if char in x:
        x = x.replace(char,"")

print(x)