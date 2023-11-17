#  add a key to dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

d = {0: 10, 1: 20}

d.setdefault(2, 30)

# d[2] = 30

# d.update([[2, 30]])

# d.update({2:30})

print(d)