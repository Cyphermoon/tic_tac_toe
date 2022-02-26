import random
ALL_SPACES = list("123456789")
BLANK = " "
current_player, second_player = ("x", "o")

def get_board():
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK
    
    return board

def print_board(board):
    print(f"""
        {board["1"]} | {board["2"]} | {board["3"]}  
        ---------  
        {board["4"]} | {board["5"]} | {board["6"]}
        ---------  
        {board["7"]} | {board["8"]} | {board["9"]}
    """)


def isboard_full(board):
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False

    return True

def isValidSpace(board, choice):
    if board.get(choice, "error") == BLANK and choice in ALL_SPACES:
        return True
    return False


def get_winner(board, current_player):
    b, c = board, current_player

    if ((b["1"] == b["2"] == b["3"] == c) or
        (b["4"] == b["5"] == b["6"] == c) or
        (b["7"] == b["8"] == b["9"] == c) or

        (b["1"] == b["4"] == b["7"] == c) or
        (b["2"] == b["5"] == b["8"] == c) or
        (b["3"] == b["6"] == b["9"] == c) or
        
        (b["1"] == b["5"] == b["9"] == c) or
        (b["3"] == b["5"] == b["7"] == c) ):
        return c

def get_player_choice():
    choice = input("Choose a position: ")
    return choice

def get_comp_move(duplicate_board):
    copied_board = duplicate_board.copy()
    available_moves = [k for k,v in copied_board.items() if v == BLANK]
    print(available_moves)
    computer_choice = random.choice(available_moves)

    for player in ["o", "x"]:
        for move in available_moves:  
            copied_board[move] = player

            if get_winner(copied_board, player) == player:
                computer_choice = move

            copied_board[move] = BLANK
    
    return computer_choice


gameboard = get_board()
duplicate_board = {'1': 'o', '2': ' ', '3': ' ', '4': 'o', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

#get_comp_move(duplicate_board)

while True:
    player_choice = get_player_choice() if current_player == "x" else get_comp_move(gameboard)
    print(player_choice)
    if isValidSpace(gameboard, player_choice):
        gameboard[player_choice] = current_player
        print_board(gameboard)

    else:
        print("invalid input")
        continue

    winner = get_winner(gameboard, current_player)
    if winner == current_player:
        print(f"{current_player} is the winner")
        break

    if isboard_full(gameboard):
        print("it is a tie")
        break

    current_player,second_player = second_player, current_player 




