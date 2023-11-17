# Calling function within a function
# def add(a, b):
#     return (a + b)

# def mul(val):
#     return 5 * val

# print(mul(add(2, 3)))

# enumerate function
val = ['red', 'black', 'blue']
# for i in range(len(val)):
#     print(i, val[i])

# out:
# (0, 'red')
# (1, 'black')
# (2, 'blue')
# for i in enumerate(val):
#     print(i)

# out:
# 0 red
# 1 black
# 2 blue
for i, j in enumerate(val):
    print(i, j)

# print(enumerate(val)) #returns enumerate object