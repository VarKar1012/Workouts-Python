# ['x', 'xx', 'xxx', 'xxxx']

print(['x'*i for i in range(1, 5)])
print(list(map(lambda x: 'x'*x, range(1, 5))))