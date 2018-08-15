import sys


num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

D = [1 for i in range(num)]

for i in range(num):
    for j in range(i, -1, -1):
        if arr[j] > arr[i] and D[j] >= D[i]:
            D[i] = D[j] + 1

sys.stdout.write(str(max(D)))