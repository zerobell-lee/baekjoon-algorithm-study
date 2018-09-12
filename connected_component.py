#Q : 11724


import sys
from collections import deque


def bfs(l, i):
    global check
    q = deque()

    check[i] = True
    q.append(i)

    while len(q):
        x = q.popleft()
        for j in l[x]:
            if not check[j]:
                check[j] = True
                q.append(j)


n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for i in range(n+1)]
check = [False for i in range(n+1)]
check[0] = True

for i in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[v].append(u)
    graph[u].append(v)

for i in graph:
    i.sort()

cnt = 0

while True:
    toContinue = False
    for (i, e) in enumerate(check):
        if not e:
            toContinue = True
            cnt += 1
            bfs(graph, i)
    if not toContinue:
        break

sys.stdout.write(str(cnt))