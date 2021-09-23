fhandle= open ('mbox-short.txt')
file= fhandle.readlines()
count= 0
#Outro jeito de fazer seria if len (line) < 3 or line [0] =! 'From': continue
for line in file:
    if line.startswith ('From:'):
        continue
    elif line.startswith ('From'):
# Aqui ficaria igual
        words= line.split ()
        print (words[1])
        count= count + 1
    else:
        continue
print ('There were', count, 'lines in the file with From as the first word')
