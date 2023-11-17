a = ["apple", "banana"]

# replace banana with grapes
a[1] = "grapes"
print(a)

# orange needs to come between apple and grape
a.insert(1, "orange")
print(a)

# sort and reverse
a.sort()
print(a)
a.reverse()
print(a)

# delete 1st value
del a[0]
print(a)

# add pineapple last
a.append("pineapple")
print(a)

# add ["strawberry", "mango"] to this list
a.extend(["strawberry", "mango"])
print(a)