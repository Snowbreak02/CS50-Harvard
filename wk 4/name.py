import sys

#inputting one name and ensuring its one name and not anymore
"""
if len(sys.argv) < 2:
    print("too few arguements")
elif len(sys.argv) > 2:
    print("too many arguements")
else:
    print("Hi, my name is", sys.argv[1])
"""

if len(sys.argv) < 2:
    sys.exit("too few arguements")

for arg in sys.argv[1:]:
    print("Hi, my name is", arg)