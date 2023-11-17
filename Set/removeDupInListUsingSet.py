# Write a Python program to remove all duplicates from a given list of strings
# and return a list of unique strings. Use the Python set data type.

def removeDuplicates(var):
    return list(set(l))

l = ['abc', 'varna', 'abc', 'eat', 'play', 'eat']

b = removeDuplicates(l)
print(b)