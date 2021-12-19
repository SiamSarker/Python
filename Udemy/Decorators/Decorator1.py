# decorator

def my_decorator(func):
    def wrap_func():
        print('*********')
        func()
        print('*********')
    return wrap_func

# super booster
@my_decorator
def hello():
    print('hellloooo')


@my_decorator
def bye():
    print('see ya later')


hello()
bye()