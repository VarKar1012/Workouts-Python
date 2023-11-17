import random

# create random number
def generateRandomNumber(min, max):
    num = random.randint(min, max)
    return num

# compare the user input with random number.
def compareUserInput(userInput, randNum):
    isSuccess = False

    if(userInput == randNum):
        isSuccess = True
    else:
        if(userInput < randNum):
            print("Wrong. Try to guess higher.\n")
        elif(userInput > randNum):
            print("Wrong. Try to guess lower.\n")
        
        isSuccess = False

    return isSuccess

# driver code
min = 1
max = 10

randNum = generateRandomNumber(min, max)

userInput = int(input("Computer is holding a random number in the range of 1 & 10. Can you guess?\n"))

while(1):
    result = compareUserInput(userInput, randNum)
    if result == True:
        break
    userInput = int(input("New guess: "))

print(f"Congratulations! You have guessed the number {randNum} correctly.\n")