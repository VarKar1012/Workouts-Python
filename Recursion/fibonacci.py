def findFibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return findFibonacci(num-1) + findFibonacci(num-2)

count = int(input("Enter the count of Fibonacci numbers to be shown: "))
for i in range(count):
    print(findFibonacci(i))