
# limit = 4
# for i in range(1, limit+1):
#     temp = ''
#     for j in range(1, i+1):
#         temp += str(j) + " "
#     print(temp)
        

limit = 4
for i in range(1, limit+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()        