han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
#Guardian Pattern: protege o código, neste caso contra linhas em branco (len(wds) < 1)
    if len(wds) < 3 :
        continue
    if wds[0] != 'From' :
        continue
    print(wds[2])
