num = int(input())
stack = []

for i in range(num):
    line = input().split()
    if line[0]=='push':
        stack.append(int(line[1]))
    elif line[0]=='pop':
        if len(stack)==0:
            print('-1')
        else:
            print(stack[len(stack)-1])
            del stack[len(stack)-1]
    elif line[0]=='top':
        if len(stack)==0:
            print('-1')
        else:
            print(stack[len(stack)-1])
    elif line[0]=='size':
        print(len(stack))
    elif line[0]=='empty':
        print('1'if(len(stack)==0) else '0')