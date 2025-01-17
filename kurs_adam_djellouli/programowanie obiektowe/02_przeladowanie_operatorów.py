# klasa reprezentująca wektor 2D (x, y)
# self.x - jaki atrybut będzie przekazany do obiektu, x - jaka dana będzie mu w nim przkazana
# przeładowanie operatorów - nadanie operatorom nowego znaczenia np dla "+" lub "*"
# __add__ - metoda specjalna do dodawania

class Wektor:

    # inicjalizacja

    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    # zastąpienie "+" metodą add

    def __add__(self, other):
        return Wektor(self.x + other.x, self.y + other.y)

    # zatąpienie "+=" metodą iadd

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    # zastąpinie mnożenia metodą mul

    def __mul__(self, other):
        return Wektor(self.x * other.x, self.y * other.y)

    # funkcja do wyświetlania wyniku:

    def wyswietl(self):
        return 'x wynosi: ' + str(self.x) + ', y wynosi:' + str(self.y)

wektor1 = Wektor()
wektor2 = Wektor(4,8)
wektor3 = wektor1 + wektor2

print(wektor1.x, ',', wektor1.y)
print(wektor2.x, ',', wektor2.y)
print(wektor3.x, ',', wektor3.y)

wektor3 += wektor2
print(wektor3.x, ',', wektor3.y)
wektor4 = wektor2 * wektor2
print(wektor4.x, ',', wektor4.y)

print('lub z funkcji wyświetl: ')
print('Wektor1:', wektor1.wyswietl())
print('Wektor2:', wektor2.wyswietl())
print('Wektor3:', wektor3.wyswietl())
print('Wektor4:', wektor4.wyswietl())
