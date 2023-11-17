
l = ['red', 'green', 'red']
# l = ['red', 'green', 'oran']
# l = [1, 3, 4, 5, 4, 3, 1]

if l == l[::-1]:
    print("list is palindrome")
else:
    print("list is not a palindrome")

# isPal = lambda x, y: x == y
# palFlag = True
# for i in range(len(l)//2):
#     if not isPal(l[i], l[-(i+1)]):
#         print("list is not a palindrome")
#         palFlag = False
#         break

# if palFlag: print("list is palindrome")

# isPal = True
# for i in range(len(l)/2):
#     if l[i] != l[-(i+1)]:
#         isPal = False
#         print("list is not a palindrome")
#         break

# if isPal: print("list is palindrome")