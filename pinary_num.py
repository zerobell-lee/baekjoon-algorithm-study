import sys


num = int(sys.stdin.readline())

arr = [[0, 0]] * (num+1)

arr[1] = [0, 1]

if num > 1:
    for i in range(2, num+1):
        z = arr[i - 1][0]
        x, y = arr[i-1]

        arr[i][0] = x + y
        arr[i][1] = z

        # arr[i][0] = sum(arr[i-1])
        # arr[i][1] = arr[i-1][0] 을 하면 잘못된 값이 나왔다. 왜지?

sys.stdout.write(str(sum(arr[num])))