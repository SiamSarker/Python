range(100)
list(range(100))

# start generator from the morning
# Good night


def generator_function(num):
    for i in range(num):
        yield i*2
# yield stops the loop everytime

# for item in generator_function(1000):
#     print(item)


g = generator_function(100)
next(g)
next(g)
next(g)
print(next(g))  # remembers previous yield value

# def make_list(num):
#     result = []
