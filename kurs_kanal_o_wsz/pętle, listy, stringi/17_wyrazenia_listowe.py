# wyrażenia listowe - umożliwiają operacje na każdym elemencie listy
# bez modyfikacji pierwotnej listy

myList = list(range(10))
print(myList)

newLista = [i*2 for i in myList]
newLista2 = [i+2 for i in myList if i%2==0]
print('pierwotna:',myList, 'wynikowa:', newLista, 'wynikowa2:', newLista2)

# String formatter - wskazanie miejsca z ciągu znaków ze wskazaniem jakie argumenty mają się poajawić

argumenty = ["marcin",30]
tekst = 'Cześć mam na imię {0} i mam {1} lat.'.format(argumenty[0], argumenty[1])
print(tekst)
tekst = 'Cześć mam na imię {imie} i mam {wiek} lat.'.format(imie=argumenty[0], wiek=argumenty[1])
print(tekst)