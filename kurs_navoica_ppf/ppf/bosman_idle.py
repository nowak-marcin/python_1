#program obliczający kaucję za butelki

#wpisz liczbę butelek
iloscButelek = int(input('Wpisz ilość butelek: '))
print('Twoja ilość butelek to: ', iloscButelek)

#wzór wyliczający kaucję za wszytkie butelki
kaucja = iloscButelek * 0.50

#wyświetl łączną kaucję za butelki                   
print(f'Brawo!!! Twoja kucja za wszytkie butelki wynosi: {kaucja} PLN')

#sprawdzenie czy masz butelki po Bosmanie
bosmanIlosc = int(input('Ile masz butelek po Bosmanie? '))

#obliczenie kaucji za Bosmany
bosmanKaucja = bosmanIlosc * 0.50

#sprawdzenie czy jest paragon
paragon = str(input('Czy masz paragon? [TAK/NIE] '))
if paragon == 'TAK':
    paragon = True
else:
    paragon = False

#co możesz zrobić z butelkami
if bosmanIlosc > 1 and paragon:
    print(f'Brawo!!! Masz {bosmanIlosc} butelek po Bosmanie - idź do Społem i oddaj wszystkie!')
    print('Kaucja za butelki po Bosmanie wyniesie:', bosmanKaucja, 'PLN')
elif paragon == False:
    print('Zjebałeś!!! Trzeba zawsze brać paragon! Wymień 1:1 na pełne:)')
elif bosmanIlosc == 1:
    print('Z jedną butelką to się nie opłaca z domu wychodzić!')
else:
    print('Tylko cioty nie piją Bosmana!')
print('Na zdrowie!!!')

    

