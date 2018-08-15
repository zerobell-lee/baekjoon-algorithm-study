import sys

def crypt(x):
    global crypt_lower
    global lower_a
    global cap_a

    vx = ord(x)

    if vx >= lower_a:
        return crypt_lower[vx - lower_a]
    elif vx >= cap_a:
        return crypt_cap[vx - cap_a]
    else:
        return x


lower_a = ord('a')
cap_a = ord('A')

crypt_lower = [chr((i+13) % 26 + ord('a')) for i in range(26)]
crypt_cap = [chr((i+13) % 26 + ord('A')) for i in range(26)]

line = list(sys.stdin.readline())
result = ''

for l in line:
    result += crypt(l)

sys.stdout.write(result)

