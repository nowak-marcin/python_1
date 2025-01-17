# klasy - przechowują zmienne i funkcje (tu: metody)
# stanowi abstarakcyjny szablon do tworzenia konkretnego obiektu
# self - argument ukryty, domyślny, pozwala odwołać się do klasy

class Czlowiek:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstawSie(self, powitanie = 'cześć'):
        return powitanie + ', mam na imię ' + self.imie + ",lat " + str(self.wiek) + '.'

obiekt = Czlowiek('marcin', 30)

print(obiekt.przedstawSie('witam'))

obiekt2 = Czlowiek('ewa', 22)

print(obiekt2.przedstawSie())