import sys


n, k = map(int, sys.stdin.readline().rstrip().split())

input_arr = sys.stdin.readline().rstrip().split()

for i in range(len(input_arr)):
    input_arr[i] = int(input_arr[i])

arr = input_arr[:k]
arr.sort()

for i in range(k, n):
    if input_arr[i] < arr[-1]:
        arr[-1] = input_arr[i]
        arr.sort()

sys.stdout.write(str(arr[-1]))