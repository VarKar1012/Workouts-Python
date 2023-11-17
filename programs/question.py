# get upper case and lower case letters from a sentence

str = input("Please enter a sentence: ")

upper = 0
lower = 0

for each in str:
    if each.isupper():
        upper += 1
    elif each.islower():
        lower += 1
    
print("Number of lower case letters are:", lower)
print("Number of upper case letters are:", upper)