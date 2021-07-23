#Board will be made using dictionary in which keys will be the location
#(ex. top-left,mid-right...etc)
#Initial values will be empty space and after every move
#Value will be changed according to player's choice

board = {'1': '', '2': '', '3': '',
         '4': '', '5': '', '6': '',
         '7': '', '8': '', '9': '' }

boardSpaces = []

for space in board: 
    boardSpaces.append(space)

#We will have to print the updated board after every move in the game and thus we will make a function in which we'll define
#the printBoard function so that the board can be printed easily

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

#Now we write game functionality

def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(board)
        print("\nIt's your turn, turn #" + turn + ". Move to which place?")

        move = input()

        if board[move] == '':
            board[move] = turn
            count += 1
        else:
            print("\nThat space is already taken.\nChoose another place")
            continue

        # Now we check if player X or 0 has won, for every move after 5 moves
        if count >= 5:
            if board['1'] == board['2'] == board['3'] != '':
                printBoard(board)
                print("\nGame Over.\n")
                print(' ***** ' + turn + " won. *****\n")
                break
            elif board['4'] == board['5'] == board['6'] != '':
                printBoard(board)
                print("\nGame Over.\n")
                print(' ***** ' + turn + " won. *****\n")
                break
            elif board['7'] == board['8'] == board['9'] != '':
                printBoard(board)
                print("\nGame Over.\n")
                print(' ***** ' + turn + " won. *****\n")
                break
            elif board['1'] == board['4'] == board['7'] != '':
                printBoard(board)
                print("\nGame Over.\n")
                print(' ***** ' + turn + " won. *****\n")
                break
            elif board['2'] == board['5'] == board['8'] != '':
                printBoard(board)
                print("\nGame Over.\n")
                print(' ***** ' + turn + " won. *****\n")
                break
            elif board['3'] == board['6'] == board['9'] != '':
                printBoard(board)
                print("\nGame Over.\n")
                print(' ***** ' + turn + " won. *****\n")
                break
            elif board['1'] == board['5'] == board['9'] != '':
                printBoard(board)
                print("\nGame Over.\n")
                print(' ***** ' + turn + " won. *****\n")
                break
            elif board['3'] == board['5'] == board['7'] != '':
                printBoard(board)
                print("\nGame Over.\n")
                print(' ***** ' + turn + " won. *****\n")
                break
        
        #If neither X or O wins the board 
        if count == 9:
            print('\nGAME OVER\n')
            print('TIE')
        
        #Change player after each move
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
#Now we ask if the player wants to restart
    restart = input('Do you want to play again?(y/n)')
    if restart == 'y' or restart == 'Y':
        for space in boardSpaces:
            board[space] = ''

            game()

if __name__ == "__main__":
    game()
