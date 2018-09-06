import sys


num = int(sys.stdin.readline())

card_arr = []

for i in range(num):
    card_arr.append(int(sys.stdin.readline()))

card_arr.sort()

border = 0
most = [card_arr[0], 1]
last = 0

for (i, e) in enumerate(card_arr):
    if card_arr[last] != e:
        cur_val = i - border
        if cur_val > most[1]:
            most = [card_arr[last], cur_val]
        border = i
    last = i

cur_val = len(card_arr) - border
if cur_val > most[1]:
    most = [card_arr[-1], cur_val]

sys.stdout.write(str(most[0]))
