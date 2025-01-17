# dziedziczenie - hierarchiczne dzielenie się cechami między klasami z nad-klasy do pod-klasy

class Ryba():
    def __init__(self, imie='nemo', wiek=0):
        self.imie = imie
        self.wiek = wiek

    def wyswietl(self):
        print('czesc, jestem', self.imie, 'i mam', self.wiek, 'lat.')

class Tunczyk(Ryba):
    def __init__(self, imie, wiek):
        super().__init__(imie, wiek)

    def wyswietl(self):
        super().wyswietl()
        print('... a w dodatku jestem super!')

    def pozegnanie(self):
        print(self.imie, 'żegna was!')


james = Ryba('James', 100)
george = Tunczyk('George', 35)

print(james.imie, james.wiek)
print(george.imie, george.wiek)

james.wyswietl()
george.wyswietl()
george.pozegnanie()

# sprawdzenie z jakiej klasy wywodzi się obiekt (instancja klasy)

print(type(james))
print(type(george))

# czy dany obiekt jest instancją danej klasy

print('czy james jest tuńczykiem? ', str(isinstance(james, Tunczyk)))
print('czy george jest tuńczykiem? ', str(isinstance(george, Tunczyk)))
print('czy george jest rybą? ', str(isinstance(george, Ryba)))