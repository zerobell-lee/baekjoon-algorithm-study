import sys


convert_arr = [str(i) for i in range(10)]
convert_arr.extend([chr(i + ord('A')) for i in range(26)])

n, b = map(int, sys.stdin.readline().rstrip().split())

stack = []

while n > 0:
    stack.append(convert_arr[n % b])
    n = n // b

result = ''

while stack:
    result += stack.pop()

sys.stdout.write(result)