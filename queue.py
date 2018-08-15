
N = int(input())
queue = []

for i in range(N):
    lines = input().split(' ')
    if len(lines)>1:
        value = int(lines[1])
        queue.append(value)
    elif lines[0]=='front':
        if len(queue)==0:
            print('-1')
        else:
            print(queue[0])

    elif lines[0]=='back':
        if len(queue)==0:
            print('-1')
        else:
            print(queue[len(queue)-1])

    elif lines[0]=='empty':
        if len(queue)==0:
            print('1')
        else:
            print('0')

    elif lines[0]=='size':
        print(len(queue))

    elif lines[0]=='pop':
        if len(queue)==0:
            print('-1')
        else:
            print(queue[0])
            del(queue[0])