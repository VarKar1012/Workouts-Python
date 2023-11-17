# find GCD of given numbers.

def calcGCD(num1, num2, mini):
    if num1 % mini == 0 and num2 % mini == 0:
        return mini
    else:
        return calcGCD(num1, num2, mini-1)

num1 = 12
num2 = 14
mini = min(num1, num2)
gcd = calcGCD(num1, num2, mini)
print(gcd)