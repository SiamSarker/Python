with open('test.txt') as my_file:
    print(my_file.readlines())

with open('test.txt', mode='a') as my_file2:
    text = my_file2.write(" hello")
    print(text)

# print(my_file.readline())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# my_file.readline()
# print(my_file.readline())

# print(my_file.readlines())
#
# my_file.close()
