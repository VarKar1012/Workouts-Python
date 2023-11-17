s = input("Enter a word: ")
check = lambda x, y: "found" if y.startswith(x) else "not found"

search = input("Enter the starting character to be checked: ")
print(check(search, s))