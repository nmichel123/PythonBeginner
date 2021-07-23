from random import randint

#create a list of play options
t = ['Rock', 'Paper', 'Scissors']

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
#\n is regex code for new line for formatting in terminal
    player = input('\nRock, Paper, Scissors?')
    if player == computer:
        print('Tie!')
    elif player == 'Rock': 
        if computer == 'Paper':
            print('\nLoser!', computer, 'covers', player)
        else:
            print('\nWinner!', player, 'smashes', computer)
    elif player == 'Paper':
        if computer == 'Scissors':
            print('\nLoser!', computer, 'slashes', player)
        else:
            print('\nWinner!', player, 'covers', computer)
    elif player == 'Scissors':
        if computer == 'Rock':
            print('\nLoser!', computer, 'smashes', player)
        else:
            print('\nWinner!', player, 'slashes', computer)
        #player was set to True, but we want it to be False so the loop continues
        player = False
        computer = t[randint(0,2)]
        