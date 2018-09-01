import sys


class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

    def __lt__(self, other):
        if self.korean == other.korean:
            if self.english == other.english:
                if self.math == other.math:
                    return self.name < other.name
                else:
                    return self.math > other.math
            else:
                return self.english < other.english
        else:
            return self.korean > other.korean

    def __gt__(self, other):
        if self.korean == other.korean:
            if self.english == other.english:
                if self.math == other.math:
                    return self.name > other.name
                else:
                    return self.math < other.math
            else:
                return self.english > other.english
        else:
            return self.korean < other. korean

    def __str__(self):
        return self.name


num = int(sys.stdin.readline())
student_arr = []

for i in range(num):
    name, korean, english, math = sys.stdin.readline().rstrip().split()
    student_arr.append(Student(name, int(korean), int(english), int(math)))

student_arr.sort()

for i in student_arr:
    sys.stdout.write(str(i) + '\n')