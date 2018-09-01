import sys


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        else:
            return self.y < other.y

    def __gt__(self, other):
        if self.x != other.x:
            return self.x > other.x
        else:
            return self.y > other.y

    def __le__(self, other):
        if self.x != other.x:
            return self.x <= other.x
        else:
            return self.y <- other.y

    def __ge__(self, other):
        if self.x != other.x:
            return self.x >= other.x
        else:
            return self.y >= other.y


num = int(sys.stdin.readline())
point_arr = []

for i in range(num):
    x, y = map(int, list(sys.stdin.readline().rstrip().split()))
    point_arr.append(Point(x, y))

point_arr.sort()

for i in point_arr:
    sys.stdout.write('%d %d\n'%(i.x, i.y))