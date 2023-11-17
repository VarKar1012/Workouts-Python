
a = [1,2,3,4]
b = [1,2,3,4]

# out = [a[i]+b[i] for i in range(len(a))]
out = list(map(lambda x,y: x+y, a, b))
print(out)