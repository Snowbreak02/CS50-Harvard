x = str(input("Greeting: "))
x = x.strip().title()
if "Hello" in x:
    print("$0")
elif x.startswith("H"):
    print("$20")
else:
    print("$100")
