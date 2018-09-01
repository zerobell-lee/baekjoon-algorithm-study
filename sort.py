import sys


def quickSort(a, start, end):

    if start < end:
        left = start
        pivot = a[end]
        for i in range(start, end):
            if a[i] < pivot:
                a[i], a[left] = a[left], a[i]
                left += 1
        a[left], a[end] = a[end], a[left]
        quickSort(a, start, left-1)
        quickSort(a, left+1, end)


def merge_sort(arr):

    if len(arr) <= 1:
        return
    mid = len(arr)//2
    la, ra = arr[:mid], arr[mid:]

    merge_sort(la)
    merge_sort(ra)

    i, li, ri = 0, 0, 0
    while li < len(la) and ri < len(ra):
        if la[li] < ra[ri]:
            arr[i] = la[li]
            li += 1
        else:
            arr[i] = ra[ri]
            ri += 1
        i += 1
    arr[i:] = la[li:] if li != len(la) else ra[ri:]


num = int(sys.stdin.readline())
arr = []

for i in range(num):
    arr.append(int(sys.stdin.readline()))

quickSort(arr, 0, num-1)

for i in arr:
    sys.stdout.write('%d\n'%i)