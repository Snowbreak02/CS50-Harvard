def main():

    exp = input("Expression: ")
    answer = convert(exp)

def convert(answer):
    x, y, z = exp.split(" ")
    if y == "+":
        answer = x + z
    if y == "/":
        answer = x / z
    if y == "-":
        answer = x - z
    if y == "*":
        answer = x * z
    return answer

    main()