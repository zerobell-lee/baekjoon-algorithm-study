import sys


def fact(n):
    return n*fact(n-1) if n > 1 else 1


num = int(sys.stdin.readline())
sys.stdout.write(str(fact(num)))