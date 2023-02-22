import re

email = input("What's your email? ").strip

if re.search(".+@.+", email): #.:any character except newline/ +: 1 ormore rep/ ?: 0 or 1 reps/ {m,n}:m-n reps
    print("valid")
else:
    print("invalid")