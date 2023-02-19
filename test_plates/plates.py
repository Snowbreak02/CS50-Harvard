def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def middle_char(txt):
    return txt[(len(txt)-1)//2:(len(txt)+2)//2]

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    if middle_char(s).isnumeric() == True:
        return False

    length = len(s)

    if not s.isalnum():
        return False
    if not s[0:2].isalpha():
        return False
    if not 2 <= length <= 6:
        return False

    i = 0

    while i < length - 1:
        if not s[i].isalpha():
            if s[i] == "0":
                return False
            elif not s[i:].isdigit():
                return False
            else:
                return True
        i += 1

    return True

    for char in s:
        if char in [".", "!", " ", "?"]:
            return False
    return True

if __name__ == "__main__":
    main()