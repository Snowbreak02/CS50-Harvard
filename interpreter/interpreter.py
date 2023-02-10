answer = input("Expression: ")

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

