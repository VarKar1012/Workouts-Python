# Find largest element in an array

def findLargest(arr):
    max = arr[0]

    for i in arr:
        if max < i:
            max = i
    return max

# driver code
arr = [1, 34, 54, 78, 55, 60]
# max = findLargest(arr)
max = max(arr)
print(max)

# arr = [1, 34, 54, 78, 55, 60]

# max = arr[0]

# for i in arr:
#     if max < i:
#         max = i
# print(max)