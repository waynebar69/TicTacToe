import random

num_list = [1, 2, 3, 4, "X", 6, 7, 8, 9] # Assume Computer's first choice is always 5
game_over = False


def display_board(board):
    """The function accepts one parameter containing the board's current status and prints it out to the console."""
    background = (f"\n    +---+---+---+\n\
    | {board[0]} | {board[1]} | {board[2]} |\n\
    +---+---+---+\n\
    | {board[3]} | {board[4]} | {board[5]} |\n\
    +---+---+---+\n\
    | {board[6]} | {board[7]} | {board[8]} |\n\
    +---+---+---+\n")
    print(background)
    return


def enter_move(board):
    """The function accepts the board current status, asks the user about their move, checks the input and updates
    the board according to the user's decision."""
    user_move = int(input("Make your move, select 1 - 9 to place your mark! "))
    if user_move < 1 or user_move > 9:
        print("Invalid selection!, try again")
        enter_move(board)
    else:
        if user_move in board:
            user_index = board.index(user_move)
            marking_O = board[user_index] = "O"
            return marking_O
        else:
            print("Invalid selection!, try again")
            enter_move(board)


def make_list_of_free_fields(board):
    """The function browses the board and builds a list of all the free squares."""
    free_squares = []
    for i in board:
        if i not in free_squares:
            free_squares.append(i)
        for i in free_squares:
            if i == "X" or i == "O":
                while i in free_squares:
                    free_squares.remove(i)
    return free_squares


def victory_for(board, sign):
    """ The function checks the board which sign has won and terminates the game if True."""
    global game_over
    if sign == board[0] and sign == board[1] and sign == board[2] or \
            sign == board[3] and sign == board[4] and sign == board[5] or \
            sign == board[6] and sign == board[7] and sign == board[8] or \
            sign == board[0] and sign == board[3] and sign == board[6] or \
            sign == board[1] and sign == board[4] and sign == board[7] or \
            sign == board[2] and sign == board[5] and sign == board[8] or \
            sign == board[0] and sign == board[4] and sign == board[8] or \
            sign == board[2] and sign == board[4] and sign == board[6]:
        print(f"{sign} WINS!")
        game_over = True
        return game_over
    else:
        if make_list_of_free_fields(board) == []:
            print("The game is a Draw, Better luck next time!")
            game_over = True
            return game_over


def draw_move(board):
    """The function randomly chooses a number from the board for the computers turn."""
    computer_num = random.randint(1, 9)
    if computer_num in board:
        computer_index = board.index(computer_num)
        marking_x = board[computer_index] = "X"
        return marking_x
    else:
        draw_move(board)


while not game_over:
    #Display the board with ASCII Art
    display_board(num_list)

    #Users turn to choose a position & check win condition
    enter_move(num_list)
    victory_for(num_list, "O")
    if game_over:
        break

    #Computers turn to choose a position & check win condition
    draw_move(num_list)
    victory_for(num_list, "X")
