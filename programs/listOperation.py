# list operations
# -ve and +ve indexing is allowed

# l = []
# print(type(l))

# l = ['cat', 'dog', 'monkey', True, False, 2, 5.3]
# print(l)
# print(l[2]) 
# print(l[-5])

# nested list
# l = [[10,20],[30,40]]
# print(l[1][1])

# list operations

# l1 = [1,2,3,4,5]
# # # replace
# l1[1] = 50 #changes value at the index
# print(l1)
# # insert
# l1.insert(1, "hi") #[1, 'hi', 50, 3, 4, 5]
# print(l1)

# l = [40, 40, [10, 20], [45, 'hello']]
# # add 65 in b/w 10 & 20
# # a = l[2]
# # a.insert(1, 65)
# # l[2] = a
# l[2].insert(1, 65)
# print(l)

# animal =['monkey', 'dog', 'cat', 'lion']
# animal.sort()
# print(animal)

# l=[[35,75] ,[35,25]]
# l.sort()
# print(l)

# delete
# l=[5,4,"dog",3,2,1]
# print(l) 
# del l[1]
# print(l)
# l.pop(2)
# print(l)

# append
# l=[5,4,"dog",3,2,1]
# l.append(34.4)
# print(l)

# To reverse sort
# l=[5,4, 34, 3,2,1]
# l.sort(reverse=True) #[34, 5, 4, 3, 2, 1] sorted and reversed
# print(l)
# l=[5,4, 34, 3,2,1]
# l.reverse() #[1, 2, 3, 34, 4, 5] only reversed
# print(l)
# l = ['apple', 'banana', 'Apple', 'Food', 'food', '#', '1']
# above list is sorted based on ASCII value of starting char.
# l.sort() #['#', '1', 'Apple', 'Food', 'apple', 'banana', 'food']
# l.sort(reverse=True) #['food', 'banana', 'apple', 'Food', 'Apple', '1', '#']
# l.sort(key=len) #['#', '1', 'Food', 'food', 'apple', 'Apple', 'banana'] - confusing result?
# print(l)

# extend
# l=['zebra','monkey']
# l1=['fox','tiger']
# l.extend(l1) 
# l1.extend(l)
# print(l)
# print(l1)

# l = ['apple', 'banana', 'Apple', 'Food', 'food']
# a = l
# print(l, a)
# a.append("orange") # change in a changes l also.
# print(l, a)

# b = l.copy()
# print(l, b)
# b.append("pineapple")
# print(l, b)

# l = ['apple', 'banana', 'banana', 'Apple', 'Food', 'food']
# print(l.count('banana')) #2


