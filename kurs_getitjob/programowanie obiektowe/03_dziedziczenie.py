# super przekazanie metody z jednej klasy do innej np z init do init

class Auto:
    def __init__(self, waga):
        self.waga = waga

    def jedz(self):
        return 'jade prosto'

class AutoSpalinowe(Auto):
    def __init__(self, ilosc_cylindrow, waga):
        self.ilosc_cylindrow = ilosc_cylindrow
        super().__init__(waga)

    def sprawdz_olej(self):
        return 'olej jest OK'

class Polonez(AutoSpalinowe):
    def __init__(self, model, ilosc_cylindrow, waga):
        self.model = model
        super().__init__(ilosc_cylindrow, waga)

    def jazda_bokiem(self):
        return 'jadę bokiem'


moje_auto = AutoSpalinowe(6, 1800)
print(moje_auto.sprawdz_olej(), '-', moje_auto.jedz())
print(moje_auto.waga)

moje_auto = Polonez('caro plus', 6, 1500)
print(moje_auto.jazda_bokiem(), '-', moje_auto.model, '-', moje_auto.waga)

print(Polonez.__mro__)