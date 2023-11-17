# sort a dictionary values in ascending and descending order.

import operator

d = {1:2, 4: 65, 3:1, 5:10}

dictAsc = {}
dictDesc = {}

asc = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(asc)

desc = sorted(d.items(), key=operator.itemgetter(1), reverse=True) # sorted returns a list.
print(desc)
