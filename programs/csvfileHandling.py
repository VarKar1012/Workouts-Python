import csv

# print(dir(csv))
# with open('dataone.csv', 'r') as csvFile:
#     csvFile_reader = csv.reader(csvFile)
#     print(csvFile_reader)

#     for i in csvFile_reader:
#         print(i)
# ---------------------------------------
# with open('dataone.csv', 'r') as csvFile:
#     csv_reader = csv.reader(csvFile)

#     with open('data2.csv', 'w') as file:
#         csv_writer = csv.writer(file, delimiter='-') 
#         # changes the content from comma separated to - separated
#         # print(csv_writer) #<_csv.writer object at 0x0000022A4D807280>

#         for line in csv_reader:
#             csv_writer.writerow(line)
# ---------------------------------------
#  can use DictReader to get the content in dict format.

# with open('dataone.csv') as file: #must be a original csv file
#     file_reader = csv.DictReader(file)
#     print(file_reader)

#     for i in file_reader:
#         # print(i)

#         print(i['fname']) #to get each content

# ---------------------------------------
# to write to a new csv file with already existing fieldnames

# with open('dataone.csv') as file: #must be a original csv file
#     csv_reader = csv.DictReader(file)
    # print(csv_reader.dialect) #excel
    # for i in csv_reader:
    #     print(csv_reader.line_num)

    # with open('newFile.csv', 'w') as f:
        # ---------------------
        # header = ['fname', 'lname', 'email']
        # # specify the header.
        # # set the fieldnames in csv.DictWriter()
        # # call csv_writer.writeheader()
        # csv_writer = csv.DictWriter(f, fieldnames=header)
        # csv_writer.writeheader()
        # ---------------------
        # csv_writer = csv.DictWriter(f, fieldnames=csv_reader.fieldnames)
        # csv_writer.writeheader()
        # # csv_writer.

        # for i in csv_reader:
        #     csv_writer.writerow(i)
# ---------------------------------------
# to write to a new csv file with new fieldnames
# 1. write new field names to new csv file.
# 2. open new file in 'a' mode
# 3. assign dict_writer to a var
# 3. do not call writeheader()
# 4. write the content using writerow() in loop

# with open('data3.csv', 'w') as file: #must be a original csv file
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['first','last','email'])

# with open('dataone.csv') as file: #must be a original csv file
#     csv_reader = csv.DictReader(file)
#     with open('data3.csv', 'a') as f:
#         csv_writer = csv.DictWriter(f, fieldnames=csv_reader.fieldnames)
#         for line in csv_reader:
#             csv_writer.writerow(line)
# ---------------------------------------

with open('dataone.csv') as file:
    csv_reader = csv.DictReader(file)
    with open('data4.csv', 'w') as f:
        csv_writer = csv.DictWriter(f, fieldnames=csv_reader.fieldnames[:2])
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)