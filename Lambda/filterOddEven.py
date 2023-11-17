# Write a Python program to filter a list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

# def checkNum(num):
#     check = lambda num: num % 2
#     if check() == 0:
#         return lambda num:
    
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# check = lambda num: num % 2
# even = []
# odd = []
# for i in l:
#     if check(i) == False:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even numbers:", even)
# print("Odd numbers:", odd)

even = list(filter(lambda x: x%2 == 0, l))
odd = list(filter(lambda x: x%2 != 0, l))
print("Even numbers:", even)
print("Odd numbers:", odd)
