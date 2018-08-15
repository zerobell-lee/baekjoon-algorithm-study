num = int(input())

for i in range(num):
    print(' '*i+'*'*(2*(num-i)-1))
for i in range(2, num+1):
    print(' '*(num-i)+'*'*(2*i-1))