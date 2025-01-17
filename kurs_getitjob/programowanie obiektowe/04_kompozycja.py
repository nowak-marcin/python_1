# dziedziczenie - obiekt B wywodzi się z obiektu A (dziedziczy po nim)
# np obiekt Auto wywodzi się z obiektu Pojazd, bo każde auto jest pojazdem (dziedziczy jego cechy)

# kompozycja - klasa B ma/posiada cechy klasy A
# np klasa Silnik posiada cechy klasy Auto, bo każde Auto ma Silnik
# polega na przekazaniu cechy (metody, pola) z klasy B do klasy nadrzędnej A

class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor
class Auto(Pojazd):
    def __init__(self, silnik, kolor):
        self.silnik = silnik
        super().__init__(kolor)
class Silnik:
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc


silnik = Silnik(5000)
kolor = 'niebieski'
my_auto = Auto(silnik, kolor)

print(my_auto.silnik.pojemnosc)
print(my_auto.kolor)

