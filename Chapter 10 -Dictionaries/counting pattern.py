counts = dict()
print('Digite uma linha de texto: ')
line = input('')

words = line.split()
print('Palavras:', words)

print('Contando...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('A quantidade de cada palavra é:', counts)