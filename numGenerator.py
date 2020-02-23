import random as Random
gen = Random
num = gen.randrange(1, 20)
inputNum = -1

while(inputNum != num):
    print("enter a number!")
    inputNum = int(input())

    if(inputNum == num):
        print("you win!")
    else:
        print("try again")
