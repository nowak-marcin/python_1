# klasa bazowa

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# klasa dziedzicząca (subklasa)
# super - szuka w klasach bazowych metod wywołanych w subklasie

class Dog(Animal):
    def voice(self):
        print('hau, hau!')

class Wolf(Dog):
    def voice(self):
        print('jestem wilkiem!')
        super().voice()

class Cat(Animal):
    def voice(self):
        print('mau, mau!')

# utworzenie obiektów

dog = Dog('reksio', 10)

print(dog.name, dog.age)
dog.voice()

cat = Cat('mruczek', 8)

print(cat.name, cat.age)
cat.voice()

wolf = Wolf('T1000', 14)

print(wolf.name, wolf.age)
wolf.voice()