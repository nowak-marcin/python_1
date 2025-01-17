# tworzenie pliku txt w trybie wyczyść i edytuj (w) edytuj (a) lub do odczytu (r)

myPlik = open('14_mytest.txt', 'a')

# sprawdzenie czy plik jest w trybie edycji (w)/(a) - funkcja writable

print(myPlik.writable())

# zapis danych string do pliku - funkcja write

if myPlik.writable():
    myPlik.write(input('podaj tekst: ') + '\n')
else:
    print('plik nie jest w trybie edycji')
myPlik.close()

# sprawdzenie czy plik jest w trybie do odczytu - readable
# wyświelanie danych do odczytu - funkcje read i readlines

myPlik = open('14_mytest.txt', 'r')
if myPlik.readable():
    tekst = myPlik.read()
    print(tekst)
print('koniec1')

myPlik = open('14_mytest.txt', 'r')
if myPlik.readable():
    tekst = myPlik.readlines()
    print(tekst)
    for l in tekst:
        print(l)
print('koniec2')

myPlik = open('14_mytest.txt', 'r')
if myPlik.readable():
    for l in myPlik:
        print(l)
print('koniec3')

myPlik.close()