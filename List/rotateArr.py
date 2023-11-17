# Rotate array to the left by one element.

def rotateArr(arr, n):
    firstElem = arr[0]
    for i in range(0, n-1):
        arr[i] = arr[i+1]
    arr[-1] = firstElem


# driver code
arr = [1, 3, 4, 6, 7, 8]
n = len(arr)
rotateArr(arr, n)
print(arr)