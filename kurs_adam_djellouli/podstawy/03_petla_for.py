for i in range(4,8,2):
    print(i)
print('koniec1')

# suma liczb parzystych od 1 do 5:

suma = 0
for i in range(5):
    if i % 2 == 0:
        suma += i
        print('suma pośrednia:', suma)
print('suma końcowa:',suma)
print('koniec2')

# oprocentowanie środków i wyliczneie kapitału

lata = int(input('Podaj okres: '))
oprocentowanie = float(input('Oprocentowanie wynosi: '))
kapital = int(input('Podaj kwotę początkową: '))

if lata > 10:
    print('Maksymalny okres to 10 lat!')
elif kapital < 10000:
    print('Minimalna kwota to 1000 zł')
else:
    for i in range(lata):
        kapital = kapital + kapital*oprocentowanie
        print('Twój kapitał po', i+1, 'latach wynosi:', kapital)
print('Twój kapitał końcowy wynosi:', kapital)
print('koniec3')
