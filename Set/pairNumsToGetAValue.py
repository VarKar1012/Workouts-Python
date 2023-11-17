# Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers,
# adding up to a target number.
# Original list of numbers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Target value: 12
# Combine three numbers whose sum equal to a target number:
# [(1, 3, 8), (1, 4, 7), (1, 2, 9), (1, 5, 6), (3, 4, 5), (2, 3, 7), (2, 4, 6)]

# def findCombination(l, target):
#     outList = []
#     for i in l:
#         for j in l:
#             s = set()
#             if j == i: continue
#             elif j + i < target:
#                 x = target - (i + j)
#                 if x in l and x not in [i, j]:
#                     s = {i, j, x}
            
#                     if s not in outList:
#                         outList.append(s)

#     return (outList)

def findCombination(l, target):
    outSet = set()
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            complement = target - (l[i] + l[j])
            if complement in l and complement not in [l[i], l[j]]:
                outSet.add(tuple(sorted((l[i], l[j], complement))))

    return (list(outSet))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = int(input("Please enter a target value: "))

output = findCombination(l, target)
print(output)