import re
x = 'Meus 2 números favoritos são 19 e 42'
y = re.findall('[0-9]+', x)
print(y)

#o [0 - 9] + significa um ou mais dígitos naquele intervalo
#o findall gera uma lista

a = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
b = re.findall('\S+@\S+', a)
print(b)
#parentesis separam apenas o que queremos extrair:
c = re.findall('^From (\S+@\S+)', a)
print(c)

#aqui fazemos um desdobramento mais complexo, para retirar apenas a parte que vem depois do @
z = re.findall('^From .*@([^ ]*)',a)
print(z)
