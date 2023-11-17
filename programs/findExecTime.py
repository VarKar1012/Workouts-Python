# finding execution time using decorators.
import time

def findtime(func):
    def inner():
        t1 = time.time()
        func()
        t2 = time.time()
        print((t2-t1)*1000)
    return inner

@findtime
def square():
    squareList = []
    for i in range(1, 10000):
        squareList.append(i**2)

square()

