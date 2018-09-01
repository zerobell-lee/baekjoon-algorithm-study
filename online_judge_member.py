import sys


class Member():
    order = -1

    def __init__(self, name, age):
        Member.order += 1
        self.order = Member.order
        self.name = name
        self.age = age

    def __lt__(self, other):
        if self.age != other.age:
            return self.age < other.age
        else:
            return self.order < other.order

    def __gt__(self, other):
        if self.age != other.age:
            return self.age > other.age
        else:
            return self.order > other.order

    def __str__(self):
        return '%d %s' % (self.age, self.name)

    def __repr__(self):
        return '%d %s' % (self.age, self.name)


num = int(sys.stdin.readline())
member_arr = []

for i in range(num):
    age, name = sys.stdin.readline().rstrip().split()
    member_arr.append(Member(name, int(age)))

member_arr.sort()

for i in member_arr:
    sys.stdout.write(str(i) + '\n')