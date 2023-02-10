def main():

    exp = str(print("Expression: "))
    answer = convert(exp)

def convert(answer):
    x, y, z = answer.split(" ")
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