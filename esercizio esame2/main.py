infile1=open("serieA.txt","r")
infile2=open("filtri.txt","r")
lista=[]
i=0
for line in infile1:

    line.rstrip()
    informazioni=line.split()

    lista.append(informazioni)
    infile2=open("filtri.txt","r")
    for line2 in infile2:

        line2.rstrip()
        informazioni2=line2.split()
        if informazioni[0]==informazioni2[0] and informazioni[1]==informazioni2[1]:
            lista.pop(i)
            i=i-1
    infile2.close()
    i+=1

print(lista)

minimo=lista[0][2]
for i in range(len(lista)):
    if lista[i][2]<minimo:
        minimo=lista[i][2]
        x=lista[i][0]
        y=lista[i][1]

print("il giocatore con il minor numero di presenze è:",x,"",y,"numero presenze:",minimo)

massimo=lista[0][2]
for i in range(len(lista)):
    if lista[i][2]>massimo:
        massimo=lista[i][2]
        x=lista[i][0]
        y=lista[i][1]

print("il giocatore con il maggior numero di presenze è:",x,"",y,"numero presenze:",massimo)






