str = "a citizen of ekm fought and won the election"
stop_words = ['in', 'of', 'a', 'and', 'the']

# expected: 'citizen ekm fought won election'

# temp = str
# for i in stop_words:
#     temp = ''.join(temp.split(i, maxsplit=1))
# print(temp)

temp = str.split()
out = ' '.join(filter(lambda x: x not in stop_words, temp))
print(out)