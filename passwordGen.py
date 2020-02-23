import random as random


print("PASSWORD GENERATOR")

allSymbols = ['#', '@', '$', '%', '^', '&', '*']
allNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
allLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def genPass():
    # variables
    length = 0
    letters = 0
    numbers = 0
    symbols = 0
    password = ""

    # get User Inpnut
    print("Desired Password Length: ")
    length = int(input())
    print("Desired Number of Letters: ")
    letters = int(input())
    print("Desired Number of Numbers: ")
    numbers = int(input())
    symbols = length - letters - numbers

    # create password

    # track variables
    curLength = 0
    curLetters = 0
    curNumbers = 0

    while(curLength < length):
        # decide which character to add
        toAdd = random.randint(1, 3)
        if(toAdd == 1 and curLetters < letters):
            # capitilize depending on random output
            letter = allLetters[random.randint(0, len(allLetters) - 1)]
            capitalize = random.randint(0, 1)
            if(capitalize == 1):
                letter = letter.capitalize()
            password += letter
        elif(toAdd == 2 and curNumbers < numbers):
            password += str(allNumbers[random.randint(0, len(allNumbers)) - 1])
        else:
            password += allSymbols[random.randint(0, len(allSymbols) - 1)]
        curLength += 1

    # print password
    print(password)

    # check if user wants another password
    print("Generate another password? Y|N")
    response = input()
    if(response == "Y"):
        genPass()


# call function
genPass()
