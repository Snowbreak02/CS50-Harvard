from tabulate import tabulate
import sys
import csv


if len(sys.argv) == 2 :
    input = str(sys.argv[1]).lstrip()
    if input.endswith(".csv"):
        counter = 0
        try:
            with open(input, "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    table.append(row)

            print(tabulate(table, headers, tablefmt="grid"))

        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)
    elif ".csv" not in sys.argv[1]:
        print("Not a CSV file")
        sys.exit(1)
elif len(sys.argv) < 2:
    print("Too few command-line argument")
    sys.exit(1)

else:
    print("Too many command-line arguments")
    sys.exit(1)

