import math

# init i add
# operatory porównania (less then, less equal, equal, not equal, lenght)

class Punkt2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.odleglosc = math.sqrt(x**2 + y**2)

    def __add__(self, drugi):
        return Punkt2D(self.x + drugi.x, self.y + drugi.y)

    def __lt__(self, drugi):
        return self.odleglosc < drugi.odleglosc

    def __eq__(self, drugi):
        return self.x == drugi.x and self.y == drugi.y

    def __len__(self):
        return int(round(self.odleglosc, 0))


p1 = Punkt2D(2,5)
p2 = Punkt2D(4,5)
p3 = p1 + p2

print(p3.x, p3.y)
print(p1 < p2, p1.odleglosc, p2.odleglosc)
print(p3 < p2)
print(p1 == p2)
print(p2 == p2)
print(len(p3), p3.odleglosc)

