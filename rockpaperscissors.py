import random as rand

list = ['rock', 'paper', 'scissors']

play = True

while(play):
    computerOutput = list[rand.randrange(0, len(list))]
    userInput = input()

    if(userInput == 'rock'):
        if(computerOutput == 'paper'):
            print('you lose!')
        else:
            print('you win!')
    elif(userInput == 'scissors'):
        if(computerOutput == 'rock'):
            print('you lose!')
        else:
            print('you win!')
    else:
        if(computerOutput == 'scissors'):
            print('you lose!')
        else:
            print('you win!')

    print('Play again?')
    playAgain = input()

    if (playAgain == 'no'):
        play = not play
