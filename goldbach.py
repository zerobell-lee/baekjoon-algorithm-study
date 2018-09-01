import sys


eratos = [False if i % 2 == 0 else True for i in range(1000001)]

eratos[1] = False
eratos[2] = True

primes = []

for i in range(3, len(eratos), 2):
    if not eratos[i]:
        continue
    primes.append(i)
    for j in range(i*i, len(eratos), i*2):
        eratos[j] = False

while True:
    num = int(sys.stdin.readline())

    if num == 0:
        break
    else:
        a = b = 0

        for i in range(3, num//2+1, 2):
            c, d = i, num - i
            if c not in primes and d not in primes:
                continue

            if d-c >= b-a:
                a, b = c, d

        if a == b == 0:
            sys.stdout.write("Goldbach's conjecture is wrong.")
            break

        else:
            sys.stdout.write('%d = %d + %d\n'%(num, a, b))


