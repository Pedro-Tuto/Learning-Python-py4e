import re
hand = open('sampledata.txt')
lst = list()
x = re.findall('[0-9]+', hand)
num = float(x[0])
lst.append(num)
print(lst)

#print(lst)