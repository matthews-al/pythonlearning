# Section 7 - Milestone project 1
# Requirements:
#   Display board state
#   Select play from numpad grid
#   Two local players
#   First player selects symbol
#   Detect game state (win / tie)

# Design elements
#   Board state tracked as array of characters. Index 0 is ignored for display simplicity

def display_board(board = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], legend=True):
    """ Prints out the current board state.   Default board is filled with 'X' player for validation """
    # Sanity check that the board is proper length
    if len(board) != 10:
        print("corrupt board")
        exit
    
    # Loop through the board to print state
    for i in range(1, 10, 3):
        if legend:
            print(" {} | {} | {}".format(i, i+1, i+2))
        else:
            print(" {} | {} | {}".format(" ", " ", " "))
        print(" {} | {} | {}".format(board[i], board[i+1], board[i+2]))
        print(" {} | {} | {}".format(" ", " ", " "))
        if i < 7:   # Print row separators if we aren't on the last row
            print("-"*11)

def new_board():
    """ Create an empty board for a new game """
    return [" "] * 10

def get_play(board, player):
    """ Get a square selection from the player and validate it
        player is a tupple (num, symbol)
        return the selected square index
        """
    pass

def game_loop():
    board = new_board()
    display_board(board, False)

playing=True
while playing:
    playing = False # This forces the game to exit unless the play again select y or yes
    game_loop()

    print('') # Give an extra line before asking if we play again
    again = input("Would you like to play again (Y/N)? ")
    if again.lower() == 'y' or again.lower() == 'yes':
        playing = True
    print('')
        
