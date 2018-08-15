import sys


stair = []
num = int(sys.stdin.readline())

for i in range(num):
    stair.append(int(sys.stdin.readline()))

D = [[0, 0] for i in range(num)]

if num < 3:
    sys.stdout.write(str(stair[0] + stair[1]))
    exit()

D[0] = [stair[0], 0]
D[1] = [stair[0] + stair[1], stair[1]]

for i in range(2, num):
    D[i][0] = D[i-1][1] + stair[i]
    D[i][1] = max(D[i-2]) + stair[i]

sys.stdout.write(str(max(D[num-1])))
