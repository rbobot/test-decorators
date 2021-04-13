def outer(func):
    def inner(a, b):
        print("My message")
        return func(a, b)

    return inner

def div(a, b):
    return a / b

var = outer(div)
print(type(var))
print(var(1, 2)) # = print(outer(div)(1, 2))