total = 0
count = 0
while True:
    inp = input('Digite um número: ')
    if inp == 'done' : 
        break
    try:
        value = float(inp)
        total = total + value
        count = count + 1       
    except:
        print('Entrada inválida')

avg = total/count
print('Média: ', avg)