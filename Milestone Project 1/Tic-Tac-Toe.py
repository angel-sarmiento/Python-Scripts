##This the beginning of a file to create a game of tic tac toe using python


from IPython.display import clear_output
import math
import sys

def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# display_board(testing_board)
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


# function to decide each players choice of X or O in the game and return it as a tuple
def player_input():
    # continuously asking for an input until X or O is given
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Choose the starting symbol, X or O: ')
    # assigning player 1 as the chosen symbol
    player1 = marker

    # assigning player 2 as the opposite symbol
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)


def positionPlacer(marker, position):
    global emptyPos
    if game_board[position] == ' ':
        game_board[position] = marker
    else:
        print("That position is filled.")
        emptyPos = False


def check_win():
    winX = False
    winO = False

    # win if-statements for X
    if game_board[1] == 'X' and game_board[2] == 'X' and game_board[3] == 'X':
        winX = True
    elif game_board[4] == 'X' and game_board[5] == 'X' and game_board[6] == 'X':
        winX = True
    elif game_board[7] == 'X' and game_board[8] == 'X' and game_board[9] == 'X':
        winX = True
    elif game_board[1] == 'X' and game_board[4] == 'X' and game_board[7] == 'X':
        winX = True
    elif game_board[2] == 'X' and game_board[5] == 'X' and game_board[8] == 'X':
        winX = True
    elif game_board[3] == 'X' and game_board[6] == 'X' and game_board[9] == 'X':
        winX = True
    elif game_board[1] == 'X' and game_board[5] == 'X' and game_board[9] == 'X':
        winX = True
    elif game_board[3] == 'X' and game_board[5] == 'X' and game_board[7] == 'X':
        winX = True
    # win if-statements for Y
    elif game_board[1] == 'O' and game_board[2] == 'O' and game_board[3] == 'O':
        winO = True
    elif game_board[4] == 'O' and game_board[5] == 'O' and game_board[6] == 'O':
        winO = True
    elif game_board[7] == 'O' and game_board[8] == 'O' and game_board[9] == 'O':
        winO = True
    elif game_board[1] == 'O' and game_board[4] == 'O' and game_board[7] == 'O':
        winO = True
    elif game_board[2] == 'O' and game_board[5] == 'O' and game_board[8] == 'O':
        winO = True
    elif game_board[3] == 'O' and game_board[6] == 'O' and game_board[9] == 'O':
        winO = True
    elif game_board[1] == 'O' and game_board[5] == 'O' and game_board[9] == 'O':
        winO = True
    elif game_board[3] == 'O' and game_board[5] == 'O' and game_board[7] == 'O':
        winO = True

    if winX == True or winO == True:
        print("Winner!")
        sys.exit()

    return (winX, winO)


# area for while loop that allows the game to run and will terminate it when the win condition is met

print("This is a game of Tic Tac Toe!")
display_board(game_board)
p1, p2 = player_input()

while check_win() == (False, False):

    #player1 choosing a position
    new_pos = int(input("Player 1, choose a position on the board."))
    positionPlacer(p1, new_pos)
    display_board(game_board)
    check_win()

    #player2 choosing a position
    new_pos = int(input("Player 2, choose a position on the board."))
    positionPlacer(p2, new_pos)
    display_board(game_board)
