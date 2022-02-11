while True:
    name = input('Digite o nome do arquivo: ')
    try:
        x = open(name)
    except:
        print('Este arquivo não pode ser aberto:', name)
        quit()

    count = 0
    y = 'A'
    for line in x:
        if line.startswith(y):
            count = count + 1
    print('Há', count, 'frases começadas em', y, 'no arquivo', name)



