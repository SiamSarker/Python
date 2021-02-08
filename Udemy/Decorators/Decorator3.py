# decorator pattern

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func

# super booster
@my_decorator
def hello(x, emoji = ':('):
    print(x, emoji)


hello('hiii')