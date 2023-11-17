# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

# def findElementsAtIndex(var, index):
#     temp = list(var)
#     del temp[index]

var = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
result = list(x for (i,x) in enumerate(var) if i not in (0, 4, 5))
print(result)

'''
size = len(var)

var.pop(0)
var.pop(4-1)
var.pop(5-2)

print(var)
'''
