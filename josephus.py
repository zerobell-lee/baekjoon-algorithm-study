import sys


class Queue():

    def __init__(self, size):
        self.maxSize = size
        self.size = 0
        self.arr = [None]*size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if not self.isFull():
            self.rear = (self.rear+1) % self.maxSize
            self.arr[self.rear] = data
            self.size += 1

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.maxSize
            self.size -= 1
            return self.arr[self.front]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.maxSize

    def __bool__(self):
        return self.isEmpty()



a, b = map(int, sys.stdin.readline().strip().split())

people = Queue(a)

for i in range(1, a+1):
    people.enqueue(str(i))

result = '<'

while not people.isEmpty():
    for i in range(b-1):
            people.enqueue(people.dequeue())
    result += str(people.dequeue())
    if not people.isEmpty():
        result += ', '
    else:
        result += '>'


sys.stdout.write(result)