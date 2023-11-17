def binary_search(arr, key):
    start = 0
    end = len(arr)

    while start < end:
        mid = (end + start) // 2
        
        if key == arr[mid]:
            print(key,"is found in the list.")
            return
        
        else:
            if (key < arr[mid]):
                end = mid - 1
            else:
                start = mid + 1
    
    # when start < end fails
    print(key,"could not be found in the list.")

l = [34, 4, 23, 2, 45, 6, 76, 88, 1213, 233]
key = int(input("Enter the number to be searched: "))

l.sort()
print(l)
binary_search(l, key)
