import sys
import math


def prime(n):
    if n <= 1:
        return False

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i == 0) and (i != n):
            return False

    return True


num = int(sys.stdin.readline())
cnt = 0

for e in list(map(int, sys.stdin.readline().rstrip().split())):
    if prime(e):
        cnt += 1

sys.stdout.write(str(cnt))