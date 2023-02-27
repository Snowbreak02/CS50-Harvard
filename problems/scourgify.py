import sys
import csv


if len(sys.argv) == 3 :
    input = str(sys.argv[1]).lstrip()
    if input.endswith(".csv"):
        output =[]
        try:
            with open(input, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    split_name = row ["name"].split(",")
                    output.append({'first': split_name[1].lstrip(), 'last': split_name[0], 'house': row["house"]})


        except FileNotFoundError:
            print(f"Could not read {sys.argv[1]}")
            sys.exit(1)
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
            writer.writerow({"first": "first", "last": "last", "house": "house"})
            for row in output:
                writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

    elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        print("Not a CSV file")
        sys.exit(1)
elif len(sys.argv) < 3:
    print("Too few command-line argument")
    sys.exit(1)

else:
    print("Too many command-line arguments")
    sys.exit(1)

