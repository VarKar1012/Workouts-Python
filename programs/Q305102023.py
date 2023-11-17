mat = [[1, 2], [3, 4], [5, 6], [7, 8]]

# def transpose(mat):
#     l = []
#     indx = 0
#     for j in range(len(mat[0])):
#         temp = []
#         for i in mat:
#             temp.append(i[j])
#         l.append(temp)
#     return l

# out = transpose(mat)
# print(out)

# out = [[i[0] for i in mat], [i[1] for i in mat]]
# print(out)

# out = [[j[i] for j in mat] for i in range(len(mat[0]))]
# print(out)