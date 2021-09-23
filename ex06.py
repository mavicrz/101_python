def computepay (h,r):
    if h > 40:
        pay= (40*r) + ((h-40) * r *1.5)
    else:
        pay= h*r
    return pay
hr= input ("Enter hours:")
rt= input ("Enter rate:")
h= float(hr)
r= float (rt)
p= computepay (h,r)
print ('Pay', p)
