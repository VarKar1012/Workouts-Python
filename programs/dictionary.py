a = {1:2, 3:4, 3:5, 'a': 45, 1:5}
# print(a)
# print(a[3])
# print(a[45]) # returns key error

# print(a.get('a'))
# print(a.get('b')) # returns None
# print(a.get('b', 'key not found')) # displays err msg passed as argument

# key = ['devin', 'dainty', 'david']
# values = ['python', 'cyber', 'analyst', 'security']

# data = dict(zip(key, values)) # {'devin': 'python', 'dainty': 'cyber', 'david': 'analyst'}
# print(data)
# data = set(zip(key, values)) #{('david', 'analyst'), ('devin', 'python'), ('dainty', 'cyber')}
# print(data)
# data = list(zip(key, values)) #[('devin', 'python'), ('dainty', 'cyber'), ('david', 'analyst')]
# print(data)
# data = tuple(zip(key, values)) #(('devin', 'python'), ('dainty', 'cyber'), ('david', 'analyst'))
# print(data)

# print(dict( [[1,2], [3,4]] )) #{1: 2, 3: 4}
# print(dict( ((1,2), (3,4)) )) #{1: 2, 3: 4}
# a = {1:2, 2:[34, 435, 64]}
# print(a[2][1]) #435

# dict  = { 1:{ 1:{2:'b', 3:'c'}, 2:{4:'d', 5:'e'} } }
# print(dict[1][1][3]) # output- 3

# Insert values to dict
# val = {}
# print(val)
# val = dict()
# print(val)
# print(type(val))

# val = {2}
# print(type(val))

# val = {}
# val.setdefault('a')
# print(val)
# val.setdefault(1, 2)
# print(val)

# val[2] = 'absolute'
# print(val)

# appends 1 dict to another dict
# val = {0:243, 34: 34}

# a = {1: 45}
# val.update(a) #{0: 243, 34: 34, 1: 45}

# a = [[3, 67], [4, 23]]
# val.update(a) #{0: 243, 34: 34, 3: 67, 4: 23}

# val.update(abs=100, e=879) #{0: 243, 34: 34, 'abs': 100, 'e': 879}
# # In this case, LHS of assignment should be a variable name not numerals
# print(val)

# To remove items in dict
# val = {0:243, 34: 34, 2:3}
# val.pop(0) #{34: 34, 2: 3}
# print(val)

# val = {0:243, 34: 34, 2:3}
# val.popitem() #{0: 243, 34: 34}
# print(val)

# val = {0:243, 34: 34, 2:3}
# val.clear() #{}
# print(val)

# val = {0:243, 34: 34, 2:3}
# del val[0] #{34: 34, 2: 3}
# print(val)

# Iterate over a dict
# a = {1:2, 3:4, 5:6, 7:8}
# for i in a: # iterates over key not value
#     print(i, ":", a[i])

# for i in a.items(): # iterates as (key,value) tuple
#     print(i)
# (1, 2)
# (3, 4)
# (5, 6)
# (7, 8)

# for i,j in a.items(): # iterates over key and values
#     print(i, j)
# 1 2
# 3 4
# 5 6
# 7 8

# for i in a.keys(): # iterates over keys
#     print(i)
    
# for i in a.values(): # iterates over values
#     print(i)








