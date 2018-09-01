import sys


num = int(sys.stdin.readline())
point_arr = []

key_x = lambda a: a[0]
key_y = lambda a: a[1]


for i in range(num):
    point_arr.append(list(map(int, list(sys.stdin.readline().rstrip().split()))))

point_arr.sort(key=key_x)
point_arr.sort(key=key_y)

for i in point_arr:
    sys.stdout.write('%d %d\n'%(i[0], i[1]))
