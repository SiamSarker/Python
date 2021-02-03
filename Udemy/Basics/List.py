li = [1,2,3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1,2,'a', True]

# list is from of array

# Data Structure
print(li2[2])

# List slicing

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

# lits are mutable

amazon_cart[0] = 'laptop'

print(amazon_cart)

print(amazon_cart[1:3])

new_cart = amazon_cart[:]

# if you wanna copy a list use slicing lake  new_cart = amazon_cart[:]
# else it's just use as pointers


basket = [1,2,3,4,5]
print(len(basket))

# adding
basket.append(100)
new_list = basket
print(new_list)
print(basket)

# insert
basket.insert(4, 56)

basket.extend([100, 1001])
print(basket)

# remove

basket.pop()
print(basket)

basket.remove(4)
print(basket)




# index

print(basket.index(100, 0, 6))


# python keyword


print(100 in basket)
print('i' in 'hi')

print(basket.count(100))


basket = ['a', 'b','c', 'd', 'e', 'd']

# basket.sort()

print(sorted(basket))
print(basket)



basket.reverse()
print(basket)

print(list(range(100)))

new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'Siam'])

print(new_sentence)

# list unpacking

a, b, c, *other, d = [1, 2, 3, 4, 5, 6]

print(other)
print(d)


















