def decorate(func):
    def wrapper(value):
        print("wrapper")
        func(value)
    return wrapper

@decorate
def test(value):
    print(f"test, value: {value}")

test("value in test")