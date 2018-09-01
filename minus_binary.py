import sys
import math


def to_minus_bin(n):
    result = ''
    stack = []
    if n==0:
        return '0'
    while n != 0:
        new_n = math.ceil(n/-2)
        r = n + 2 * new_n
        n = new_n
        stack.append(str(r))

    while stack:
        result += stack.pop()

    return result


num = int(sys.stdin.readline())

sys.stdout.write(to_minus_bin(num))