# iterator - obiekt słuzacy do przegladania elementów kolekcji
# (listy, zbiory, slowniki czy krotki są iterowalne

lista = [1, 2, 4]

# iter - inicjator iteracji
# next - zwraca wartosc kolejnego elementu

iterator1 = iter(lista)
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))


class MojIterator():
    def __init__(self, max=10):
        self.x = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        x = self.x
        if x > self.max:
            raise StopIteration
        self.x += 5
        return x

for i in MojIterator(21):
    print(i)