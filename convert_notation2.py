import sys


def to_num(str):
    if '0' <= str <= '9':
        return ord(str) - ord('0')
    else:
        return ord(str) - ord('A') + 10


n, b = sys.stdin.readline().rstrip().split()
b = int(b)

value = 0

for e in list(n):
    value = value * b + to_num(e)

sys.stdout.write(str(value))