# import extractData as content

# f1 = open('words1.txt', 'w+')
# f2 = open('words2.txt', 'w+')

# f1.write(content.data1)
# f2.write(content.data2)
    
# f1.seek(0)
# f2.seek(0)

# print([f1.read(), f2.read()])

# f1.close()
# f2.close()

import glob

files = glob.glob('words*[0-9].txt')
list = []

for file in files:
    with open(file, 'r') as f:
        list.append(f.read())

print(list)