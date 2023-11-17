import string

alphabets = string.ascii_lowercase
alphList = [alphabets[i:i+3] for i in range(0, 26, 3)]

file = open('alphabets.txt', 'w+')
for i in alphList:
    file.write(i+'\n')

file.seek(0)
for line in file:
    print(line)
