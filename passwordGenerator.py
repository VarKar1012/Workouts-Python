import random

chars = 'abcdefghijklmnopqrstuvwxyz0123456789@#$%^&*!~_ABCDEFGHIJKLMNOPQRSTUVWXYZ'

count = int(input("Enter required number of passwords: "))
letters = int(input("Enter password length needed: "))

# while(count > 0):
#     password = ''.join(random.choices(chars, k=letters))
#     print(password)
#     count -= 1

# for i in range(count):
#     password = ''
#     for j in range(letters):
#         password += random.choice(chars)
#     print(password)