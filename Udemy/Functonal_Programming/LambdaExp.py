# lambda expression
# use function only once

from functools import reduce

my_list = [1, 2, 3]


def multiply_by2(li):
    return li * 2


def check_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


#lambda param: action(param)


print(list(map(lambda item: item*2, my_list)))
print(my_list)