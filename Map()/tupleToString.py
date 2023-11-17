# convert list of tuples to list of strings
# Original list of tuples:
# [('red', 'pink'), ('white', 'black'), ('orange', 'green')]

# Convert the said list of tuples to a list of strings:
# ['red pink', 'white black', 'orange green']

l = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print(list(map(lambda x: ' '.join(x), l)))