import sys


def lcm(a, b):
    if b > a:
        a, b = b, a

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

    g = gcd(a, b)
    return a * b // g


num = int(sys.stdin.readline())
result = ''

for i in range(num):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    result += str(lcm(a,b)) + '\n'

sys.stdout.write(result)