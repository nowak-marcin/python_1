suma = ile = 0
while True:
    dana = input('Podaj liczbę: [enter = koniec]')
    if dana == '':
        break
    liczba = float(dana)
    suma += liczba
    ile += 1
if ile == 0:
    print('Nie podałeś żadnej liczby!')
else:
    print('suma = ', suma)
    print('średnia = ', suma / ile)










