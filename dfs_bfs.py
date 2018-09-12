# Q:1260

import sys
from collections import deque


def dfs(l, i):
    global check

    check[i] = True
    sys.stdout.write('%d ' % i)

    for j in l[i]:
        if not check[j]:
            check[i] = True
            dfs(l, j)


def bfs(l, i):
    global check

    q = deque()

    check[i] = True
    q.append(i)

    while len(q):
        x = q.popleft()

        sys.stdout.write('%d ' % x)

        for j in l[x]:
            if not check[j]:
                check[j] = True
                q.append(j)


sys.setrecursionlimit(10000)
n, m, v = map(int, sys.stdin.readline().rstrip().split())

ad_list = [[] for i in range(n+1)]
check = [False for i in range(n+1)]
resultStr = ''
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if b not in ad_list[a]:
        ad_list[a].append(b)
    if a not in ad_list[b]:
        ad_list[b].append(a)

for i in ad_list:
    i.sort()

dfs(ad_list, v)
sys.stdout.write('\n')

check = [False for i in range(n+1)]
bfs(ad_list, v)



