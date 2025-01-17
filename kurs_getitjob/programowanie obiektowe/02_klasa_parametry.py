class Polonez:
    def __init__(self, kolor):
        self.kolor = kolor
        self.ilosc_paliwa = 10
        self.spalanie_na_100 = 12

    def zasieg(self):
        zasieg = self.ilosc_paliwa * 100 / self.spalanie_na_100
        return zasieg


my_polonez = Polonez('czerwony')
my_polonez2 = Polonez('zielony')
print(my_polonez.kolor, my_polonez2.kolor)

print(my_polonez.zasieg(), my_polonez2.zasieg())

my_polonez.ilosc_paliwa += 10
print(my_polonez.zasieg(), my_polonez2.zasieg())