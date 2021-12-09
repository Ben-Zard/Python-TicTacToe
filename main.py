board = [f'{x}' for x in range(10)]
#board game layout to display board game takes (board as input)
def display_board(board):
    print('   |   | ')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('-----------')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('   |   | ')

display_board(board)
#append the board game with the input
# print('\n'*100)#clears out

# #Write a function that can print out a board. Set up your board as a list, where each index 1-9
# # corresponds with a number on a number pad, so you get a 3 by 3 board representation.
#
# #player input to assign player at X or O ()
# def players_input():
#
# #Write a function that can take in a player input and assign their marker as 'X' or 'O'.
# # Think about using while loops to continually ask until you get a correct answer.
#
#
# # place maker (board, marker, position)
# def place_maker(board,marker,position):
#
# #Write a function that takes in the board list object, a marker ('X' or 'O'),
# # and a desired position (number 1-9) and assigns it to the board.
#
# #choose player that goes first (random or something else no input peramiter maybe)
# def choose_first():
#
# #Write a function that uses the random module to randomly decide which player goes first.
# # You may want to lookup random.randint() Return a string of which player went first.
#
#
# #check if win
# def win_check(board,marker):
#
# #run the win_check function against our test_board - it should return True
#
# #player space input check
# def board_check(board,position):
#
# # Write a function that returns a boolean indicating whether a space on the board is freely available.
#
#
# #check if the board is full
# def full_board_check(board):
#
# # Write a function that checks if the board is full and returns a boolean value.
# # True if full, False otherwise.
#
#
# def player_choice(board):
# #Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position.
# # If it is, then return the position for later use.
#
#
# #if they want to play again
# def rreplay():
#
# #Write a function that asks the player if they want to play again and returns a boolean
# # True if they do want to play again.
#
#
#
# #run the main game
# def main():
#     #keep playing use else break