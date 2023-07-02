infile=open("file.txt","r")
risposta=""
dizionario=dict()
for line in infile:
    line.rstrip()
    lista=line.split()

    dizionario[lista[1]]=lista[2]
risposta=input("inserisci il nome della nazione di cui si vuole vedere il reddito pro capite, inserire quit per terminare ")
while risposta!="quit":
    print(dizionario[risposta])
    risposta=input("inserisci il nome della nazione di cui si vuole vedere il reddito pro capite, inserire quit per terminare ")

