print("My calculator")

def performArithmeticOp(a, b):
    return (add(a, b), sub(a, b), mul(a, b), div(a, b))

def add(a,b):
    print(a+b)

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b