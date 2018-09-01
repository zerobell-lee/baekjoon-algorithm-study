import sys


num = int(sys.stdin.readline())
sys.stdout.write(str(num//5 + num//25 + num//125) + '\n')