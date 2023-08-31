# print board
def printBoard(board):
    for r in board:
        for c in r:
            print(c, end=' ')
        print('\n')

# update board
def updateBoard(board, pos, player):
    pos = int(pos)
    if pos <= 3:
        board[0][pos-1] = player
    elif pos <= 6:
        board[1][pos-4] = player
    else:
        board[2][pos-7] = player


# check for winner
def checkWinner(board, player):
    # for rows
    for r in board:
        if r.count(player) == 3:
            return True
        
    # for columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == player:
            return True 
    
    # diagonally
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


# check for Tie
def checkTie(board):
    for r in board:
        if r.count('-') > 0:
            return False
    return True