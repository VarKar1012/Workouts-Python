# count the digits of a number.

num = 75869
count = 0
# while count < len(str(num)):
#     count += 1

while num != 0:
    count += 1
    num = num // 10


print("count:", count) 