import sys


num = int(sys.stdin.readline())
tai = [0] * (num+1)
sale = [None] * (num+1)

for i in range(num+1):
    sale[i] = [0]*(num+1)

line = list(sys.stdin.readline().strip().split())

for i in range(1, num + 1):
    tai[i] = int(line[i-1])

sale[1][1] = tai[1]

for i in range(1, num + 1):
    for j in range(1, num+1):
        arr = []

        if j >= i:
            arr.append(sale[i][j-i] + tai[i])

        arr.append(sale[i-1][j])
        arr.append(sale[i][j-1])
        sale[i][j] = max(arr)

sys.stdout.write(str(sale[num][num]))