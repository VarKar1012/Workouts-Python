# To create a new sequence based on the existing sequence.
# 4types: list, set, dictionary and generator comprehension

# List comprehension

# temp = []
# for i in range(1, 8):
#     temp.append(i**2)
# print(temp)
# #    ||
# #    \/
# a = [i*i for i in range(1,8)]
# print(a)

# import math
# l = [math.sqrt(i) for i in range(1, 8)]
# print(l)

# val = [2, 3, 4, 5, 6 ,7 ,8]
# l = [i for i in val if i%2 == 0]
# l = {i for i in val if i%2 == 0}
# l = (i for i in val if i%2 == 0) # returns a generator object
# to access gen obj.
# 1. looping
# for i in l:
#     print(i)
# 2. next() fn
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(l)

# a = ['devin', 'dainty', 'david']
# b = ['abin', 'afitha', "jessica"]

# # c = [(i, j) for i in a for j in b]
# c = [(a[i], b[i]) for i in range(len(a))]
# print(c)

# dictionary comprehension
# a = [1,2,3,4,5]
# c = {}
# for i in a:
#     c[i] = i ** 2
# print(c)

# c = {i:i**2 for i in a}
# print(c)

# a = ['devin', 'dainty', 'david']
# b = ['python', 'cyber', "analyst"]

# c = {a[i]:b[i] for i in range(len(a))}
# d = {i:j for i,j in zip(a,b)}
# print(c)
# print(d)














