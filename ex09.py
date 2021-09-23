fname= input ('Enter file:')
fhandle= open (fname)
for line in fhandle:
    line= line.rstrip()
    print (line.upper())
