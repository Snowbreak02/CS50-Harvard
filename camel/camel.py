def main():
    name = input ("What's your name? ")
    name = name.strip().title()
    greeting(name)

def greeting(to="there"):
    print("hello", to)
#to is defined as a value if no name is being called

main()