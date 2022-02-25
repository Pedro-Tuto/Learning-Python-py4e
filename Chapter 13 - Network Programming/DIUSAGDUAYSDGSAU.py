import ssl
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#ignorando SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

itt = 0
while itt < 4:
    if itt == 0:
        url = input('Enter-')
        print('Retrieving:', url)
    else:
        url = lst[2]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup)

    count1 = 0
    lst = list()
    tags = soup('a')
    #print(tags)
    for tag in tags:
        if count1 < 3:
            tag = tag.get('href', None)
            lst.append(tag)
            count1 = count1 + 1
    #print(lst)
    print('Retrieving:', lst[2])

    itt = itt + 1


    
    
    





