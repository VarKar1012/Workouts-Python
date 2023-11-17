# Sum of digits of non -ve integer

# def findSum(num):
#     if len(num) == 1:
#         return int(num[0])
#     elif not num:
#         return "Did not receive a number." 
#     else:
#         return int(num[0]) + findSum(num[1:])

# num = input("Enter a number: ")
# sum = findSum(num)
# print(sum)

def findSum(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + findSum(int(num / 10))

num = 345
sum = findSum(num)
print(sum)