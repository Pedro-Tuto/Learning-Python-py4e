print('BEM VINDE. DIGITE NÚMEROS PARA SABER A MÉDIA ARITMÉTICA ENTRE ELES.')
print('QUANDO ESTIVER SATISFEITE COM OS NÚMEROS, DIGITE "done":')
numlist = list()
while True:
    inp = input('Digite um número: ')
    if inp == 'done':
        break
    try:
        x = float(inp)
    except:
        print('Entrada inválida. Por favor digite um NÚMERO.')
        continue
    x = float(inp)
    numlist.append(x)

avg = sum(numlist)/len(numlist)
print('Média Aritmética:', avg)
print('Pressione ENTER para sair.')
input()