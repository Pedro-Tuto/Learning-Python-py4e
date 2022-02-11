#simplificando a contagem com get
#com este médoto, criamos novas entries em dicionários, e updatamos as existentes

counts = dict()
nomes = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for nome in nomes:
    counts[nome] = counts.get(nome, 0) + 1
print(counts)