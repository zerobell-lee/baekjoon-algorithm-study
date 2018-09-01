import sys
import math


num = int(sys.stdin.readline())

if num == 1:
    exit()

sqrt_n = math.floor(math.sqrt(num))

for i in range(2, sqrt_n + 1):
    while num%i == 0:
        sys.stdout.write(str(i) + '\n')
        num //= i

if num > 1:
    sys.stdout.write(str(num))