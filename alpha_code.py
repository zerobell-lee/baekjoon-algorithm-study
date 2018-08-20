import sys


line = sys.stdin.readline().strip()

D = [[0, 0] for i in range(len(line) + 1)]

D[1] = [1, 0]

if line == '0':
    sys.stdout.write('0')
    exit()

for i in range(2, len(line)+1):
    if line[i-1] == '0':
        D[i][0] = 0
    else:
        D[i][0] = sum(D[i-1])
    if (line[i-2] >= '3') or (line[i-2] == '2' and line[i-1] > '6') or (line[i-2] == '0'):
        D[i][1] = 0
    else:
        D[i][1] = D[i-1][0]

sys.stdout.write(str(sum(D[len(line)]) % 1000000))