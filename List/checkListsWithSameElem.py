# Write a Python function that takes two lists and
# returns True if they have at least one common member.

def checkCommonMember(list1, list2):
    for elem in list1:
        for mem in list2:
            if elem == mem:
                return True

list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
result = checkCommonMember(list1, list2)
print(result)