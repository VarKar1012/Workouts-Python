# linear search

def numberSubscript(num):
    if num == 0 or num > 3:
        return 'th'
    elif num == 1:
        return 'st'
    elif num == 2:
        return 'nd'
    elif num == 3:
        return 'rd'
    
numbers = [4,2,7,1,8,3,6]
target = int(input("Please enter the number to be searched: "))
# if target in numbers:
#     print("Number is found and is at position:", numbers.index(target))
# else:
#     print("Searched number could not be found.")
    
found = 0
for i in range(len(numbers)):
    if numbers[i] == target:
        found = True
        print(f"Number is found and is at {i}{numberSubscript(i)} index")
        break
        
if not found:
    print("Searched number could not be found.")
