def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    i = 0
    while i < lens(s):
        if s[i].is.alpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i+=1

    for char in s:
        if char 


main()