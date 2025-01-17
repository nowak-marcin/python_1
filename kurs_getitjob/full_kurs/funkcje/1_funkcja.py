# return - konczy dzialanie funcji w lini,w ktorej sie znajduje

def czy_to_kobieta(imie):
    if imie[-1] == 'a':
        return 'to kobieta'
    else:
        return 'to mezczyzna'


print(czy_to_kobieta('Adam'))
print(czy_to_kobieta('Magda'))
wynik = (czy_to_kobieta(input('podaj imie: ')))
print(wynik)