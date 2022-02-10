fhand = open('ASDAS.txt')
for line in fhand:
    line = line.rstrip()
    if not '28EY' in line:
        continue
    print(line)
