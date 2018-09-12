import sys

def search(a, begin, end, num):
    new_begin = begin
    new_end = end

    while begin <= new_begin <= new_end <= end:
        mid = (new_begin + new_end) // 2
        if a[mid] == num:
            if mid == end:
                return end
            else:
                if a[mid+1] > num:
                    return mid
                else:
                    new_begin = mid+1
        elif a[mid] < num:
            new_begin = mid+1
        else:
            new_end = mid-1


arr = []


n = int(sys.stdin.readline())

for i in range(n):
    arr.append(int(sys.stdin.readline()))

sorted_arr = [x for x in sorted(arr)]
val = 0

for i in range(n):
    tmp = i - search(sorted_arr, 0, n-1, arr[i])
    val = max(val, tmp)

sys.stdout.write(str(val+1))