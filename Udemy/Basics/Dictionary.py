# unordered key value pair

dictionary = {
    'a' : [1, 2, 3],
    'b' : 'hello',
    'x' : True
}
print(dictionary)

my_list = [
{
    'a' : [1, 2, 3],
    'b' : 'hello',
    'x' : True
}
]

print(my_list)

print(dictionary.get('x', 43))   # if doesn't exists other value

user2 = dict(name = 'Siam')
print(user2)

print('a' in dictionary.keys())
print('b' in dictionary.items())
print(dictionary.update({'age': 20}))
print(dictionary)

