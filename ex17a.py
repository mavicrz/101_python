from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count=0
t=0
# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    tag= tag.contents[0]
    count= count + 1
    value= int(tag)
#somar todos os valores
    if t == 0:
        t= value
    else:
        t= t + value
print('Count', count)
print('Sum', t)
