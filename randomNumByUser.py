import random

def guessByComputer(max):
    feedBack = "N"

    # Random initial guess by computer
    num = random.randint(1, max)
    min = 1

    # Get feedback from user to know if guess is correct.
    while(1):
        feedBack = input(f"Is {num} correct? Y/N\n")
        if(feedBack == "N"):
            if(input(f"Is guessed number high? Y/N\n") == "Y"):
                max = num - 1
                # num = random.randint(min, max-1)
            else:
                min = num + 1
                # num = random.randint(min+1, max)
            num = random.randint(min, max)
        else:
            break
    print(f"Computer guessed the number {num} correctly.")

max = int(input("Please enter the maximum number can be guessed.\n"))
guessByComputer(max)