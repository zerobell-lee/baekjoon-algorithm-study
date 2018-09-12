# Q :2331


import sys


def calc(num):
    global p
    num_arr = []
    while num != 0:
        num_arr.append(num%10)
        num //= 10

    result = 0
    for x in num_arr:
        result += x**p

    return result


a, p = map(int, sys.stdin.readline().rstrip().split())

graph = [a]
border = -1

while True:
    val = calc(graph[-1])
    for (i, e) in enumerate(graph):
        if val == e:
            border = i
            break
    if border != -1:
        break
    else:
        graph.append(val)

sys.stdout.write(str(border))