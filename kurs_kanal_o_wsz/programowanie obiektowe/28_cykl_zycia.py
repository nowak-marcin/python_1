# destruktor - magiczna metod del

class Test:
    def __del__(self):
        print('Bye Class')


obj = Test()
