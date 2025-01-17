# hermetyzacja - ukrycie danych lub meteod w klasie
# odpowiednik private: _lista lub __lista
# (tylko informacyjnie, nie blokuje faktycznego dostępu spoza klasy)

class Test:
    _lista = []
    def dodaj(self, argument):
        self._lista.append(argument)

    def zdejmij(self):
        if len(self._lista) > 0:
            return self._lista.pop(len(self._lista) - 1)
        else:
            return


obj = Test()
obj.dodaj('a')
obj.dodaj('b')
obj.zdejmij()
print(obj._lista)

# lub:
# print(obj._Test__lista)
