import sys


line = sys.stdin.readline().strip()
postfix = []

for i in range(len(line)):
    postfix.append(line[i:])

postfix.sort()

for e in postfix:
    print(e)