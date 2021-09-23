import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count= input ('Enter count:')
position= input ('Enter position:')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

p= int(position)
c= 0
count=int(count)

tags = soup('a')

while True:
    if c == count: break
    else:
        for tag in tags:
            if tags [p]:
                name= tags[p].get('href', [0])
                print ('Retrieving:', name)
                c= c+1
                html = urllib.request.urlopen(name, context=ctx).read()
                soup = BeautifulSoup(html, 'html.parser')
            else: continue
