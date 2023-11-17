# using send function of generator

def findAverage():
    total = 0
    count = 0
    while True:
        avg = yield (total / count) if count > 0 else 0
        total += avg
        count += 1

print("enter starting number: (type \'n\' to stop running)\n")

avg = findAverage()
next(avg)

while True:
    inp = input('> ')
    if inp == 'n':
        break
    
    num = int(inp)
    average = avg.send(num)
    print("avg is:", average)
