def outer(func):
    def inner(*args, **kwargs):
        print("My message")
        return func(*args, **kwargs)

    return inner

@outer
def div(a, b):
    return a / b

print(div(1, 2))