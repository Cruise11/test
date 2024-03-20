input_str = input()
stack = []
output = ""

for char in input_str:
    if char == "(":
        stack.append("(")
    elif char == ")":
        if stack:
            stack.pop()
        else:
            output += "?"
    else:
        output += char

for _ in stack:
    output += "x"
print(output)