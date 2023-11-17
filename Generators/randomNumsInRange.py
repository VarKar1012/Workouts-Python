import random

def generateRandomNumbers(start, end):
    for i in range(0, 10):
        yield random.randint(start, end)


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
nums = generateRandomNumbers(start, end)
for i in nums:
    print(i)
