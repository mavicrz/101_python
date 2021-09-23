xhr= input('Enter hours:')
xrt= input('Enter rate:')
try:
    hr= float(xhr)
    rt= float (xrt)
except:
    print('Error')
    quit()
if hr > 40:
    pay= (40*rt) + ((hr-40) * rt *1.5)
else:
    pay= hr*rt
print (pay)
