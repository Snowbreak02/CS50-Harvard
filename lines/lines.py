import sys

if sys.argv.endswith(".py") :
    try:
        input = str(sys.argv[1])
    except:
        print("File does not")
        sys.exit(1)
else:
    print("Too few command-line argument")
    sys.exit(1)