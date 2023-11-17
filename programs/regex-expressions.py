import re

text = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa Has 
MetaCharacters (need to be escaped):
. ^ $ * + ? { } [ ] \ / ( )
coreyms.com
321--555--4321
123.555.1234
123*555*1234
900--555--1234
Mr. Schafer
Mr Smith
ms Davis
Mrs. Robinson
Mr. T'''

# com = re.compile(r'abc')
# # print(com) #re.compile('abc')

# matches = com.finditer(text)
# for each in matches:
#     print(each) 
#<re.Match object; span=(1, 4), match='abc'>

# print(com.match(r'abc')) #err
# <re.Match object; span=(0, 3), match='abc'>

# com = re.compile(r'abcA')
# matches = com.finditer(text)
# for each in matches:
#     print(each) # if no match found, returns Nothing (but no err)

# matches = re.finditer(r'abc', text)
# for each in matches:
#     print(each)
# --------------------------------------
# com = re.compile(r'.') #gets all chars
# com = re.compile(r'\.') #gets '.' char
# com = re.compile(r'\d') #gets all digits
# com = re.compile(r'\D') #gets all chars except digits
# com = re.compile(r'\w') #gets all chars of alphabet + digits
# com = re.compile(r'\W') #gets all chars except alphabet + digits
# com = re.compile(r'\s') #gets ' ', \t, \n
# com = re.compile(r'\S') #gets all chars except ' ', \t, \n
# com = re.compile(r'\bHa') # gets all words starting with 'Ha' that are separated by space
# <re.Match object; span=(66, 68), match='Ha'>
# <re.Match object; span=(69, 71), match='Ha'>
# <re.Match object; span=(74, 76), match='Ha'>
# com = re.compile(r'\BHa') # gets all words with 'Ha' that are not at starting pos
# <re.Match object; span=(71, 73), match='Ha'>

# matches = com.finditer(text)
# for each in matches:
#     print(each) 

# sent = 'Sentence starting with a regex'
# com = re.compile(r'^Sen') #<re.Match object; span=(0, 3), match='Sen'>
# com = re.compile(r'ex$') #<re.Match object; span=(28, 30), match='ex'>
# com = re.compile(r'reg$') #None

# matches = com.finditer(sent)
# for each in matches:
#     print(each) 
# -----------------
# find phone numbers
# <re.Match object; span=(156, 168), match='321-555-4321'>
# <re.Match object; span=(169, 181), match='123.555.1234'>
# <re.Match object; span=(182, 194), match='123*555*1234'>
# <re.Match object; span=(195, 207), match='900-555-1234'>

# num = re.compile(r'\d\d\d\W\d\d\d\W\d\d\d\d')
# for each in num.finditer(text):
#     print(each)

# num = re.compile(r'\d\d\d\.\d\d\d\.\d\d\d\d')
# for each in num.finditer(text):
#     print(each)

# num = re.compile(r'\d{3}.\d{3}.\d{4}')
# for each in num.finditer(text):
#     print(each)
# ------------------------------------------------
# finding the pattern by reading a file

# num = re.compile(r'\d{3}.\d{3}.\d{4}')

# with open('data.txt') as f:
#     cont = f.read()
#     itr = num.finditer(cont)

#     for i in itr:
#         print(i)
# <re.Match object; span=(155, 167), match='321-555-4321'>
# <re.Match object; span=(168, 180), match='123.555.1234'>
# <re.Match object; span=(181, 193), match='123*555*1234'>
# <re.Match object; span=(194, 206), match='900-555-1234'>
# --------------------------------------------------

# num = re.compile(r'\d{3}--\d{3}--\d{4}')
# # num = re.compile(r'\\') #<re.Match object; span=(136, 137), match='\\'>

# for each in num.finditer(text):
#     print(each)

# <re.Match object; span=(156, 170), match='321--555--4321'>
# <re.Match object; span=(197, 211), match='900--555--1234'>

# -------------------------------------------

# a = r'^Mr'
# b = r'th$'
# for each in num.finditer(text):
#     print(each)


