import sys


num = int(sys.stdin.readline())

arr = [None] * (num + 1)

arr[1] = [1] * 10

if num > 1:
    for i in range(2, num+1):
        arr[i] = [0] * 10

    for i in range(2, num+1):
        for (j, e) in enumerate(arr[i-1]):
            for k in range(j, 10):
                arr[i][k] += e

sys.stdout.write(str(sum(arr[num])%10007))