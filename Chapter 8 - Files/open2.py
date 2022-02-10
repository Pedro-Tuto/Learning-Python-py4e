x = open('ASDAS.txt')
for c in x:
    print(c)

y = open('ASDAS.txt')
count = 0
for line in y:
    count = count + 1
print('Contagem de Linhas:', count)

z = open('ASDAS.txt')
inp = z.read()
print(len(inp))
print(inp[:10])