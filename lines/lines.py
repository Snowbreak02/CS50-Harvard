import sys

if len(sys.argv) == 1 :
    input = str(sys.argv)
    if input.endswith(".py"):
        try:
            print("Finding")
        except:
            print("File does not exist")
            sys.exit(1)
else:
    print("Too few command-line argument")
    sys.exit(1)