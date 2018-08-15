import sys


num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

D = [[1, 1] for i in range(num)]

for i in range(num):
    for j in range(i):
        if arr[j] < arr[i] and D[j][0] >= D[i][0]:
            D[i][0] = D[j][0] + 1
#        if arr[num-1 - j] < arr[num-1 - i] and D[num-1 - j][0] >= D[num-1 - i][0]:
#            D[num-1 - i][1] = D[num-1 - j][1] + 1

for i in range(num-1, -1, -1):
    for j in range(num-1, i-1, -1):
        if arr[j] < arr[i] and D[j][1] >= D[i][1]:
            D[i][1] = D[j][1] + 1

max_value = 0

for i in range(num):
    max_value = max(max_value, sum(D[i]) - 1)

sys.stdout.write(str(max_value))