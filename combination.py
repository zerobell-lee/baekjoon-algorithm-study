import sys


primes = [2, 5]


def sub_arr(arr1, arr2):
    x = arr1[0] - arr2[0]
    x = x if x > 0 else 0

    y = arr1[1] - arr2[1]
    y = y if y > 0 else 0

    return [x, y]


def sum_arr(arr1, arr2):
    return [arr1[0] + arr2[0], arr1[1] + arr2[1]]


def count_prime(n):
    result = [0, 0]
    for (i, e) in enumerate(primes):
        j = e
        while True:
            if j > n:
                break

            result[i] += n // j
            j *= e

    return result


n, m = map(int, list(sys.stdin.readline().rstrip().split()))

value = min(sub_arr(count_prime(n), sum_arr(count_prime(m), count_prime(n-m))))

sys.stdout.write(str(value))