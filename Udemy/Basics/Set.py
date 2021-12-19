#  set

my_list = [1,2,3,4,5,6]

#my_set = {1,2,3,4,5,5}

print(set(my_list))

print('*', end='')
print('')


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)