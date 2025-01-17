# zmienna lub metoda, która jest współdzielona przez wszytkie obiekty danej klasy
# możemy się do niej odwołąć przez klasę a nie przez obiekt

class Tunczyk:
    # tworzymy zmienna statyczna
    ilosc_tunczykow = 0

    def __init__(self, imie):
        self.imie = imie
        Tunczyk.ilosc_tunczykow += 1

    # tworzymy metode statyczna
    @staticmethod
    def getIloscTunczykow():
        print('aktualna ilosc:', Tunczyk.ilosc_tunczykow)


print(Tunczyk.ilosc_tunczykow)
tunczyk1 = Tunczyk('James')
print(Tunczyk.ilosc_tunczykow)
tunczyk2 = Tunczyk('Michael')
print(Tunczyk.ilosc_tunczykow)

print(tunczyk2.imie)
print(tunczyk1.imie)

Tunczyk.getIloscTunczykow()