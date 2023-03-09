"""
x = str(input("Greeting: "))
x = x.strip().title()
if "Hello" in x:
    print("$0")
elif x.startswith("H"):
    print("$20")
else:
    print("$100")
"""
def main():
    greeting = str(input("Greeting: "))
    final_val = value(greeting)
    print("$",final_val, sep="")

def value(greeting):
    greeting = greeting.strip().title()
    if "Hello" in greeting:
        return 0
    elif greeting.startswith("H"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()