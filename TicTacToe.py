board = ["X","X","X",
		"O","","O",
		"","",""]

def CheckWin(board):
    # Checking win for rows
    if board[0] == board[1] == board[2] != "":
        return board[0]
	if board[3] == board[4] == board[5] != "":
        return board[3]
    if board[6] == board[7] == board[8] != "":
        return board[6]


    # Checking win for columns
    if board[0] == board[3] == board[6] != "":
        return board[0]
    if board[1] == board[4] == board[7] != "":
        return board[1]
    if board[2] == board[5] == board[8] != "":
        return board[2]


    # Checking Diagonal
    if board[0] == board[4] == board[8] != "":
        return board[0]
    if board[2] == board[4] == board[6] != "":
        return board[2]
    return None


player = CheckWin(board)

if CheckWin(board):
    print(f"{player} wins!")
else:
    pass
