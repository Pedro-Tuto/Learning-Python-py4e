x = open('ASDAS.txt')
for line in x:
    line = line.rstrip()
    if line.startswith('28EY'):
        print(line)

y = open('ASDAS.txt')
for line in y:
    line = line.rstrip()
    if not line.startswith('28EY'):
        continue
    print(line)

#ambos os códigos fazem a mesma coisa, o primeiro apenas define o que estamos procurando
#o segundo exclui o que estamos procurando e pula para o começo com continue