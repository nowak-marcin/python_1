lista = [1,2,4,6]

suma = 0
for i in range(4):
    suma += lista[i]
print(suma)

# wariant bez podawania ilości elementów

iloczyn = 1
for element in lista:
    iloczyn *= element
print(iloczyn)

# in - sprawdzenie czy element jest na liście
#>>> 2 in lista
#>>> True
#>>> 2 not in lista
#>>> False

# wycinek - przekształcenie fragmentu listy w nową listę
# [a:b]
# a - indeks pierwszego elementu nowejlisty
# b - indeks pierwszego elementu nie branego do nowej listy
#>>> lista = [0,1,2,3,4]
#>>> lista[1:3]
#>>> [1,2]

# wstawianie elementów do listy

myList = []
for i in range(10):
    myList.append(2**i)
print(myList)

myList = []
for i in range(10):
    myList.insert(0,2**i)
print(myList)

# maksimum na liście

mojaLista = [1,100,5,68,8,-1]
maksimum = mojaLista[0]
for i in range(1, len(mojaLista)):
    if mojaLista[i] > maksimum:
        maksimum = mojaLista[i]
print(maksimum)

for myElement in mojaLista:
    if myElement > maksimum:
        maksimum = myElement
print(maksimum)
    

    
        









