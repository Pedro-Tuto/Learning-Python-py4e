asdas = input('Digite o nome do arquivo: ')
fhand = open(asdas)
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#print(counts)
        
lst = list()
for k, v in counts.items():
    tup = (v, k)
    lst.append(tup)

#print(lst)

lst = sorted(lst, reverse=True)
for v, k in lst[:10] :
    print(k, v)





