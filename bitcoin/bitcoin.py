import requests
import sys
import json


if len(sys.argv) == 2:
    try:
        in

else:
    print("Missing command-line argument")
    sys.exit()

except requests.RequestException:
    print("hello.2")