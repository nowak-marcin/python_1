# klasa - nasz typ danych, składająca się z:
# atrybuty - konkretne dane np zmienne użyte w klasie
# metody - funkcje zdefiniowane w klasie
# init
# self - za jego pomocą wchodzi w interakcje z aktualną instancją klasy

class osoba:
    def __init__(self, imie = 'brak', wiek = 0, zarobki = 0):
        self.imie = imie
        self.wiek = wiek
        self.zarobki = zarobki
    def przywitanie(self):
        print('Cześć, jestem', self.imie, 'i mam lat:', self.wiek)

# obiekt - wybrana instancja (zastosowanie) zdefiniowanej klasy

ja = osoba('adam', 33, 6000.5)
ty = osoba('marcin', 39, 7000.5)
brakdanych = osoba()

ja.przywitanie()
ty.przywitanie()
brakdanych.przywitanie()
print(ja.imie, ja.wiek)
print(ty.imie, ty.zarobki)
print(brakdanych.imie, brakdanych.wiek)


