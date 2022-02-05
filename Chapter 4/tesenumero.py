a = input('Digite um número:')
try:
    b = int(a)
except:
    b = -1

if b >= 0 :
    print(f'Parabéns, {b} é um número! É GABIGOLMES!')
else:
    print(f'{a} não é um número')

import os
os.system('pause')
