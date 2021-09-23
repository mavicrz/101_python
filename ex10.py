fname= input('Enter file:')
fhandle= open(fnamse)
count=0
t= 0
for line in fhandle:
#achar o que queremos
    if not line.startswith ('X-DSPAM-Confidence:'): continue
#contamos
    count= count + 1
#achar o valor
    n= line.find (':')
    m= line [n+1:]
    value= float(m)
#somar todos os valores
    if t == 0:
        t= value
    else:
        t= t + value

a= t/count
print ('Average spam confidence:', a)
