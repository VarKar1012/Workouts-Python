names = []

for i in range(5):
    names.append(input("Please enter a name: ")+'\n')

with open('userIn.txt', 'w') as f:
    f.writelines(names)