name = input('Digite o nome do arquivo: ')
hand = open(name)

#primeiro criamos o dicionário, e separamos todas as palavras extraídas do arquivo umas das outras
#além disso, fazemos o loop do .get, para construir o dicionário a partir das palavras
counts = dict()
for line in hand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#em seguida, estabelecemos variáveis para um loop de for

bigcount = None
bigword = None
for word, count in counts.items() :
#aqui simplesmente temos um loop de máximo, em que os valores bigword e bigcount só serão atualizados 
#caso haja uma entrada do count maior do que a bigword anterior
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
