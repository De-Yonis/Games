#board
#display board
#play game
#handle turns
#check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip player

board = ["-","-","-",
        "-", "-","-",
        "-","-","-"]

game_still_going = True

winner = None

current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

    display_board()
    
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("It looks like nobody one its a Tie.")

def handle_turn(player): 
    print("Its", player + "'s turn")
    position = input("Choose a position on the board from 1-9: ")
    
    check = True
    while check: 

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position on the board from 1-9: ")

        position = int(position) - 1 

        if board[position] != "-":
            print("What you trying to do, that position has already been taken. Go again mate!")
            check = True
        else:
            check = False

    board[position] = player

    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    
    global winner

    row_winner = check_rows()
    # print(row_winner)
    column_winner = check_columns()

    diagonal_winner = check_diagonals()


    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return winner

def check_rows():

    global game_still_going

    #check if any of the rows have all the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    
    winning_player = ""
    if row_1:
        winning_player = board[0]
        return winning_player
    elif row_2:
        winning_player = board[3]
        return winning_player
    elif row_3:
        winning_player = board[6]
        return winning_player
    
    return
    
def check_columns():
    global game_still_going

    #check if any of the columns have all the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
    
    winning_player = ""
    if column_1:
        winning_player = board[0]
        return winning_player
    elif column_2:
        winning_player = board[1]
        return winning_player
    elif column_3:
        winning_player = board[2]
        return winning_player
    
    return 

def check_diagonals():
    global game_still_going

    #check if any of the diagonals have all the same value
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"

    if diagonals_1 or diagonals_2:
        game_still_going = False
    
    winning_player = ""
    if diagonals_1:
        winning_player = board[0]
        return winning_player
    elif diagonals_2:
        winning_player = board[6]
        return winning_player

    
    return 
    

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"
    return

play_game()