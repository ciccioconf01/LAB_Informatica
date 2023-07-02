dizionario1={5:4, 9:2, 10:9}
dizionario2={5:3, 8:2, 9:9}
lista=[0]*100
for element in dizionario1:
    chiave=element
    lista[element-1]=dizionario1[element]

for element in dizionario2:
    chiave=element
    if lista[element-1]==0:
        lista[element-1]=dizionario2[element]
    else:
        lista[element-1]=lista[element-1]+dizionario2[element]

print(lista)
