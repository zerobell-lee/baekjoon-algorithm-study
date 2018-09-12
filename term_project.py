# Q: 9466


import sys


def search(x, cnt, s):
    global graph
    global check
    global step

    while True:
        if check[x] != 0:
            if s != step[x]:
                return 0
            return cnt - check[x]

        check[x] = cnt
        step[x] = s
        x = graph[x]
        cnt += 1


num = int(sys.stdin.readline())
sys.setrecursionlimit(100000)

for i in range(num):
    size = int(sys.stdin.readline())
    graph = [0]
    graph.extend(list(map(int, sys.stdin.readline().rstrip().split())))
    check = [0 for j in range(size + 1)]
    step = [0 for j in range(size + 1)]

    ans = 0
    for j in range(1, size+1):
        if check[j] == 0:
            ans += search(j, 1, j)
    sys.stdout.write('%d\n' % (size-ans))
