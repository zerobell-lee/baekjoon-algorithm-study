import sys


def check_ord(x):
    global huddle
    for (i, cmp) in enumerate(huddle):
        if x >= cmp:
            return i
    return 3


result = ''
huddle = [ord('a'), ord('A'), ord('0')]

for l in sys.stdin:

    character = [0] * 4
    for e in list(l):
        if e == '\n':
            break
        character[check_ord(ord(e))] += 1
    character = list(map(str, character))
    sys.stdout.write(character[0] + ' ' + character[1] + ' ' + character[2] + ' ' + character[3] + '\n')
