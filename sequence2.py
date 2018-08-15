import sys


num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

D = [0 for i in range(num)]

for i in range(num):
    D[i] = arr[i]

for i in range(num):
    last_ind = -1
    for j in range(i, -1, -1):
        if arr[j] < arr[i] and D[j] > D[i] - arr[i]:
            D[i] = D[j] + arr[i]

sys.stdout.write(str(max(D)))
