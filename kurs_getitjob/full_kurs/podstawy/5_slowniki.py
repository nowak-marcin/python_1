lista = [1, 2, 'adam']

# słownik - klucz + wartość

nasz_slownik = {'adam': 32, 'marek': 18, (1, 2): 'krotka'}

print(nasz_slownik)
print(nasz_slownik['marek'])

# metoda get - zwraca wartość dla przypisanego klucza
# lub podaną wartość jesli nie znajdzie dopasowania

print(nasz_slownik.get('marek'))
print(nasz_slownik.get('zbyszek', 'brak'))
print(nasz_slownik.get('adam', 'brak'))
