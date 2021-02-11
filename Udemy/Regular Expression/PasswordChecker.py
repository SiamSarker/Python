import re

pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")

string = 'uiu@acbdxcvxc8'

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

