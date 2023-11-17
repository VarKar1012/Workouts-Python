# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

str = 'google.com'
d = {}
for i, j in enumerate(str):
    if j not in d.values():
        count = str.count(j)
        d[j] = count

print(d)