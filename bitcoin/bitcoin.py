import requests
import sys
import json


if len(sys.argv) == 2:
    try:
        input = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

