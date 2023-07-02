infile=open("labirinto.txt","r")
lista=[]
tabella=[]
i=0
for i in range(9):
    x=[0]*9
    tabella.append(x)

dizionario=dict()
insieme=set()
i=0
for line in infile:
    line.rstrip()
    lista=line

    for j in range(9):
        tabella[i][j]=lista[j]
    i+=1

for i in range(9):
    for j in range(9):
        print(tabella[i][j], end=" ")
    print()

for i in range(9):
    for j in range(9):
        if tabella[i][j]!="*":
            if tabella[i-1][j]!="*":
                insieme.add([i-1][j])
            if tabella[i][j-1]!="*":
                insieme.add([i][j-1])
            if tabella[i+1][j]!="*":
                insieme.add(i+1+j)
            if tabella[i][j+1]!="*":
                insieme.add([i][j+1])

            chiave=tuple([i][j])
            dizionario[chiave]=insieme




