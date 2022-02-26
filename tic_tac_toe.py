def main():
    """Tic Tac Toe """
    ALL_SPACES = list("123456789")
    BLANK = " "
    current_player, second_player = "x", "o"
    x_score, o_score = 0,0
    board = {}

    def get_board():
        for space in ALL_SPACES:
            board[space] = BLANK
        return board
    
    def clear_board():
        for space in ALL_SPACES:
            board[space] = BLANK

        return board


    def print_board(board):
        print(f"""
            {board["1"]} | {board["2"]} | {board["3"]}      1 2 3
            ---------
            {board["4"]} | {board["5"]} | {board["6"]}      4 5 6
            ---------
            {board["7"]} | {board["8"]} | {board["9"]}      7 8 9
        """)


    def isboard_full(board):
        for space in ALL_SPACES:
            if board[space] == BLANK:
                return False

        return True


    def isValid_space(board, player_choice):
        if board.get(player_choice, "error") == BLANK and player_choice in ALL_SPACES:
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



    gameboard = get_board()

    print("Welcome to a game of Tic Tac Toe")
    print_board(gameboard)

    while True:
        print("Current Player: " + current_player)
        player_choice = input("Make a choice: ")

        if player_choice == "quit":
            break

        if isValid_space(gameboard, player_choice):
            gameboard[player_choice] = current_player
            print_board(gameboard)

        else:
            print("invalid input")
            continue
        
        winner = get_winner(gameboard, current_player)
        if winner == current_player:
            clear_board()
            if winner == "x":
                x_score += 1
            
            if winner == "o":
                o_score += 1

            print(f"{current_player} is the winner")
            print(f"Scores X:{x_score}  O:{o_score} \n")
            continue

        if isboard_full(gameboard):
            clear_board()
            print("it is a tie")
            continue

        current_player, second_player = second_player, current_player


if __name__ == "__main__":
    main()


