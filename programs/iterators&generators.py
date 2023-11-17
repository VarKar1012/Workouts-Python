# iterable and iterators
# iterable - list, array etc (something that can be looped over)
# iterator - object with state (saves the state of operation)

# l = [1,2,4,5]
# print(type(l))
# for i in l:
#     print(i)
#1 2 4 5


# l = [1,2,4,5]
# val = iter(l)
# print(type(val))
# for i in val:
#     print(i)
# <class 'list_iterator'>
# 1
# 2
# 4
# 5
# print(next(val)) #1
# print(next(val)) #2
# print(next(val)) #4

# l = [1,2,4,5]
# itr = iter(l)
# while True:
#     try:
#         val = next(itr)
#         print(val)
#     except StopIteration:
#         break
# out
# 1
# 2
# 4
# 5
# ---------------------------------------------
# creating a custom range function using class
# class myrange:
#     def __init__(self, start, end) -> None:
#         self.start = start
#         self.end = end
    
#     def __iter__(self): 
#         return self
    
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#         current = self.start
#         self.start += 1
#         return current

# r = myrange(2, 7)

# for i in r:
#     print(i)
# 2
# 3
# 4
# 5
# 6

# while True:
#     try:
#         print(next(r)) #throws raise StopIteration (48)
#     except StopIteration:
#         break # handles the exeception thrown @48
# ------------------------------------------------------------
# generators - creating generator object using yield keywword

# def myrange(start):
#     current = start

#     while True:
#         yield current #creates a generator object
#         current += 1

# r = myrange(5)
# print(r) #<generator object myrange at 0x00000197859FC380>

# print(next(r)) #5
# print(next(r)) #6
# print(next(r)) #7
# print(next(r)) #8


# --------------------------------------------------
# def words(str1):
#     itr = iter(str1.split())
#     return itr

# r = words('hi, i am varna karthik')
# for i in r:
#     print(i)
# --------------------------------------------------
# class words:
#     def __init__(self, str) -> None:
#         self.val = str.split(' ')

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         s = self.val[0]
#         self.val = self.val[1:]
#         return s

# w = words('hi, i am varna karthik')

# try:
#     for i in w:
#             print(i)
# except:
#     pass

# print(next(w))
# print(next(w))
# print(next(w))
# print(next(w))
# print(next(w))
# ----------------------------------------
# class words:
#     def __init__(self, str) -> None:
#         self.sent = str
#         self.indx = 0
#         self.val = str.split(' ')

#     def __iter__(self): 
#         return self
    
#     def __next__(self):
#         if self.indx >= len(self.val):
#             raise StopIteration
        
#         indx = self.indx
#         self.indx += 1
#         return self.val[indx]

# w = words('hi, i am varna karthik')
# for i in w:
#     print(i)


# print(next(w))
# print(next(w))
# print(next(w))
# print(next(w))
# print(next(w))
# print(next(w))
# ----------------------------------------
def words(str):
    for i in str.split():
        w = yield i 

w = words('hi, i am varna karthik')
# print(next(w))
print(w.next())









