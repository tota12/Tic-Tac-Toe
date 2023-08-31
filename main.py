import utils

#design game board
board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

# take player1 input
print('Welcome to Tic Tac Toe!')

print('Player1, Would you like to be X or O?')
while True:
    player1 = input().upper()
    if len(player1) == 1 and player1 in 'XO':
        break
    else:
        print('Please enter X or O')

# assign player2
if player1 == 'X':        
    player2 = 'O'
else:
    player2 = 'X'

player1_score = 0
player2_score = 0

while True:
    validPos = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # main game loop
    while True:
        # player1 turn
        print('Player1, choose a position (1-9)')
        while True:
            player1_pos = input()
            if len(player1_pos) == 1 and player1_pos in validPos:
                validPos.remove(player1_pos)
                break
            else:
                print('Invalid Position. Please enter a number of these: ', validPos)
        utils.updateBoard(board, player1_pos, player1)
        utils.printBoard(board)
        if utils.checkWinner(board, player1):
            print('Player1 wins!')
            player1_score += 1
            break
        if utils.checkTie(board):
            print('Tie!')
            break

        # player2 turn
        print('Player2, choose a position (1-9)')
        while True:
            player2_pos = input()
            if len(player2_pos) == 1 and player2_pos in validPos:
                validPos.remove(player2_pos)
                break
            else:
                print('Invalid Position. Please enter a number of these: ', validPos)
        utils.updateBoard(board, player2_pos, player2)
        utils.printBoard(board)
        if utils.checkWinner(board, player2):
            print('Player2 wins!')
            player2_score += 1
            break
        if utils.checkTie(board):
            print('Tie!')
            break
    
    # print score
    print('Player1: ', player1_score, 'Player2: ', player2_score)
    
    # ask for replay
    print('Would you like to play again? (Y/N)')
    while True:
        choice = input().upper()
        if choice == 'N':
            exit()
        elif choice == 'Y':
            board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
            validPos = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            break
        else:
            print('Invalid input. Please enter Y or N')
