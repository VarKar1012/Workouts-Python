def findLargestNumber(l):
    max = l[0]
    for i in range(1, len(l)):
        if max < l[i]:
            max = l[i]
    print("Largest number is:", max, "& its index is:", l.index(max))

l = [3,8,1,7,2,9,5,4]
# l = [45, 32,5,46,7,8]
findLargestNumber(l)
# print(max(l))