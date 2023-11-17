num = int(input("Enter a number: "))

def reverse(num, r):
    if num == 0:
        return r
    else:
        return reverse(num//10, (num % 10) + r*10)

r = 0  
out = reverse(num, r)
print(out)
     