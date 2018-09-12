# Q : 10451


import sys


def dfs(graph, i):
    global check

    if check[i]:
        return

    check[i] = True
    dfs(graph, graph[i])


num = int(sys.stdin.readline())
sys.setrecursionlimit(10000)

for i in range(num):
    size = int(sys.stdin.readline())
    graph = [0]
    graph.extend(list(map(int, sys.stdin.readline().rstrip().split())))
    check = [False for j in range(size + 1)]
    cnt = 0

    for (j, e) in enumerate(check):
        if j == 0:
            continue
        if not check[j]:
            dfs(graph, j)
            cnt += 1

    sys.stdout.write('%d\n' % cnt)