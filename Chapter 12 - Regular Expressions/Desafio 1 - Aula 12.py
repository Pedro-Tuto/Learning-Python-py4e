import re
hand = open('actualdata.txt')
lst = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    #print(x)
    if len(x) < 1:
        continue
    for num in x:
        num = float(num)
        lst.append(num)

print(sum(lst))
