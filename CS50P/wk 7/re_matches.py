import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), ?(.+)$", name) # ?: means the left side is optional, if have then ok,if not there its fine
if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")