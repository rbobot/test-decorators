def second_outer(param):
    def outer(func):
        def inner(*args, **kwargs):
            print(param)
            return func(*args, **kwargs)

        return inner
    return outer

@second_outer("My message")
def div(a, b):
    return a / b

print(div(1, 2))