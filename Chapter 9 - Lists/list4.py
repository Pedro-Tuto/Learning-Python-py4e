line = "AQUI      TEM                   MUITOS          ESPAÇOS"
etc = line.split()
print(etc)
etc.sort()
print(etc)

line = 'primeiro;segundo;terceiro;quarto'
x = line.split(';')
print(x)
print(len(x))

#novamente usando como exemplo o documento 'mbox-short.txt'. Nesse caso, queremos extrair apenas os dias da semana de e-mails recebidos.
#exemplo: splitando : 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008' retiraremos os espaços com .split() e transformaremos numa lista de strings.

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])

#aqui temos um exemplo de split() duas vezes

line = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
print(email)
piece = email.split('@')
print(piece[1])