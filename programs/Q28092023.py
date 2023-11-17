def findSum(l):
    sum = 0
    for i in l:
        if type(i) == list: #can use type([]) also
            sum += findSum(i)
        else:
            sum += i
    return sum

l = [2,3, [4,5], 5, [6,7]]

sum = findSum(l)
print("Sum is:", sum)