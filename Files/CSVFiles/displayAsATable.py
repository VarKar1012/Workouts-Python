import csv

rows = []

with open('AAPL.csv') as file:
    rFile = csv.reader(file)
    cont = next(rFile)

    num = 1
    for line in rFile:
        if num > 5: break

        for i in line:
            print('%10s'%i, end=' ')

        print('\n')
        num += 1