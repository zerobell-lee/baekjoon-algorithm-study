import sys


def to_deci(arr, a):
    value = 0
    for e in arr:
        value = value * a + e
    return value


def to_b(num, b):
    stack = []
    while num > 0:
        stack.append(str(num % b))
        num = num // b

    stack.reverse()
    return ' '.join(stack)


a, b = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

sys.stdout.write(to_b(to_deci(arr, a), b))
