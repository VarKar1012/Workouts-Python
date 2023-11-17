def cubes(num):
    for i in range(1, num+1):
        yield i**3

limit = int(input("Enter a number: "))
out = cubes(limit)

for i in out:
    print(i)