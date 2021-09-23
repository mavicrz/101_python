#Abrir arquivo
fhandle= open ('mbox-short.txt')
#Lê cada linha e faz uma lista de linhas
file= fhandle.readlines()
counts= dict()
lt=list()
#Pra cada item da lista
for line in file:
    if line.startswith ('From:') or not line.startswith ('From'): continue
    else:
#Faz uma lista das palavras na linha
        words=line.split()
    for word in words:
        if word == words[5]:
            hours= word.split(':')
#Fazer lista de horários
            lt.append(hours[0])
        else: continue
#Contar horários
for hour in lt:
    counts [hour] = counts.get (hour,0) + 1
for hour, count in sorted (counts.items()):
    print (hour, count)
