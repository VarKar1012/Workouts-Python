# list of strings to list of lists

l = ['abc', 'red', 'black']

# out = list(map(lambda x: list(x), l))
out = list(map(list, l))

print(out)