import sys
import math


def fact(n):
    return n * fact(n-1) if n > 1 else 1


# num = int(sys.stdin.readline())

for num in range(0, 501):

    if num < 2:
        sys.stdout.write("0\n")
        continue

    primes = [2]

    for i in range(2, num + 1):
        notPrime = False
        for j in range(2, math.ceil(math.sqrt(i))+1):
            if i % j == 0:
                notPrime = True
                break

        if not notPrime:
            primes.append(i)

    count = [0, 0]
    fact_n = fact(num)

    for i in primes:
        while True:
            if fact_n % i == 0:
                if i == 2:
                    count[0] += 1
                elif i == 5:
                    count[1] += 1
                fact_n //= i
                continue
            else:
                break

    sys.stdout.write(str(min(count)) + '\n')