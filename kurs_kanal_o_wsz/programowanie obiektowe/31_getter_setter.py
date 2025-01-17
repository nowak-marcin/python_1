# property - ustawienie właściwości aby wywołać daną jako zmienną a nie funkcję i tylko do odczytu
# getter, setter - tworzony tylko dla danej właściwości, pozwala na pobranie lub
# modyfikację danej zmiennej z property
class KontoBankowe:
    __stan = 0

    @property
    def stan_konta(self):
        return self.__stan

    @stan_konta.getter
    def stan_konta(self):
        return 'stan konta: ' + str(self.__stan)

    @stan_konta.setter
    def stan_konta(self, newValue):
        self.__stan += newValue


konto = KontoBankowe()
print(konto.stan_konta)

konto.stan_konta = 50
print(konto.stan_konta)

konto.stan_konta = -20
print(konto.stan_konta)



