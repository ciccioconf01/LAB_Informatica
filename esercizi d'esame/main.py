from operator import itemgetter

infile1=open("passaggi.txt","r")
infile2=open("tempi.txt","r")
lista=[]
lista2=[]
data=input("inserisci la data da analizzare (formato aaaa-mm-gg)")
for line in infile1:
    line.rstrip()
    lista=line.split()
    if lista[1]==data:
        lista2.append(line.split())

lista2.sort(key=itemgetter(0))
for i in range(1,len(lista2)):
    if lista2[i-1][0]==lista2[i][0]:
        numimpianto=lista2[i-1][3]
        orari=lista2[i][2].split(":")
        tottempo=int(orari[0])*360+int(orari[1])*60+int(orari[2])
        orari2=lista2[i-1][2].split(":")
        tottempo2=int(orari2[0])*360+int(orari2[1])*60+int(orari2[2])
        differenza=abs(tottempo-tottempo2)
        infile2=open("tempi.txt")
        for line in infile2:
            line.rstrip()
            lista3=line.split()
            if lista3[0]==numimpianto:
                orari3=lista3[1].split(":")
                tempo=int(orari3[0])*60+int(orari3[1])
                diff=differenza-tempo
                if diff<0:
                    print("ANOMALIA")
                    print("ID", lista2[i][0],"Numero impianto",lista2[i][3],"Ora:", lista2[i][2])
        infile2.close()
