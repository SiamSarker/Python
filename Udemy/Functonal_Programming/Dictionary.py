# dictionary comprehension

simple_dictionary = {
    'a' : 1,
    'b' : 2
}
my_dict = {key: value**2 for key, value in simple_dictionary.items() if value%2 == 0 }
my_dict2 = {key: key*2 for key in [1,4,3] }

print(my_dict2)
print(my_dict)