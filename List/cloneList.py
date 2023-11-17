# clone.copy a list

var = [3, 45, 3, 56, 77, 36]
a = var # same address as var
b = list(var) # diff memory location than var
print(a, b)
print(id(var))
print(id(a), id(b))

