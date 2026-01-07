board = [["X","","X"],
		["O","X","O"],
		["X","","O"]]

def CheckWin(board):
    # Checking win for rows
    if board[0][0] == board[0][1] == board[0][2] != "":
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] != "":
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] != "":
        return board[2][0]


    # Checking win for columns
    if board[0][0] == board[1][0] == board[2][0] != "":
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] != "":
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] != "":
        return board[0][2]


    # Checking Diagonal
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None


player = CheckWin(board)

if CheckWin(board) == "X":
    print(f"{player} wins!")
elif CheckWin(board) == "O":
    print(f"{player} wins!")
else:
    pass
