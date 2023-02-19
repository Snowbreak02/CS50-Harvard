"""
x = str(input("Greeting: "))

for char in ["A", "E", "I", "O", "U","a", "e", "i", "o", "u"]:
    if char in x:
        x = x.replace(char,"")

print(x)
"""

#shortening it
def main():
    word = str(input("Greeting: "))

def shorten(word):
    for char in ["A", "E", "I", "O", "U","a", "e", "i", "o", "u"]:
        if char in word:
            x = word.replace(char,"")
            return x

print(x)


if __name__ == "__main__":
    main()