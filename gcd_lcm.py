import sys


a, b = map(int, sys.stdin.readline().rstrip().split())

if b > a:
    c, d = b, a
else:
    c, d = a, b

while d != 0:
    c, d = d, c % d


sys.stdout.write(str(c) + '\n' + str((a*b)//c))