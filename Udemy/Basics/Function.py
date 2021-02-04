
def say_hello():
    print("Hello")

say_hello()

# Rule: params, *args, default parameters, **kwargs

def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(highest_even([10,2,3,4,5]))


total = 0

def count():
    global total   # do not use
    total += 1
    return total

count()
print(total)
