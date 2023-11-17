
def findPrimeNum(num):
    isPrime = True
    if num == 1 or num == 2:
        print(f"{num} is a prime number")
    else:
        for i in range(2, num):
            if num%i == 0:
                print(f"{num} is not a prime number")
                isPrime = False
                break
            else:
                continue
        if isPrime == True:
            print(f"{num} is a prime number")

findPrimeNum(14)
        
        
