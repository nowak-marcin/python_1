class User:
    def __init__(self, name, mail, age):
        self.name = name
        self.mail = mail
        self.age = age

    def print_info(self):
        print(self.name, self.mail, self.age)

    def is_men(self):
        return self.name[-1:] != 'a'


user1 = User('marcin', 'marcin2204@op.pl', 40)
user2 = User('ewa', 'ewa0304@op.pl', 44)

user1.print_info()
user2.print_info()
print(user1.is_men())
print(user2.is_men())