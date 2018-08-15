import sys
from collections import deque

class Deque():

    def __init__(self, size):
        self.maxSize = size
        self.size = 0
        self.arr = [None] * size
        self.front = -1
        self.rear = -1

    def empty(self):
        return 1 if self.size == 0 else 0

    def isFull(self):
        return 1 if self.size == self.maxSize else 0

    def push_front(self, d):
        if self.isFull() == 0:
            if self.empty() == 1:
                self.front += 1
                self.rear += 1
            else:
                self.front = (self.front + self.maxSize - 1) % self.maxSize
            self.arr[self.front] = d
            self.size += 1

    def push_back(self, d):
        if self.isFull() == 0:
            if self.empty() == 1:
                self.front += 1
                self.rear += 1
            else:
                self.rear = (self.rear + 1) % self.maxSize
            self.arr[self.rear] = d
            self.size += 1

    def pop_front(self):
        if self.empty() == 0:
            d = self.arr[self.front]
            self.front = (self.front + 1) % self.maxSize
            self.size -= 1
        else:
            d = -1
        return d

    def pop_back(self):
        if self.empty() == 0:
            d = self.arr[self.rear]
            self.rear = (self.rear + self.maxSize - 1) % self.maxSize
            self.size = -1
        else:
            d = -1
        return d

    def get_size(self):
        return self.size

    def get_front(self):
        return -1 if self.empty() == 1 else self.arr[self.front]

    def get_back(self):
        return -1 if self.empty() == 1 else self.arr[self.rear]


num = int(sys.stdin.readline().strip())
deque = deque()

for i in range(num):
    line = sys.stdin.readline().strip().split()

    if line[0]=='pop_front':
        if len(deque) == 0:
            print('-1')
        else:
            print(str(deque.popleft()))
    elif line[0]=='pop_back':
        if len(deque) == 0:
            print('-1')
        else:
            print(str(deque.pop()))
    elif line[0]=='push_front':
        deque.appendleft(line[1])
    elif line[0]=='push_back':
        deque.append(line[1])
    elif line[0]=='empty':
        print('1' if len(deque)==0 else '0')
    elif line[0]=='front':
        if len(deque) == 0:
            print('-1')
        else:
            print(str(deque[0]))
    elif line[0]=='back':
        if len(deque) == 0:
            print('-1')
        else:
            print(str(deque[len(deque)-1]))
    elif line[0]=='size':
        print(str(len(deque)))

