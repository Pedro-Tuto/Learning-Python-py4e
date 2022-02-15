fname = input('Digite o nome do arquivo: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)
    for w in wds:
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1
        print(w,di[w])

print(di)






