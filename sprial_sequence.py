import sys


P = [0 for i in range(101)]

P[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, 101):
    P[i] = P[i-1] + P[i-5]


num = int(sys.stdin.readline())

for i in range(num):
    sys.stdout.write(str(P[int(sys.stdin.readline())]) + '\n')