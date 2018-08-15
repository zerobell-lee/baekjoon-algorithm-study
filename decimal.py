import sys


arr = [0] * 11

arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in range(4, 11):
    arr[i] = arr[i-3] + arr[i-2] + arr[i-1]

num = int(sys.stdin.readline())


for i in range(num):
    line = int(sys.stdin.readline())
    sys.stdout.write(str(arr[line]) + '\n')