from math import sqrt
num=int(input("Scegliete un numero intero, n: questa funzione calcolerà tutti i numeri primi fino a n "))
insieme=set()
for i in range (2,num):
    insieme.add(i)
x=int(sqrt(num))

for element in insieme.copy():

   for i in range(2,x):

        if element%i==0 and element!=i:
            insieme.discard(element)







print(insieme)


