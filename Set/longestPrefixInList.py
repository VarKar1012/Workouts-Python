# Original list of strings:
# ['pqrefgh', 'pqrsfgh']
# Longest common prefix of all said strings:
# pqr

# def checkPrefix(prev, new):
#     for i in range(0, len(new)):
#         if new[i] != prev[i]:
#             return prev[:i]
#     return prev

# def findLongestPrefix(l):
#     s = min([len(i) for i in l])
#     pre = l[0][:s]
#     for i in range(1, len(l)):
#         if pre != l[i][:s]:
#             pre = checkPrefix(pre, l[i][:s])
#             s = len(pre)

#     return pre

def findLongestPrefix(l):
    mini = min([len(i) for i in l])
    for i in range(mini):
        chars = set(j[i] for j in l)
        if len(chars) > 1:
            return l[0][:i]
    
    return l[0][:mini]


l = ['pqrefgh', 'pqrsfgh']
# l = ["w3r","w3resource"]
# l = ["Python","PHP", "Perl"]
output = findLongestPrefix(l)
print(output)