class Polonez:
    def __init__(self):
        print('polonez jest cool!')
        self.hamuj()

    def hamuj(self):
        print('stop! hamuj!')

    def skrecaj(self, strona):
        print(f'skrecaj w: {strona}')

    def iloscPaliwa(self, litry = '0'):
        return 'ilosc paliwa: ' + str(litry) + ' litrow'

    def info(self, skrecaj, iloscPaliwa):
        return 'skręcaj w: ' + skrecaj + ', iloscPaliwa: ' + iloscPaliwa

moj_polonez = Polonez()
moj_polonez.hamuj()
moj_polonez.skrecaj('prawo')
zuzycie_paliwa = moj_polonez.iloscPaliwa(50)
print(zuzycie_paliwa)

twoj_polonez = Polonez()
zuzycie_paliwa = twoj_polonez.info('lewo', '100')
print(zuzycie_paliwa)