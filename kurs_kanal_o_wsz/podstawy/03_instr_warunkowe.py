# operatory porównania

print(5 == 5)
print(5 != 5)
print(5 > 5)
print(5 <= 5)

# intrukcja warunkowa if, if not, elif, else

x = 5
y = 5

if x > y:
    print('x większe od y')
elif x == y:
    print('x równe y')
else:
    print('x mniejsze od y')
print('Koniec')

# promocja min. 2 piwa ze zniżką 50 lub 30%

piwo50 = ['Bosman', 'Połczyn', 'Bakalar']
piwo30 = ['Lech', 'Tyskie', 'Żywiec']
a = input('Podaj nazwę piwa: ')
ilosc = int(input('Liczba piw: '))
kaucja = 0.5 * ilosc

if a in piwo50 and ilosc >= 2:
    print('Wybrałeś piwo', a, 'Gratulacje, otrzymasz 50% zniżki!!!')
elif a in piwo30 and ilosc >= 2:
    print('Wybrłeś piwo', a, 'Gratulacje, masz 20% zniżki!')
elif a not in piwo50 and piwo30:
    print('Piwo', a, 'nie jest objęte promocją!')
else:
    print('Musisz kupić przynajmniej 2 piwa w tej promocji')
print('Kaucja za butelki wynosi', kaucja)

