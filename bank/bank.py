x = str(input("Greeting: "))
x = x.strip().title()
if "Hello" in x:
    print("$0")
elif "H" in x:
    print("$20")
else:
    print("$100")
