# Write a Python program to print the numbers of a specified list after removing even numbers from it.

var = [34, 52, 55, 2, 5 , 7, 9, 33]

result = [i for i in var if i%2 != 0]
print(result)
# for i in var:
#     if(i%2 != 0):
#         print(i)