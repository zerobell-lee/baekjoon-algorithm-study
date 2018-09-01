import sys


n, k = map(int, sys.stdin.readline().rstrip().split())

P = [[1 if i>0 else 0 for i in range(k + 1)] for j in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        P[i][j] = P[i-1][j] + P[i][j-1]

sys.stdout.write(str(P[n][k] % 1000000000))