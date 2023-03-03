from datetime import datetime as dt

def time(func):
    def wrapper():
        start = dt.now()
        func()
        end = dt.now()

        result_time = end - start
        print(result_time)
    return wrapper()

@time
def test():
    sum = 0
    for i in range(100000000):
        sum += i
    print(sum)

