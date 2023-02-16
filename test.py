import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://www.nike.com/sg/launch/t/womens-air-jordan-1-game-royal-and-varsity-maize")
print(json.dumps(response.json(), indent=2))
"""
o = response.json()
for result in o["results"]:
    print(result["nikeSize"])