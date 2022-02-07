fruta = 'banana'
x = len(fruta)
print(x)

fruta = 'banana'
index = 0
while index < len (fruta):
    letter = fruta[index]
    print(index, letter)
    index = index + 1

fruta = 'TropicalBanana'
for letra in fruta:
    print(letra)

word = 'GABIGOLMES'
count = 0
for letra in word:
    if letra == 'G':
        count = count + 1
print('O total de letras', word[0], 'em:', word, 'é:', count)



