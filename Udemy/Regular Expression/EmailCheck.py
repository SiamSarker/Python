import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string = 'uiu@ac.bd'

print('search' in string)

a = pattern.search(string)
# a = re.search('this', string)
#print(re.search('this', string))

print(a.span())
print(a.start())
print(a.end())
print(a.group())

b = pattern.findall(string)

print(b)

c = pattern.fullmatch(string)
print(c)

d = pattern.match(string)  # first match
print(d)

