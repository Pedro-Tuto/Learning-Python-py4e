d = {'a':10, 'b': 1, 'c':22}
#convertemos o dicionário em uma lista:
print(d.items())
print(sorted(d.items()))
#convertemos a lista em tuples:
for k, v in sorted(d.items()):
    print(k,v)

c = {'a':10, 'b': 1, 'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)







