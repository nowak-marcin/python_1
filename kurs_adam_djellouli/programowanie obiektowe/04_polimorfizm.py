# polimorfizm - różne działanie tej samej metody w różnych klasach

class Ksztalt:
    def __init__(self, nazwa='Ksztalt'):
        self.nazwa = nazwa

    def pole(self):
        print('brak danych na temat', self.nazwa)

class Trojkat(Ksztalt):
    def __init__(self, nazwa='Trojkat', a=2, h=2):
        super().__init__(nazwa)
        self.a = a
        self.h = h

    def pole(self):
        print('Pole figury', self.nazwa, 'wynosi:', self.a*self.h)

class Prostokat(Ksztalt):
    def __init__(self, nazwa='Prostokat', a=2, b=2):
        super().__init__(nazwa)
        self.a = a
        self.b = b

    def pole(self):
        print('Pole figury', self.nazwa, 'wynosi:', self.a*self.b)

class Kwadrat():
    def __init__(self, nazwa='Kwadrat', a=3):
        self.nazwa = nazwa
        self.a = a

    def pole(self):
        print('Pole figury', self.nazwa, 'wynosi:', self.a**2)

def wyswietl_pole(lista):
    for x in lista:
        x.pole()
        print(type(x))


ksztalt = Ksztalt()
trojkat = Trojkat()
prostokat = Prostokat()
kwadrat = Kwadrat()

lista = [ksztalt, trojkat, prostokat, kwadrat]
wyswietl_pole(lista)

