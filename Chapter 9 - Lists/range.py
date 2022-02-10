from bz2 import BZ2Decompressor


print(range(4))
amigos = ['Robson', 'Jellyson', 'Gabigolmes']
print(len(amigos))  
print(range(len(amigos)))

for x in amigos:
    print('Feliz ano novo:', x)
for i in range(len(amigos)):
    x = amigos[i]
    print('Feliz ano novo:', x)
 