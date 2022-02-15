fname = input('Digite o nome do arquivo: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
hand = open(fname)

#este é o loop que vimos anteriormente para montar o dicionário a parir do arquivo:
di = dict()
for line in hand:
    line = line.rstrip()
    #print('\n LINHA:', line)
    wds = line.split()
    #print('\n PALAVRA:', wds)
    for w in wds:
        di[w] = di.get(w,0) + 1

print(di)

t = list()
for k,v in di.items():
    tup = (v, k)
    t.append(tup)

t = sorted(t, reverse=True)
for v, k in t[:5]:
    print (k, v)









