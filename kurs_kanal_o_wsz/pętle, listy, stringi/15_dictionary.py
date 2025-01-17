# słownik - klucz-wartość

dniTygodnia = {1:'poniedziałek', 2:'wtorek', 7:'niedziela'}

print(dniTygodnia[7])
dniTygodnia[3] = 'środa'
dniTygodnia['a'] = 100
print(dniTygodnia)

# funkcja get - pobranie elementu o podanym indeksie lub zwrócenie info o braku indeksu (opcjonalnie)

print(dniTygodnia.get(7, 'brak danych'))
print(dniTygodnia.get(8, 'brak danych'))
print('koniec1')

# keys i values - wyświetlanie kluczy i wartości całego słownika

for l in dniTygodnia.keys():
    print(l)
for l in dniTygodnia.values():
    print(l)
print('koniec2')

# usuwanie elementu ze słownika

dniTygodnia.pop(1)
print(dniTygodnia.keys())
print(dniTygodnia.values())
print('koniec3')