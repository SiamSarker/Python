
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


duplicates = list(set([x for x in some_list if some_list.copy(x) > 1]))

print(duplicates)





