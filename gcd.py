import sys


def gcd(a, b):
    if b > a:
        a, b = b, a

    def gcd_help(a, b):
        return a if b == 0 else gcd_help(b, a%b)

    return gcd_help(a, b)


a, b = map(int, sys.stdin.readline().rstrip().split())

sys.stdout.write(str(gcd(a, b)))