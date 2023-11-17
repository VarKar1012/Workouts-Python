# string is an ordered list with each character in an index.

str = "new string"
# 0th index starts from left and -1th index starts from right side.
 
# print(str.upper())
# print(str.lower())
# up = str.upper()
# lo = str.lower()

####To check if the string is lower case / upper case
# print(up.islower())
# print(up.isupper())
# print(lo.islower())

# print(str.capitalize()) #New string
# print(str.title()) #New String

# print(str.count(""))
# print(len(str))

# print(str.index('n'))
# print(str.index('n', 1))
# print(str.index('n', 1, -1))
# print(str.index('n', 1, 2)) # returns value error

# print(str.find('n'))
# print(str.find('n', 1))
# print(str.find('n', 1, -1))
# print(str.find('n', 1, 2)) # returns -1

# str1 = "strx efdg"
# print(str1.split('x'))

# str = "new member is a geek"
# sub = str.split('m')

# print(sub)
# print(''.join(sub))
# print(' '.join(sub))
# print('m'.join(sub))
 
# print(str.isalpha())
# new = "wefdfsf"
# print(new.isalpha())
# new = "wefdfsf234"
# print(new.isalpha())

# str = "new member is a geek"
# print(str.replace('m', 'X', 3))

# str = "123X"
# print(str.isnumeric()) #supports digits, vulgar frctions, subscripts/superscripts, roman numberals
# print(str.isdecimal()) # decimal
# print(str.isdigit()) #supports decimals, subscripts/superscripts

# a = '23434'
# a = '8\u00B2'
# a = '¼'
# print(a.isnumeric())
# print(a.isdecimal())
# print(a.isdigit())

# new = "name is abby"
# print(new.startswith("name"))
# print(new.endswith("name"))
# print(new.endswith("abby"))

# new = "     name is abby  "
# print(new)
# # print(new.strip())
# print(new.lstrip())
# print(new.rstrip())

# new = "sdfs as tiny bad"
# print(new[5:7]) # as
# print(new[-11:-9]) # as
# print(new[0:-10]) # sdfs a
# print(new[5::4]) # aib
# print(new[:10:3]) # sssi
# print(new[:10:3]) # sssi
# print(new[:10:3]) # sssi
# print(new[0:-10:2]) #sf 
# print(new[::-1]) # to reverse a string

# to reverse a string, index should begin in the reverse order.
# print(new[11:7:-1]) # to reverse 'tiny'
# print(new[-5:-9:-1]) # to reverse 'tiny'
# print(new[3::-1]) # to reverse 'sdfs'
# print(new[-13::-1]) # to reverse 'sdfs'
# print(new[:-4:-1]) # to reverse 'bad'

# concatenation
# str1 + str2
# a = "abs"
# b = "stabs"
# print(a+b)
# can multiply strings with integers but not itself
# a *2 allowed  but not a*a

# var1 = "it's a sunday"
# var2 = "have a great day"
# # expected:
# # it's a great day
# # great sunday
# print(var1[:4]+ var2[4:])
# print(var2[7:12]+ var1[-7:]) # var2[7:-3]+var1[7:]

# str = 'heLLO, Welcome'
# print(str.swapcase()) # inverts the case of the letter used

# str = "ban#orang#apple"
# # x = str.split(sep='#', maxsplit= 1)
# x = str.split('#', 1)
# print(x)

# str = "I love apples and apple is my favourite fruit."
# print(str.count('apple', 5, 25))





