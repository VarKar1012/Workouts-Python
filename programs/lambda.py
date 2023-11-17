# def sumf(a, b, c):
#     return a + b + c

# print(sumf(3,4,5))

# expr = lambda a,b,c: a+b+c
# print(expr(3,4,5))


# print((lambda a,b,c: a+b+c)(3,4,5))


# [1,2,3,4,5] => [1,4,9,16,25]
# l = [1,2,3,4,5]
# square = lambda i: i ** 2
# out = [square(i) for i in l]
# print(out)

# l = ['var', 'karly', 'caress']
# l.sort()
# print(l) #['caress', 'karly', 'var']

# l.sort(key=len)
# print(l) #['var', 'karly', 'caress']

# l.sort(key=lambda x: len(x))
# print(l) #['var', 'karly', 'caress']

# l.sort(key=lambda x: len(x), reverse=True)
# print(l) #['caress', 'karly', 'var']

# example: output-7
def func(v=2):
    c = v * 2
    return c

x = 2
high = lambda x, func: x + func
print(high(3, func()))