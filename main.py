import random
import os
import sys

board = ['' for x in range(10)]
test_board = ['#','X','O','X','O','X','O','X','O','X']

def display_board(board):
    #print out a board as a list, where each index 1-9
    # # corresponds with a number on a number pad for 3 by 3 board representation.
    print('\n\n')
    print('   |   | ')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('-----------')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('   |   | ')
    print('\n')

# print('\n'*100)#clears out




def players_input():
# take in a player input and assign their marker as 'X' or 'O'.
# while loops to continually ask until you get a correct answer.
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X': #tuple assign player (player1,player2)
        return ('X','O')
    else:
        return ('O','X')



# # place maker (board, marker, position)
def place_maker(board,mark,position):
#takes in the board, marker ('X' or 'O'), position (number 1-9) and assigns it to the board.
    board[position]= mark


def choose_first():
#choose player that goes first (random)
    choice = ('Player1','Player2')
    print(f"The player who goes first is going to be random so lets make: {random.choice(choice)} go first!\n")
    if choice[0]== "Player1":
        return "Player1"
    else:
        return "Player2"


def win_check(board,mark):
# return True if Win
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def space_check(board,position):
# returns True indicating whether a space on the board is freely available.
    return board[position] == ' '


def full_board_check(board):
#checks if the board is full and returns a True if full
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board, turn):
# asks for a player's next position (as a number 1-9) 
#check if it's a free position with space_check()
#return the position for later use.
    position = 0
    try:
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
            position = int(input(f'{turn} Choose your next position: (1-9) '))
    except ValueError:
        print(" Pick Again! That is not a number idiot")
    return position




def replay():
#asks the player if they want to play again  
#returns True if they do want to play again.
        return (input(" would you like to keep playing: (y or n)").upper().startswith('Y'))
# #run the main game


def main_game():
    os.system("cls") # clears the output of the terminal

    while True: #keep playing break at very end ends the whole loop

        p1_marker,p2_marker =players_input() #gets the input and assigns them to a marker it was created in a tuple

        game_board= [' 'for i in range(10)] # making an empty game board
        turn = choose_first()

        play_game = input('\nAre you ready to play? Enter Yes or No.')

        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == "Player1":#for player one
                # play game
                display_board(game_board)
                position = player_choice(game_board,turn)
                place_maker(game_board,p1_marker,position)

                #wincheck
                if win_check(game_board, p1_marker):
                    print("\n\n\n\nYou Won Player1\n sucks to be player2")
                    display_board(game_board)
                    break
                else:
                    if full_board_check(game_board):
                        print("\n\n\n\nThis seems to be a draw \ntry playing again for a winner")
                        display_board(game_board)
                        break
                    else:
                        turn = "Player2" # will exit and not repeat if statment of player one because turn is now = 'Player2'
            else:#for player two

                display_board(game_board)
                position = player_choice(game_board,turn)
                place_maker(game_board, p2_marker, position)

                if win_check(game_board, p2_marker):
                    print("\n\n\n\nYou Won Player2\n sucks to be player1")
                    display_board(game_board)
                    break
                else:
                    if full_board_check(game_board):
                        print("\n\n\n\nThis seems to be a draw \ntry playing again for a winner")
                        display_board(game_board)
                        break #will break out of the loop and go to replay
                    else:
                        turn = "Player1" # will exit and not repeat if statment of player two because turn is now = 'Player1'
        if replay() == False:
                        break

main_game()