import sys


def fibo(n):
    def fibo_help(a, b, n):
        return fibo_help(b, a+b, n-1) if n>0 else a
    return fibo_help(0, 1, n)


num = int(sys.stdin.readline())


sys.stdout.write(str(fibo(num+1)%10007))