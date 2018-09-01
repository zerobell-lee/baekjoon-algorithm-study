import sys


m, n = map(int, sys.stdin.readline().rstrip().split())

arr = [True for i in range(n + 1)]

arr[1] = False
primes = [2]

for i in range(3, n+1, 2):
    if not arr[i]:
        continue

    primes.append(i)

    for j in range(i*3, n+1, i*2):
        arr[j] = False

for i in primes:
    if m <= i <= n:
        sys.stdout.write('%d\n'%i)
