# Write a Python program to create a function that takes one argument, 
# and that argument will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75

def multiply(n):
    opr = lambda num: n * num
    return opr

num = 15

double = multiply(2)
print("Double the number of 15 =", double(num))

triple = multiply(3)
print("Triple the number of 15 =", triple(num))

quad = multiply(4)
print("Quadruple the number of 15 =", quad(num))

quint = multiply(5)
print("Quintuple the number of 15 =", quint(num))