# input - "devin123"
# o/p - [1,2,3]

str = 'devin123'
output = [int(i) for i in str if i.isdigit()]
print(output)

# out = list(filter(lambda x: x.isdigit(), str))
# print(out)
