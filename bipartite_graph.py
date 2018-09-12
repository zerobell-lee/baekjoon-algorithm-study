# Q: 1707


import sys
from collections import deque


def bfs(l):

    global check

    for (i, x) in enumerate(check):
        if i == 0:
            continue
        if not x:
            q = deque()
            check[i] = 1
            q.append(i)

            while len(q):
                x = q.popleft()
                for j in l[x]:
                    if check[j] == check[x]:
                        return False
                    else:
                        if not check[j]:
                            check[j] = 3 - check[x]
                            q.append(j)

    return True


num = int(sys.stdin.readline())

for i in range(num):
    v, e = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for j in range(v+1)]

    for j in range(e):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    check = [0 for j in range(v+1)]
    result = 'YES\n' if bfs(graph) else 'NO\n'
    sys.stdout.write(result)
