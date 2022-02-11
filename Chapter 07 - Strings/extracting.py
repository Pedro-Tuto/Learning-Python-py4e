data = 'from gabigolmes.silverIV@serrabra.com Sat Jan 09:14:16 2008'
atpos = data.find('@')
print(atpos)
#no caso abaixo, o find procura o próximo ' ' a partir do atpos:
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)
