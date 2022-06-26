board = [" " for i in range(9)]


# function that prints the grid
def print_board():
    # put space in grid rows
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    # print grid rows
    print()
    print(row1)
    print(row2)
    print(row3)
    print()


# function that prints layout
def print_layout():
    # put numbers into grid rows
    row1 = "|{}|{}|{}|".format(1, 2, 3)
    row2 = "|{}|{}|{}|".format(4, 5, 6)
    row3 = "|{}|{}|{}|".format(7, 8, 9)

    # print grid rows
    print()
    print(row1)
    print(row2)
    print(row3)
    print()


# function to execute the players move
def player_move(icon):

    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print("your turn player {}".format(number))

    choice = int(input("Enter your move(1-9): ").strip())
    if board[choice-1] == " ":
        board[choice-1] = icon
    else:
        print()
        print("sorry that space is taken up")


# function to check if players had won
def is_victory(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or\
            (board[3] == icon and board[4] == icon and board[5] == icon) or\
            (board[6] == icon and board[7] == icon and board[8] == icon) or\
            (board[0] == icon and board[3] == icon and board[6] == icon) or\
            (board[1] == icon and board[4] == icon and board[7] == icon) or\
            (board[2] == icon and board[5] == icon and board[8] == icon) or\
            (board[0] == icon and board[4] == icon and board[8] == icon) or\
            (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


# function that checks if the players had a tie
def is_draw():
    if " " not in board:
        return True
    else:
        return False


# print layout
print("layout:")
print_layout()

# run the game in loop
while True:
    print_board()
    # check for "X"
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X wins! Congratulations")
        break
    elif is_draw():
        print("its a draw!")
        break
    # check for "O"
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O wins! Congratulations!")
        break
    elif is_draw():
        print("its a draw!")
        break
