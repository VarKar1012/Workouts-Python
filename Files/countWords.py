words_count = 0

with open('count_words.txt', 'r') as file:
    line = file.readline()

    comma_removed = line.replace(',', ' ')
    words_count += comma_removed.count(' ') + 1

print(words_count)