# Count number of elems with same starting and ending character.

l = ["abc", 'xyz', 'aba', '23', '121']

count = 0
for i in l:
    if 1 < len(i) and i[0] == i[-1]:
        count += 1

print("Number of elems with same start and end characters is: ", count)