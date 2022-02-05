#o break "pula" pra fora do bloco que está o loop
#o continue "volta" para o começo do bloco do loop
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'pronto':
        break
    print(line)
print('Pronto!')

input()
