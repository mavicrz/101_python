name= input ('Enter file:')
fhandle= open (name)
lt= list()
import re
f= re.findall('[0-9]+', fhandle.read())
for number in f:
    value= int(number)
    lt.append(value)
print(sum(lt))
