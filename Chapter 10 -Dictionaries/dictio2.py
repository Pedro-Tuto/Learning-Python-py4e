ccc = dict()
ccc ['csev'] = 1
ccc ['cwen'] = 1
print(ccc)

#aqui temos uma aplicação de contagem para dict()

counts = dict()
nomes = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for nome in nomes:
    if nome not in counts:
        counts[nome] = 1
    else:
        counts[nome] = counts [nome] + 1    
print(counts)



if nome in counts:
    x = counts[nome]
else:
    x = 0
print(x)

#aqui temos a aplicação do 'get', que junta todas as linhas de contagem em uma só

y = counts.get(nome, 0)
print(y)