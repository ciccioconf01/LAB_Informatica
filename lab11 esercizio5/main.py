infile=open("parolacce.txt","r")
insieme=set()
for line in infile:
    line.rstrip()
    lista=line.split()
    for i in range(len(lista)):
        insieme.add(lista[i])

infile.close()
infile=open("testo.txt","r")
outfile=open("testofinale.txt","w")

for line in infile:
    line.rstrip()
    lista=line.split()
    for i in range(len(lista)):
        if lista[i] not in insieme:
            outfile.write(lista[i])
            outfile.write(" ")
        else:
            x=len(lista[i])
            stringa="*"*x
            
            outfile.write(stringa)
            outfile.write(" ")
