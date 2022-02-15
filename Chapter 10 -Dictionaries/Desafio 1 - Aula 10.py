'''Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer'''


'''Este desafio deu trabalho, pois eu não estava conseguindo encontrar as 5 entradas do email desejado.
Sempre estava encontrando 10 entradas. O segredo está no enunciado.
O professor pede apenas as entradas iniciadas por 'From ', e excluindo as entradas com 'From:'.
Smilares, porém diferentes...'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

ls = []
di = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        wds = line.split()
        email = wds[1]
        ls.append(email)

for em in ls:
    di[em] = di.get(em,0) + 1

#print(di)

palavra = None
maior = -1
for k, v in di.items():
    if v > maior:
        maior = v
        palavra = k
print(palavra, maior)
