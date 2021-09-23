name= input ('Enter file:')
lt= list()
#Abrir o arquivo
fhandle= open(name)
#Cria a lista com linhas separadas
file= fhandle.readlines()
#Para cada linha tira o espaço, e divide
for line in file:
    line= line.rstrip()
    words= line.split()
#Cada palavra da lista inserir na listona
    for word in words:
        if word in lt: continue
        lt.append (word)
lt.sort()
print (lt)
