def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(19):
    print(x)


def fib2(num):
    a = 0
    b = 1
    result = []
    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


print(fib2(19))