import sys


alpha = [0] * 26
line = list(sys.stdin.readline().strip())

for x in line:
    alpha[ord(x) - ord('a')] += 1

print(' '.join(map(str, alpha)))