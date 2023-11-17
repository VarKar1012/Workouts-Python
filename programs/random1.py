import random

# create random number
def generateRandomNumber(min, max):
    num = random.randint(min, max)
    return num

# compare the user input with random number.
def compareUserInput(userInput, randNum, min, max):
    isSuccess = False

    if(userInput == randNum):
        print("Congratulations! You have guessed it correct.\n")
        isSuccess = True
    else:
        # randRange = int(1 - ((randNum - userInput) / 100))

        if(userInput < min):
            print("This is very lower than expected value. Try to guess it higher.\n")
        elif(userInput > max):
            print("You're guess is going through the roof. Come on down.\n")
        elif(userInput in range(randNum-100, randNum-50)):
            print("This is lower than expected value but you are getting near.\n")
        elif(userInput in range(randNum+50, randNum+100)):
            print("This is higher than expected value but you are getting near.\n")
        elif(userInput in range(randNum-20, randNum)):
            print("This is lower but so close. Try again.\n")
        elif(userInput in range(randNum+1, randNum+20)):
            print("This is higher but so close. Try again.\n")
        
        isSuccess = False

    return isSuccess

# driver code
min = 1000
max = 10000

randNum = generateRandomNumber(min, max)

userInput = int(input("Computer is holding a random number. Can you guess?\n"))

while(1):
    result = compareUserInput(userInput, randNum, min, max)
    if result == True:
        break
    userInput = int(input("New value: "))