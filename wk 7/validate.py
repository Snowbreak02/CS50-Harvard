import re

email = input("What's your email? ").strip


# .:any character except newline/ +: 1 ormore rep to the thing to the left/ ?: 0 or 1 reps/ {m,n}:m-n reps
# r allows some charcters to be some characters like \ to not be rec as a special char(if special char in the dict then bobian)
# [^@]: any character except the @ sign
# \w is alphanumeric:a-z,A-Z,0-9
if re.search(r"^\w+@[a-zA-Z0-9].+\.(edu|com|gov|sg)$", email):
    print("valid")
else:
    print("invalid")