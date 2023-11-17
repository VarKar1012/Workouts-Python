import csv

with open('AAPL.csv') as file:
    rFile = csv.reader(file)

    with open('newAAPL.csv', 'w') as f:

        # to write line by line
        # wFile = csv.writer(f, delimiter='#')
        # for line in rFile:
        #     wFile.writerow(line)

        rows = []
        for line in rFile:
            rows.append(line)

        wFile = csv.writer(f)
        wFile.writerows(rows)