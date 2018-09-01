import sys


m, n = map(int, sys.stdin.readline().rstrip().split())

arr = [True for i in range(n + 1)]

arr[1] = False

for i in range(2, n+1):
    if not arr[i]:
        continue

    for j in range(i*2, n+1, i):
        arr[j] = False


result = ''

for i in range(m, n+1):
    if arr[i]:
        result += '%d\n'%i

sys.stdout.write(result)