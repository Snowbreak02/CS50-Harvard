answer = input("Expression: ")

x, y, z = answer.split(" ")

x1 = float(x)
z1 = float(z)

if y == "+":
    answer = x1 + z1
if y == "/":
    answer = x1 / z1
if y == "-":
    answer = x1 - z1
if y == "*":
    answer = x1 * z1
print (answer)

