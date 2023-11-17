# To create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and prints the result.
# Sample Output:
# 25
# 48

def add(val):
    add = lambda val: val + 15
    return add(val)

def multiply(m, n):
    mul = lambda n, m: n * m
    return mul(m, n)

x = 25
y = 48
print(add(x))
print(multiply(x, y))
