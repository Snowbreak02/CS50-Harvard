import re

email = input("What's your email? ").strip

if re.search(".+@.+", email): #.:any character ex
    print("valid")
else:
    print("invalid")