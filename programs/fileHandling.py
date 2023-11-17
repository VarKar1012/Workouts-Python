# 1. open the file
# 2. Perform operations
# 3. close the file

# x - to create a file
# r - to read
# w - to write
# a - to append
# b - to read an img file

# open('sample.txt', 'x') #creates the file in teh current working folder

# file = open('sample.txt', 'w')
# file.write("Welcome to the world\n") # if newline didnt used, lines will be in single line
# file.write("its me varna")
# print(file.name)
# file.close()

file = open('sample.txt', 'r')

# lines = file.read()
# print(lines)
# out:
# Welcome to the world
# its me varna

# lines = file.readlines() #['Welcome to the world\n', 'its me varna']
# print(lines)

# print(file.tell()) #0 #tells where  the file handler is
# line = file.readline()
# print(line) #Welcome to the world
# print(file.tell()) #22
# line = file.readline()
# print(line) #its me varna

# line = file.readline(6) #Welcom
# print(line)
# line = file.readline() #e to the world
# print(line)

# f.seek(i) - to change file handle to diff pos.
# print(file.tell()) #0
# line = file.readline()
# print(line) #Welcome to the world
# file.seek(5)
# print(file.tell()) #5
# line = file.readline()
# print(line) #me to the world

# file.close()

# to create a non-existant file and write it
# f = open('test.txt', 'w')
# f.write('file testing')
# # f.writelines(['hi', 'hey']) # to write multiple lines
# f.close()
# -----------------------------
# append mode

# f = open('sample.txt', 'a')
# f.write('\nappend file testing')
# f.close()
# -----------------------------
# with stmt - not a loop

# with open('sample.txt') as f:
#     print(f.read())
# -----------------------------
# to remove/delete a file
# import os

# # print(dir(os))
# os.remove('sample.txt')
# -----------------------------
# with open('Screenshot.png', 'br') as f:
#     print(f.read())






