# Remove duplicates in the list.

var = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

temp = []
for elem in var:
    if elem not in temp:
        temp.append(elem)

print(temp)