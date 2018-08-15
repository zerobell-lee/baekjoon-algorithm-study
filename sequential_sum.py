import sys


num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

D = [0 for i in range(num)]
D[0] = arr[0]

for i in range(1, num):
    D[i] = max(D[i-1] + arr[i], arr[i])

sys.stdout.write(str(max(D)))