import sys


def gcd(a, b):
    if b > a:
        a, b = b, a
    if b==0:
        return a
    return gcd(b, a%b)


a, b = map(int, sys.stdin.readline().rstrip().split())

sys.stdout.write(str(gcd(a, b)))