import sys


a, b, c = map(int, sys.stdin.readline().rstrip().split())

result = '%d\n%d\n%d\n%d'%((a+b)%c, (a%c + b%c)%c, (a*b)%c, (a%c * b%c)%c)

sys.stdout.write(result)