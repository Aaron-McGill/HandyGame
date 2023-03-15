def handy_game_intro():
    game_choice = input("Welcome to HandyGame, which of the following games would you like to play: A) Tic-Tac-Toe, B) Connect Four, C) Exit HandyGame ").strip().lower()
    if game_choice == "a":
        return "Tic-Tac-Toe"
    elif game_choice == "b":
        return "Connect Four"
    elif game_choice == "c":
        return "Exit"

def play_game(game, player_names):
    print(instruction_manual(game))
    while True:
        print_board(game)
        player_move(game, "X", player_names)
        print_board(game)
        if is_victory(game, "X"):
            print("Player X wins! Congratulations {}!".format(player_names[0]))
            break
        elif is_draw():
            print("Its a draw!")
            break
        player_move(game, "O", player_names)
        if is_victory(game, "O"):
            print_board(game)
            print("Player O wins! Congratulations {}!".format(player_names[1]))
            break
        elif is_draw():
            print("Its a draw!")
            break

def instruction_manual(game_name):
    if game_name == "Tic-Tac-Toe":
        return "~Tic-Tac-Toe instructions~"
    elif game_name == "Connect Four":
        return "~Connect Four instructions~"

def print_board(game):
    if game == "Tic-Tac-Toe":
        row1 = "|  {}  |  {}  |  {}  |".format(board[0], board[1], board[2])
        row2 = "|  {}  |  {}  |  {}  |".format(board[3], board[4], board[5])
        row3 = "|  {}  |  {}  |  {}  |".format(board[6], board[7], board[8])
        print()
        print(row1)
        print(row2)
        print(row3)
        print()
    elif game == "Connect Four":
        row1 = "|  {}  |  {}  |  {}  |  {}  |".format(board[0], board[1], board[2], board[3])
        row2 = "|  {}  |  {}  |  {}  |  {}  |".format(board[4], board[5], board[6], board[7])
        row3 = "|  {}  |  {}  |  {}  |  {}  |".format(board[8], board[9], board[10], board[11])
        row4 = "|  {}  |  {}  |  {}  |  {}  |".format(board[12], board[13], board[14], board[15])
        print()
        print(row1)
        print(row2)
        print(row3)
        print(row4)
        print()

def player_move(game, icon, player_names):
    if icon == "X":
        print("Your turn player {} ({})".format(icon, player_names[0]))
    elif icon == "O":
        print("Your turn player {} ({})".format(icon, player_names[1]))
    if game == "Tic-Tac-Toe":
        choice = int(input("Enter your move (1-9): ").strip())
        while choice not in range(1,10):
            choice = int(input("You entered an invalid spot. Please enter the spot you would like to place your token (1-9): ").strip())
        if board[choice-1] == " ":
            board[choice-1] = icon
        else:
            print("That space is taken! Please select another space.")
            print_board(game)
            player_move(game, icon, player_names)
    elif game == "Connect Four":
        choice = int(input("Enter the column you would like to drop your token (1-4): ").strip())
        while choice not in range(1,5):
            choice = int(input("You entered an invalid column. Please enter the column you would like to drop your token (1-4): ").strip())
        if board[(choice-1)+12] == " ":
            board[(choice-1)+12] = icon
        elif board[(choice-1)+8] == " ":
            board[(choice-1)+8] = icon
        elif board[(choice-1)+4] == " ":
            board[(choice-1)+4] = icon
        elif board[(choice-1)+0] == " ":
            board[(choice-1)+0] = icon
        else:
            print("That column is full! Please choose another column.")
            print_board(game)
            player_move(game, icon, player_names)

def is_victory(game, icon):
    if game == "Tic-Tac-Toe":
        if (board[0] == icon and board[1] == icon and board[2] == icon) or \
           (board[3] == icon and board[4] == icon and board[5] == icon) or \
           (board[6] == icon and board[7] == icon and board[8] == icon) or \
           (board[0] == icon and board[3] == icon and board[6] == icon) or \
           (board[1] == icon and board[4] == icon and board[7] == icon) or \
           (board[2] == icon and board[5] == icon and board[8] == icon) or \
           (board[0] == icon and board[4] == icon and board[8] == icon) or \
           (board[2] == icon and board[4] == icon and board[6] == icon):
            return True
        else:
            return False
    elif game == "Connect Four":
        if (board[0] == icon and board[1] == icon and board[2] == icon and board[3] == icon) or \
           (board[4] == icon and board[5] == icon and board[6] == icon and board[7] == icon) or \
           (board[8] == icon and board[9] == icon and board[10] == icon and board[11] == icon) or \
           (board[12] == icon and board[13] == icon and board[14] == icon and board[15] == icon) or \
           (board[0] == icon and board[4] == icon and board[8] == icon and board[12] == icon) or \
           (board[1] == icon and board[5] == icon and board[9] == icon and board[13] == icon) or \
           (board[2] == icon and board[6] == icon and board[10] == icon and board[14] == icon) or \
           (board[3] == icon and board[7] == icon and board[11] == icon and board[15] == icon) or \
           (board[0] == icon and board[5] == icon and board[10] == icon and board[15] == icon) or \
           (board[3] == icon and board[6] == icon and board[9] == icon and board[12] == icon):  
            return True
        else:
            return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False

def get_player_names():
    player_names = ["",""]
    player1_name = input("What is player 1's name? ")
    while player1_name == "":
        player1_name = input("Sorry, please enter a valid name. What is player 1's name? ")
    print("Welcome to HandyGame {}! You will be player X for this game.".format(player1_name))
    player2_name = input("What is player 2's name? ")
    while player2_name == "":
        player2_name = input("Sorry, please enter a valid name. What is player 2's name? ")
    print("Welcome to HandyGame {}! You will be player O for this game.".format(player2_name))
    player_names = [player1_name,player2_name]
    return player_names



while True:
    game = handy_game_intro()
    if game == "Exit":
        print("Sorry to see you go, please come back to play HandyGame soon!")
        break
    if game == "Tic-Tac-Toe":
        board = [" " for i in range(9)]
        player_names = get_player_names()
        play_game(game, player_names)
    elif game == "Connect Four":
        board = [" " for i in range(16)]
        player_names = get_player_names()
        play_game(game, player_names)
  
