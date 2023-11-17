# Rotate d elements of a list.

def rotateElemByRange(arr, start, end):
    # select the sub array to be rotated to the end.
    temp = arr[start:end]
    subarr = arr[2:]
    # arr = [subarr, temp] => [[2 8 4] [3 6]]
    arr = subarr + temp


# driver code
arr = [3, 6, 2, 8, 4]
# expected: 2, 8, 4, 3, 6
rotateElemByRange(arr, 0, 2)
print(arr)