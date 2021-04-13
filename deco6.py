def second_outer(param):
    def outer(func):
        def inner(a, b):
            print(param)
            return func(a, b)

        return inner
    return outer

@second_outer("My message")
def div(a, b):
    return a / b

print(div(1, 2))