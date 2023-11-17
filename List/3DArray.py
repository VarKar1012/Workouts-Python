# Write a Python program to generate a 3*4*6 3D array whose each element is *.
# 3*4*6 3D array == a list containing 3 nested lists each containing 4 lists with 6 elems
# [ 
# [[*, *, *, *, *, *], [*, *, *, *, *, *], [*, *, *, *, *, *], [*, *, *, *, *, *]], 
# [[*, *, *, *, *, *], [*, *, *, *, *, *], [*, *, *, *, *, *] ,[*, *, *, *, *, *]], 
# [[*, *, *, *, *, *], [*, *, *, *, *, *], [*, *, *, *, *, *], [*, *, *, *, *, *]]
# ]

row = 3
col = 4
dep = 6

list3D = [[["*" for depth in range(dep)] for column in range(col)] for rows in range(row)]

# list3D = []
# for i in range(row):
#     arr2D = []
#     for x in range(col):
#         val = []
#         for y in range(dep):
#             val.append("*")
#         arr2D.append(val)
#     list3D.append(arr2D)

print(list3D)