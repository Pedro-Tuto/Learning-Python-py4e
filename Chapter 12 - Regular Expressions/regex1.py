#aqui usamos o re.search como o find

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line) 

#aqui usamos o re.search como o .startswith

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

#aqui usamos o ^ para selecionar as linhas que COMEÇAM com X
#usamos o . para  indicar que queremos qualquer caracter após o inicial
#usamos o * para dizer que queremos qualquer número de caracteres
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X.*', line):
        print(line)

#aqui usamos o \S para tirar os caracteres que são espaços
#usamos o + para dizer uma ou mais vezes o \S

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X-\S+:', line):
        print(line)



