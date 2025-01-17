class Ubranie:
    def __init__(self, material, kolor='błękitny'):
        self.material = material
        self.kolor = kolor

    def __str__(self):
        return self.material + ' w kolorze ' + self.kolor


class Kurtka(Ubranie):
    def skorzana(self):
        return self.material == 'skóra'


class Spodnie(Ubranie):
    def __init__(self, material='jeans', kolor='niebieski'):
        super().__init__(material, kolor)

    def letnie(self):
        return self.kolor == 'biały'


u = Ubranie('wełna', 'szary')
k = Kurtka('bawełna', 'czerowny')
s = Spodnie('jeans', 'niebieski')

print(u, k, s, sep='\n')

j = Spodnie('jedwab')
print(j)

