# def square(x):
#     return x*x

# l = [1, 3, 4]
# print(list(map(square, l)))

# print(list(map(lambda x: x*x, l)))

# a = [3,4,5]
# b = [4,5,6] 
# c = [6,7,8]
# print(list(map(lambda x,y,z: x+y+z, a, b, c)))

# filter function
# a = range(1,11)
# print(a)

# find list of even numbers from 1 to 10
# print(list(filter(lambda x: x%2 == 0, range(1, 11))))


# reduce function
# to use, needs to import functools lib
# import functools
# nums = [1,2,3,4]
# a = functools.reduce(lambda x,y: x+y, nums)
# # performs sum of elements
# print(a)

# import functools
# l = [2,5,7,12,34,56,22,43]
# out = functools.reduce(lambda x, y: x if x < y else y, l)
# print(out)


# import functools
# l = [1, 3, 2, 4]
# # out = functools.reduce(lambda x, y: x - y, l)
# # print(out) #-8

# out = functools.reduce(lambda x, y: x - y, l, 100)
# # 1st iteration: x=100, y=1 => x=99, y=2 => x=97, y=3 => x=94, y=4 => out=90
# print(out) #90