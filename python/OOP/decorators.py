def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()

def decorators(func):
    def wrapper(*args, **kwargs):
        print('parameters of the function', *args)
        
        
        b = func(*args, **kwargs)
        print('after execution')

        return b
    return wrapper

@decorators
def add(a, b):
   print(a+b)

add(6, 10)
