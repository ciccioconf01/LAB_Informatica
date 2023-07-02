infile=open("movimenti.txt","r")
x=[]
lista=[]
piano=0
accumula=0
consumo=0
conta=0
conta1=0
consumo1=0
accumulatorerisparmio=0
for line in infile:
    line.rstrip
    x=line.split()
    lista.append(int(x[0]))
    lista.append(int(x[1]))

for i in range(0,len(lista)):



    if  piano<lista[i]:
        differenza=lista[i]-piano
        conta1=conta1+differenza
        consumo1=differenza*100
        accumulatorerisparmio=accumulatorerisparmio+consumo1


    differenza=abs(lista[i]-piano)
    conta=conta+differenza
    consumo=differenza*100
    accumula=accumula+consumo
    piano=lista[i]

print("Ascensore senza risparmio, spostamenti=",conta,"consumo=",accumula)
print("Ascensore con risparmio, spostamenti=",conta1,"consumo=",accumulatorerisparmio)
print("risparmio assoluto=",accumula-accumulatorerisparmio)
operazione=(accumula+accumulatorerisparmio)/(accumulatorerisparmio+accumula)
percentuale=operazione*100
print("risparmio in percentuale=",percentuale)


