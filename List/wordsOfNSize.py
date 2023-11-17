# To find the list of words that are longer than n from a given list of words.

def findLongWords(str, n):
    words = []
    for word in str:
        if len(word) > n:
            words.append(word)
    return words
   
# str = "The quick brown fox"
str = "The quick brown fox jumps over the lazy dog"
n = int(input("Please enter the desired length for the words: "))

var = str.split(" ")
wordsList = findLongWords(var, n)
# print(' '.join(wordsList)) # prints in string format
print(wordsList)