fname = input('Digite o nome do arquivo: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
hand = open(fname)

#este é o loop que vimos anteriormente para montar o dicionário a parir do arquivo:
di = dict()
for line in hand:
    line = line.rstrip()
    print('\n LINHA:', line)
    wds = line.split()
    print('\n PALAVRA:', wds)
    for w in wds:
        di[w] = di.get(w,0) + 1

#este é um loop para achar os key/values que mais aparecem:
maior = -1
palavra = None
print('\n DICIONARIO: ITENS', di.items())
for x,y in di.items():
    #print(f'\n {x} E {y}:')
    if y > maior:
        maior = y
        palavra = x #"capturamos" a palavra que mais apareceu
print(palavra, maior)










