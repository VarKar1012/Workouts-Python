# Given a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
# Input:
# [19, 19, 15, 5, 5, 5, 1, 2]
# Output:
# True

def checkFifthElem(l):
    return (len(l) == 8) and (l.count(l[4]) == 3)

l = [19, 19, 15, 5, 5, 5, 1, 2]
l = [19, 15, 5, 7, 5, 5, 2]
l = [11, 12, 14, 13, 14, 13, 15, 14]
res = checkFifthElem(l)
print(res)