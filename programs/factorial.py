# def findFactorial(num):
#     fact = 1
#     if num == 0:
#         return fact
#     elif num < 0:
#         return "Can't find factorial of -ve numbers"
    
#     for i in range(1, num+1): # range(num, 0, -1)
#         fact *= i
#     return fact

# num = int(input("Please enter a number: "))
# fact = findFactorial(num)
# print(fact)

# def findFactorial(num, fact):
#     if num > 0:
#         return findFactorial(num-1, fact*num)
#     elif num == 0:
#         return fact
#     elif num < 0:
#         return "Can't find factorial of -ve numbers"

# num = int(input("Please enter a number: "))
# fact = 1
# output = findFactorial(num, fact)
# print(output)

# def findFactorial(num):
#     if num > 0:
#         return findFactorial(num-1, fact*num)
#     elif num == 0:
#         return fact
#     elif num < 0:
#         return "Can't find factorial of -ve numbers"

# num = int(input("Please enter a number: "))
# fact = 1
# output = findFactorial(num, fact)
# print(output) 

def findFactorial(num):
    fact = 1
    if num > 0:
        return num*findFactorial(num-1)
    elif num == 0:
        return fact
    elif num < 0:
        return "Can't find factorial of -ve numbers"

num = int(input("Please enter a number: "))
output = findFactorial(num)
print(output)