num = int(input())

for i in range(1, num):
    print('*'*i + ' '*(2*(num-i)) + '*'*i)
print('*'*(2*num))
for i in range(1, num):
    print('*'*(num-i) + ' '*(2*i) + '*'*(num-i))