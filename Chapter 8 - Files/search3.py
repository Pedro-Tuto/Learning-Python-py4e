name = input('Digite o nome do arquivo: ')
x = open(name)
count = 0
for line in x:
    if line.startswith('A'):
        count = count + 1
print('Existem', count, 'frases começando com a letra A em', name)