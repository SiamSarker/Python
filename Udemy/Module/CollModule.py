from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 7]

# counts occurrence
print(Counter(li))

sentence = 'blah blah blah thining about python'

print(Counter(sentence))

dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})

print(dictionary['b'])


d = OrderedDict()
d['a'] =  1
d['b'] =  2

d2 = OrderedDict()
d2['a'] =  2
d2['b'] =  1

print(d2 == d)