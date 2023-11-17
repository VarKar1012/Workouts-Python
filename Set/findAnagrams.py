# Write a Python program to find all the anagrams in a given list of strings and then group them together.
# Use the Python data type.

# Original list of strings:
# ['eat', 'cba', 'tae', 'abc', 'xyz']
# Find and group all anagrams in the said list:
# [['eat', 'tae'], ['cba', 'abc'], ['xyz']]

# input = ['restful', 'forty five', 'evil', 'over fifty', 'vile', 'fluster']
# [('restful', 'fluster'), ('forty five', 'over fifty'), ('evil', 'vile')]

def findAnagrams(srcList):
    anagrms = []

    for i in range(len(srcList)):
        for j in range(i+1, len(srcList)):
            if sorted(srcList[i]) == sorted(srcList[j]):
                anagrms.append((srcList[i], srcList[j]))
    return anagrms

# l =  ['eat', 'cba', 'tae', 'abc', 'xyz']
l = ['restful', 'forty five', 'evil', 'over fifty', 'vile', 'fluster']
anagrams = findAnagrams(l)
print(anagrams)