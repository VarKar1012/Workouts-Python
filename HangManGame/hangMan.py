import random
from hangManInput import words

# driver code
def hangman():
    print("Welcome to HangMan. Here's your clue:-")
    randomWord = random.choice(words)
    size = len(randomWord)
    word_dict = dict(enumerate(randomWord)) # for index-letter info

    # create clue based on length of the selected word.
    clue_size = list(map(lambda x: '-', randomWord))
    print(''.join(clue_size))

    # Gives user guesses = length of selected word + 2 additional choices
    for choice in range(size+5):
        # prompt user to guess
        userIn = input("Enter a guess: ")
        if userIn in word_dict.values():
            # Find the index of user input.
            index = [indx for indx, letter in word_dict.items() if letter == userIn][0]
            # Change the value in the dictionary to empty string.
            word_dict[index] = ''

            clue_size[index] = userIn
            print(''.join(clue_size))
            if('-' not in clue_size):
                print("Congratulations, you've completed the game.")
                break

    if '-' in clue_size:
        print("Sorry, (", randomWord, ") your guesses are over. Good luck next time.")

hangman()