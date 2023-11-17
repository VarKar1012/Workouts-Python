# Write a Python program to find the third largest number
# from a given list of numbers.Use the Python set data type.

def getThirdLargest(l):
    s = set(l)
    sortedList = sorted(s)
    return sortedList[-3]

# l = [1, 56, 34, 67, 243, 67, 64,2,3]
l = [1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 10]
# using set to remove duplicates

num = getThirdLargest(l)
print(num)

