# def function_name(parameter1, param2):
#     print("inside function called function_name")

# function_name(argument1, arg2)

# Positional arg passing:
# def call(a, b):
#     print(a+b)
# call(2,4)

# Setting default values to fn parameter
# def call(a=1, b=1):
#     print(a+b)
# call() #2
# call(2,3) #5

# keyword argument passing:
# def call(a, b):
#     print(a+b)

# call(b=23,a=45)

# arbitrary argument passing: other params should be declared before arb argument.
# def call(*a):
#     print(a)

# call(1,2,3,4,5)

# def call(val, *a): # val=1, *a=(2,3,4,5)
#     print(val)
#     print(a)

# call(1,2,3,4,5)

# def call(val=2, *a): # val=1, *a=(2,3,4,5)
#     print(val)
#     print(a)

# call(1,2,3,4,5)

# keyword arbitrary arg passing: for dictionary types
# def call(**a): #a={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#     print(a)

# call(a=1,b=2,c=3,d=4,e=5)

# def call(val, **a): #a={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#     print(val)
#     print(a)
# call(23, a=1,b=2,c=3,d=4,e=5)

# def call(val=1, **a): #val=23, a={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#     print(val)
#     print(a)
# call(23, a=1,b=2,c=3,d=4,e=5)



