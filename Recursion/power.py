# Python program to calculate the value of 'a' to the power of 'b'.

def power(num, pow):
    if pow < 1:
        return 1
    else:
        return num * power(num, pow - 1)

p = power(3, 4)
print(p)