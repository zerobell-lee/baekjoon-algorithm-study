import sys

a, b, c, d = sys.stdin.readline().rstrip().split()

ab = int(a+b)
cd = int(c+d)

print(ab+cd)