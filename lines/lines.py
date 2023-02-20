import sys

if len(sys.argv) == 2 :
    input = str(sys.argv[1]).lstrip()
    if input.endswith(".py"):
        try:
            with open(input) as file:
                 for line in file:
                     if not line.startswith("# "):


        except:
            print("File does not exist")
            sys.exit(1)
    else:
        print("Not a python file")
        sys.exit(1)
elif len(sys.argv) < 2:
    print("Too few command-line argument")
    sys.exit(1)

else:
    print("Too many command-line arguments")
    sys.exit(1)