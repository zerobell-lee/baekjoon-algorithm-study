import sys


def gcd(a, b):
    if b > a:
        a, b = b, a

    def gcd_help(a, b):
        return a if b == 0 else gcd_help(b, a % b)
    return gcd_help(a, b)


num = int(sys.stdin.readline())

result = ''

for i in range(num):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    sum = 0

    for j in range(1, len(arr)):
        for k in range(j + 1, len(arr)):
            sum += gcd(arr[j], arr[k])

    result += '%d\n'%sum

sys.stdout.write(result)