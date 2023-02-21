import sys


if len(sys.argv) == 3 :
    input = str(sys.argv[1]).lstrip()
    if input.endswith(".csv"):
        try:



        except FileNotFoundError:
            print(f"Could not read {sys.argv[1]}")
            sys.exit(1)

    elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        print("Not a CSV file")
        sys.exit(1)
elif len(sys.argv) < 3:
    print("Too few command-line argument")
    sys.exit(1)

else:
    print("Too many command-line arguments")
    sys.exit(1)

