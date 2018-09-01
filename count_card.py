import sys


num = int(sys.stdin.readline())

card_arr = []

for i in range(num):
    card_arr.append(int(sys.stdin.readline()))

card_arr.sort()
