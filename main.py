
def my_decorator(func):
    def wrapper():
        print("Line number is 1")
        func()
        print("Line number is 3")
    return wrapper()
def test():
    print("Line number is 2")

my_decorator(test)
