stringa1=input("inserisci una stringa ")
stringa2=input("inserisci un'altra stringa ")
insieme1=set(stringa1)
insieme2=set(stringa2)
insiemetot=set()
alfabeto={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
lista=[]
lista2=[]
for element1 in insieme1:
    for element2 in insieme2:
        insiemetot.add(element1)
        insiemetot.add(element2)
        if element1==element2:
            lista.append(element1)




for element in insiemetot:
    if element in insieme1 and element not in insieme2 or element not in insieme1 and element in insieme2:
        lista2.append(element)

for element in insiemetot:
    alfabeto.discard(element)

print("le lettere che compaiono in entrambe le stringhe sono:",lista)
print("le lettere che compaiono in solo una delle due stringhe sono",lista2)
print("le lettere che non compaiono in nessuna stringa sono",sorted(alfabeto))
