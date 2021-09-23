#Abrir arquivo
fhandle= open ('mbox-short.txt')
#Lê cada linha e faz uma lista de linhas
file= fhandle.readlines()
counts= dict()
maxi= None
#Pra cada item da lista
for line in file:
    if line.startswith ('From:'):
        continue
    elif line.startswith ('From'):
#Faz uma lista das palavras na linha
        words= line.split()
    else: continue
#Fazer dicionário de emails e contar quantos de cada tem
    for mail in words:
#Separa só email da lista
        if mail != words [1]: continue
        else:
#Conta os email
            counts [mail] = counts.get (mail, 0) +1
#Qual email tem mais
    for mail, count  in counts.items():
        if maxi is None or count > maxi:
            maxi= count
            maximail= mail
    else: continue
print (maximail,maxi)
