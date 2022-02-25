import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(x) != 1:
        continue
    num = float(x[0])
    numlist.append(num)

print('Máxmimo:', max (numlist))
