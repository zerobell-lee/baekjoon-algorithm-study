import sys


def search(arr, begin, end, num):
    mid = (begin + end)//2
    new_begin = begin
    new_mid = mid
    new_end = end

    while begin <= new_begin <= new_end:
        if arr[new_mid] == num:
            if new_mid < end and arr[new_mid + 1] > num:
                return new_mid + 1
            else:
                new_begin = new_mid + 1
                new_mid = (new_begin + new_end) // 2
        elif arr[new_mid] < num:
            new_begin = new_mid + 1
            new_mid = (new_begin + new_end) // 2
        else:
            if new_mid > begin and arr[new_mid - 1] < num:
                return new_mid
            else:
                new_end = new_mid - 1
                new_mid = (new_begin + new_end) // 2

    return begin



arr = []

n = int(sys.stdin.readline())

for i in range(n):
    arr.append(int(sys.stdin.readline()))

last_border = 0
last_val = arr[0]
cnt = 0

for i in range(n):
    if last_val > arr[i]:
        cnt += i - search(arr, last_border, i-1, arr[i])
        last_border = i
    last_val = arr[i]

sys.stdout.write(str(cnt+1))