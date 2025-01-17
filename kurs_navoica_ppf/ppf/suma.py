suma = 0
while True:
    dana = input('Liczba do sumowania: [enter = koniec]')
    if dana == '':
        break
    liczba = float(dana)
    if liczba <=0:
        continue
    suma += liczba
print('suma = ', suma)










