month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

a, b = input().split(' ')
a = int(a)
b = int(b)
date = 0

for i in range(1, a):
    date += month[i-1]

date += b-1

print(day[date%7])