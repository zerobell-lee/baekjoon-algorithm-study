import sys


oct_num = int(sys.stdin.readline(), 8)

sys.stdout.write(bin(oct_num)[2:])