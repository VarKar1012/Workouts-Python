values = [[1,2,3], [4,5,6], ['a', 'b']]
# expected: [1, 4, 'a']

out = [i[0] for i in values]
print(out)