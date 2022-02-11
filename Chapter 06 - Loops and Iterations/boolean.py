found = False
print('Antes', found)
for valor in [9, 41, 12, 3, 74, 15] :
    if valor == 3 :
        found = True
    else: 
        found = False
    print(found, valor)
print('Depois', found)

#tentando achar o menor valor, método 1 (não vai funcionar sempre):
menor = 100
print('Antes', menor)
for num in [9, 41, 12, 3, 74, 15] :
    if num < menor :
        menor = num
    print(menor, num)
print('Depois', menor)

#tentando achar o menor valor, método 2:
menor = None
print('Before')
for valor in [9, 41, 12, 3, 74, 15] :
    if menor is None :
        menor = valor
    elif valor < menor :
        menor = valor
    print(menor, valor)
print('Depois', menor)

