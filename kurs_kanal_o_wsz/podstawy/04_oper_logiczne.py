# operatory logiczne - or, and, not

wiek = int(input('Podaj wiek: '))
kasa = int(input('Podaj ile masz pieniedzy: '))

if wiek >= 18 and kasa >= 40:
    print('dorosły, może wejść')
elif wiek < 18:
    print('nieletni, inny film')
else:
    print('nie może wejść')
print('Podsumowanie:','Klient ma lat:',wiek,'Ilość pieniędzy:',kasa)

