x= 'X-DSPAM-Confidence:    0.8475'
a= x.find (':')
b= x[a+5:]
value= float(b)
print (value)
