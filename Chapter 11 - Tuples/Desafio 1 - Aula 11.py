'''Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

ls = list()
di = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        w = line.split()
        hora = w[5]
        atpos = hora[0:2]
        #print(atpos)
        ls.append(atpos)

#print(ls)

for hr in ls:
    di[hr] = di.get(hr,0) +1

#print(di)

ls2 = list()
for k, v in di.items():
    newt = (k, v)
    ls2.append(newt)

#print(ls2)

ls2 = sorted(ls2)
for k, v in ls2:
    print(k,v)