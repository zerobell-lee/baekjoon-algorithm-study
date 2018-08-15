line = input()

while len(line)>0:
    if (len(line)>=10):
        print(line)
        line = line[10:]
    else:
        print(line)