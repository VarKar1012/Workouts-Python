import csv

dict_data = {'id':['1', '2', '3'],
    'Column1':[33, 25, 56],
    'Column2':[35, 30, 30],
    'Column3':[21, 40, 55],
    'Column4':[71, 25, 55],
    'Column5':[10, 10, 40], }

with open('dictData.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=dict_data.keys())
    writer.writeheader()
    writer.writerow(dict_data)
    
with open('dictData.csv') as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line)