# create a dictionary containing 1 to 5 as key and their squares as values.

d = {}
for i in range(1, 6):
    d.setdefault(i, i**2)

print(d)