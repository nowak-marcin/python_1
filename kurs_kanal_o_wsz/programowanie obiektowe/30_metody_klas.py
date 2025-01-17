# metoda klasy - ustanowienie metody dla klasy, którą można wywołać z klasy a nie z obiektu
# aby wywołać classmethod nie trzeba tworzyć specjalnie obiektu, można odwołać się bezpośrednio

# metoda statyczna - j.w. ale nie przyjmuje elementu domyślnego cls

class Czlowiek:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw(self):
        print('nazywam się: ' + self.imie)

    @classmethod
    def nowy_czlowiek(cls, imie):
        return cls(imie)

    @staticmethod
    def przywitaj(powitanie):
        print('cześć ' + powitanie)


czlowiek1 = Czlowiek.nowy_czlowiek('marcin')
czlowiek1.przedstaw()

czlowiek2 = Czlowiek.nowy_czlowiek('janusz')
czlowiek2.przedstaw()

Czlowiek.przywitaj('przyjacielu!')
czlowiek2.przywitaj('kolego!')