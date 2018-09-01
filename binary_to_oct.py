import sys

binary = int(sys.stdin.readline().rstrip(), 2)

sys.stdout.write(oct(binary)[2:])