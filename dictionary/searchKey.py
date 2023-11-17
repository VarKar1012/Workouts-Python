# Search a key


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key = int(input("key to be searched: "))

if key not in d:
    print("key not found")
else:
    print("key is found")

# l = [i for i in d.keys() if i == key]
# if not l:
#     print("key not found")
# else:
#     print("key is found")

