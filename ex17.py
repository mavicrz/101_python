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

t=0
count=0

# Retrieve all of the spam tags
tags = soup('span')
for tag in tags:
#contamos
    count= count + 1
#Achar o valor
    m= tag.get('class="comments">', None)
    value= int(m)
#somar todos os valores
    if t == 0:
        t= value
    else:
        t= t + value

print('Count', count)
print('Sum', t)
