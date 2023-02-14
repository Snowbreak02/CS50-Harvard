x = str(input("Greeting: "))
x = x.strip().title()
to_remov = {"A", "E", "I", "O", "U","a", "e", "i", "o", "u"}
for char in to_remov(x):
    new_x = 