def findSum(userList):
    sum = 0
    for elem in userList:
        sum += elem
    return sum

# driver code
limit = int(input("Please enter the limit: "))

print("Enter the numbers: ")
l = [int(input("")) for i in range(limit)]

sum = findSum(l)
print(f"Sum of {limit} numbers are:", sum)

avg = sum / limit
print("The average is:", avg)