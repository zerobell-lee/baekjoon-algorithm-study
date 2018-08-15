stack = []
result = 0

line = list(input())
laser = False
for i, e in enumerate(line):
    if e == '(':
        laser = False
        stack.append(e)
    else:
        if laser:
            result += 1
            stack.pop()
        else:
            laser = True
            stack.pop()
            result += len(stack)

print(result)