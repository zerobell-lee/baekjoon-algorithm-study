# Q: 2667


import sys


doingValue = -1
firstDone = -2
index = 1


def check(x, y):
    global doingValue
    global firstDone
    global matrix
    global size
    global index
    global tagged

    matrix[x][y] = firstDone
    doinglist = [(x, y)]

    def getNear(x, y):
        global matrix

        result = []
        if x < size-1:
            if matrix[x+1][y] > 0:
                result.append((x+1, y))
        if x > 0:
            if matrix[x-1][y] > 0:
                result.append((x-1, y))
        if y < size-1:
            if matrix[x][y+1] > 0:
                result.append((x, y+1))
        if y > 0:
            if matrix[x][y-1] > 0:
                result.append((x, y-1))

        return result

    z = getNear(x, y)
    checkArea = z
    doinglist.extend(z)

    while True:

        if len(checkArea) == 0:
            break

        tmp = []
        for e in checkArea:
            matrix[e[0]][e[1]] = firstDone
            z = getNear(e[0], e[1])
            for e2 in z:
                if e2 not in doinglist:
                    doinglist.append(e2)
                    tmp.append(e2)

        checkArea = tmp

    tagged.append(len(doinglist))
    index += 1







size = int(sys.stdin.readline())
matrix = [[0 for i in range(size)] for j in range(size)]
tagged = []


for i in range(size):
    matrix[i] = list(map(int, list(sys.stdin.readline().rstrip())))

for i in range(size):
    for j in range(size):
        if matrix[i][j] == 1:
            check(i, j)

sys.stdout.write('%d\n' % len(tagged))
for e in sorted(tagged):
    sys.stdout.write('%d\n' % e)