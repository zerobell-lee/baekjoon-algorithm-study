import sys

alpha = [-1] * 26
line = list(sys.stdin.readline().strip())
conv = lambda x : ord(x) - ord('a')

for (i, x) in enumerate(line):
    if alpha[conv(x)] == -1:
        alpha[conv(x)] = i

sys.stdout.write(' '.join(map(str, alpha)))