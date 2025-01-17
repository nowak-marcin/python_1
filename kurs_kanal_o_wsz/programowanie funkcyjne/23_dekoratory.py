def decorator(funk):
    def wrapper():
        print('------')
        funk()
        print('------')
    return wrapper

def hello():
    print('hello world')

# bez dekoratora

hello()

# z dekoratorem

hello = decorator(hello)
hello()

# inny sposób

@decorator
def witaj():
    print('witaj świecie')

witaj()

