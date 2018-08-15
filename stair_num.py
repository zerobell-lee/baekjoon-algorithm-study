import sys


def fibo(n):
    def fibo_help(a, b, n):
        return fibo_help(b, a+b, n-1) if n > 0 else a
    return fibo_help(0, 1, n)

num = int(sys.stdin.readline())

arr = [1] * 10
arr[0] = 0


for i in range(1, num):
    new_arr = [0]*10
    for (j, e) in enumerate(arr):
        if j == 0:
            new_arr[1] += e
        elif j == 9:
            new_arr[8] += e
        else:
            new_arr[j-1] += e
            new_arr[j+1] += e

    arr = new_arr


sys.stdout.write(str(sum(arr)%1000000000))