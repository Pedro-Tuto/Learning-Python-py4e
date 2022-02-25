'''Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. 
One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1475029.html (Sum ends with 41)
You do not need to save these files to your folder since your program will read the data directly from the URL.
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
Look at the sample code provided. 
It shows how to find all of a certain kind of tag, loop through the tags and extract the various aspects of the tags.
You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to integers and add them up to complete the assignment.
'''

import ssl
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#ignorando SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#usando urllib + BeautifulSoup para abrir e ler o link em html
url = input('Enter- ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#criando uma lista para somar depois
lst = list()
#Pegando todas as Span Tags <span>
tags = soup('span')
for tag in tags:
    print(tag)
    #print ('TAG:',tag)
    #print ('URL:',tag.get('href', None))
    #print ('Contents:',tag.contents[0])
    #print ('Attrs:',tag.attrs)    
    num = tag.contents[0]
    num = int(num)
    lst.append(num)

soma = sum(lst)
print('Count', soma)


