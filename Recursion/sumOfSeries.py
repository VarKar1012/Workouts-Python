# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... 
# (until n-x =< 0).

def sumOfSeries(num):
    if num <= 0:
        return 0
    else:
        return num + sumOfSeries(num-2)

num = int(input("Enter the maximum number in your series: "))
sum = sumOfSeries(num)
print(sum)