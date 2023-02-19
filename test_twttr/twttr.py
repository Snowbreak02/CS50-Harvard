"""
x = str(input("Greeting: "))

for char in ["A", "E", "I", "O", "U","a", "e", "i", "o", "u"]:
    if char in x:
        x = x.replace(char,"")

print(x)
"""

def main():
    message = input("Input: ")
    msg_wo_vowels = shorten(message)
    print("Output: " + msg_wo_vowels)


def shorten(word):
    wo_vowels = ""
    for letter in word:
        if not letter.lower() in ["a", "e", "i", "o", "u"]:

            wo_vowels += letter
    return wo_vowels


if __name__ == "__main__":
    main()