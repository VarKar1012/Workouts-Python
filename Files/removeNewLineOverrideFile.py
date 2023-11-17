# f = open('remove_newline.txt', 'r+')
# new_line = ''

# lines = f.readlines()
# new_line = ' '.join([line.rstrip('\n') for line in lines])

# f.seek(0)
# f.write(new_line)
# f.close()

f = open('remove_newline.txt', 'r')

lines = f.readlines()
new_line = ' '.join([line.rstrip('\n') for line in lines])

f.close()

f = open('remove_newline.txt', 'w')
f.write(new_line)
f.close()