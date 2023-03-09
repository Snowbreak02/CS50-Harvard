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
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    bitcoin = response['bpi']['USD']['rate_float']
    total_amt = bitcoin * input
    print(f"${total_amt:,.4f}")
except requests.RequestException:
    print("Request error")
    sys.exit(1)