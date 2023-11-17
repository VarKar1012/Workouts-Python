keys = ['name', 'age']
values = ['devin', 27]

out = dict(zip(keys, values))
out = {keys[i]:values[i] for i in range(len(keys))}
print(out)