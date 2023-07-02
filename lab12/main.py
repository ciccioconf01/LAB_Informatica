infile1=open("presenze.txt","r")
infile2=open("sospetti.txt","r")
lista=[]
dizionario={}
for line in infile1:
    lista=line.rstrip().split(",")
    key=lista[0]
    lista.pop(0)
    dizionario[key]=lista
key=0
for line in infile2:
    flag="false"
    sospetto=line.rstrip()
    print("***Contatti del cliente:",sospetto)
    if sospetto in dizionario:


        for key in dizionario:
            if key!=sospetto:

                if int(dizionario[key][1])>=int(dizionario[sospetto][1]) and int(dizionario[key][1])<=int(dizionario[sospetto][2]) or int(dizionario[key][2])>=int(dizionario[sospetto][1]) and int(dizionario[key][2])<=int(dizionario[sospetto][2]) or (int(dizionario[key][1])<=int(dizionario[sospetto][1]) and int(dizionario[key][1])<=int(dizionario[sospetto][2]) and int(dizionario[key][2])>=int(dizionario[sospetto][1]) and int(dizionario[key][2])>=int(dizionario[sospetto][2])):
                    print("E' stato in contatto con:",key,", Telefono:",dizionario[key][0])
                    flag="true"

        if flag=="false":
            print("Il cliente",sospetto,"non ha avuto contatti")

    else:
        print(sospetto,"non è in elenco")
