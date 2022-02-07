print ('antes')
for x in [9, 41, 12, 3, 74, 15] :
    print(x)
print('depois')

maiorateagora = -1
print('Antes', maiorateagora)
for num in [9, 41, 12, 3, 74, 15] :
    if num > maiorateagora : 
        maiorateagora = num
    print(maiorateagora, num)

print('Depois', maiorateagora)

