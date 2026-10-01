
expression = (input("expression: "))

x, op, y = expression.split(" ")
x = int(x)
y = int(y)

if op == "+":
    result = x+y
    print(f"{result:.1f}")
elif op == "-":
    result = x-y
    print(f"{result:.1f}")
elif op == "*":
    result = x*y
    print(f"{result:.1f}")
elif op == "/" and y != 0:
    result = x/y
    print(f"{result:.1f}")
