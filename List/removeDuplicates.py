# remove duplicates in a list.

# var = [1, 4, 2, 5, 3, 4, 2, 65, 234, 65]
var = [10,20,30,20,10,50,60,40,80,50,40]

temp = []
for elem in var:
    if elem not in temp:
        temp.append(elem)
    # index = var.index(elem) + 1
    # while index < len(var):
    #     if elem == var[index]:
    #         del var[index]
    #     index += 1

print(temp)