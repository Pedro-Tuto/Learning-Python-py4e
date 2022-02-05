def greet(lang):
    if lang == 'es':
        print('¡Hola Gagigolmes!')
    elif lang == 'fr':
        print('Bonjour Monsieur Gabigolmes.')
    elif lang == 'ru':
        print('Привет Gabigolmes.')
    elif lang == 'ja':
        print('こんにちは Gabigolmes-san.')
    else:
        print('Olá Gabigolmes')

a = input('Deseja ser recebido em qual língua?')
if a == 'espanhol':
    greet('es')
elif a == 'francês':
    greet('fr')
elif a == 'russo':
    greet('ru')
elif a == 'japonês':
    greet('ja')
else:
    print(a,'não é uma língua válida. Tente: espanhol, francês, russo ou japonês')

import os
os.system('pause')
