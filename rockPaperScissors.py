from random import randint

#create a list of play options
t = ['Rock', 'Paper', 'Scissors']

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input('Rock, Paper, Scissors?')
    if player == computer:
        print('Tie!')
    elif player == 'Rock': 
        if computer == 'Paper':
            print('Loser!', computer, 'covers', player)
        else:
            print('Winner!', player, 'smashes', computer)
    elif player == 'Paper':
        if computer == 'Scissors':
            print('Loser!', computer, 'slashes', player)
        else:
            print('Winner!', player, 'covers', computer)
    elif player == 'Scissors':
        if computer == 'Rock':
            print('Loser!', computer, 'smashes', player)
        else:
            print('Winner!', player, 'slashes', computer)
        #player was set to True, but we want it to be False so the loop continues
            player = False
            computer = t[randint(0,2)]
        