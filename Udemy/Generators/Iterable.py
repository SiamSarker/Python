def special_for(iterable):
    iterable = iter(iterable)
    while True:
        try:
            print(iterable)
            print(next(iterable)*2)
        except StopIteration:
            break


special_for([1, 2, 3])