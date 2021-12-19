try:
    with open('tsdcdst.txt', mode='r') as my_file2:
        text = my_file2.read()
except FileNotFoundError as err:
    print('file not found')
    raise err
except IOError as err:
    print('IO error')
    raise err