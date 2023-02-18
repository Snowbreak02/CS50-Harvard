import requests
import sys
import json

try:
    if len(sys.argv) == 0:
        print("Missing command-line argument")
        sys.exit()
    elif int(sys.argv) > 0:
        print("hello")

    else:
        print("Command-line argument is not a number")
        sys.exit()

except requests.RequestException:
    print("hello.2")