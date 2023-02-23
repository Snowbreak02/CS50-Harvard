import re


url = input("URL: ").strip()

matches = re.search(r"^(https://|www\.)twitter\.com/(.+)$", url, re.IGNORECASE) # "?:" means dont capture the stuff in this bracket

if matches:
    print(f"Username: ", matches.group(1))


