# Sort list of tuples in ascending order by the increasing order of last elem in the tuple.

l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# print(l.sort())

tempList = []
# index = 0
index = len(l)

print("before sorting", l)

# by using sorted function
# syntax: sorted(iterable_var, [key=], [reverse=])
# iterable_var = list, tuple, string, set, dict
def last(n): return n[-1]
l = sorted(l, key=last)

# def sort_list_last(tuples):
#   return sorted(tuples, key=last)

# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# for elem in l:
#     j = 0
#     while j < len(l)-1:
#         if l[j][-1] > l[j+1][-1]:
#             l[j], l[j+1] = l[j+1], l[j]
#         j += 1

# while(index > 0):
#     j = 0
#     while(j <= index-j+1):
#         if l[j][-1] > l[j+1][-1]:
#             l[j], l[j+1] = l[j+1], l[j]
#         j += 1
#     index -= 1

print("after sorting: ", l)


