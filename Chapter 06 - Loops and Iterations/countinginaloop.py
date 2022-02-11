print('Contando:')
zork = 0
print('Antes', zork)
for x in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, x)
print('Depois', zork)

print('Total:')
zork = 0
print('Antes', zork)
for x in [9, 41, 12, 3, 74, 15] :
    zork = zork + x
    print(zork, x)
print('Depois', zork)

print('Média:')
count = 0
sum = 0
print('Antes', count, sum)
for y in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + y
    print(count, sum, y)
print('Depois: Contagem:', count,'Soma:', sum, 'Média:', sum/count)
