import string

path = 'D:\Python\Workouts\Files\AtoZ\\'

for alphabet in string.ascii_uppercase:
    with open(path + alphabet + '.txt', 'w') as file:
        file.write(alphabet)

