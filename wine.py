import sys

wine = []

num = int(sys.stdin.readline())

for i in range(num):
    wine.append(int(sys.stdin.readline()))


T = [[0 for i in range(2)] for j in range(num+1)]

for i in range(1, num+1):
    T[i][0] = max(T[i-1])
    if i > 1:
        T[i][1] = max(T[i-2][0] + wine[i-1] + wine[i-2], T[i-1][0] + wine[i-1])
    else:
        T[i][1] = wine[i-1]

sys.stdout.write(str(max(T[num])))