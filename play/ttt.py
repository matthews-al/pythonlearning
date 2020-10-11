# Section 7 - Milestone project 1
# Requirements:
#   Display board state
#   Select play from numpad grid
#   Two local players
#   First player selects symbol
#   Detect game state (win / tie)

# Design elements
#   Board state tracked as array of characters. Index 0 is ignored for display simplicity

def display_board(board = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], legend=False):
    """ Prints out the current board state.   Default board is filled with 'X' player for validation """
    # Sanity check that the board is proper length
    if len(board) != 10:
        print("corrupt board")
        exit
    
    # Loop through the board to print state
    for i in range(7, 0, -3):
        if legend:
            print(" {} | {} | {}".format(i, i+1, i+2))
        else:
            print(" {} | {} | {}".format(" ", " ", " "))
        print(" {} | {} | {}".format(board[i], board[i+1], board[i+2]))
        print(" {} | {} | {}".format(" ", " ", " "))
        if i > 1:   # Print row separators if we aren't on the last row
            print("-"*11)

def new_board():
    """ Create an empty board for a new game """
    return [" "] * 10

def get_play(board, player):
    """ Get a square selection from the player and validate it
        return the selected square index - return 0 for a skipped turn
        """
    for tries in range(2,-1,-1):   # We'll give the player 3 attempts to make a valid selection
        sel = input(f"Player {player}: Select your move: ")
        try:
            sel = int(sel)
        except:
            print(f"That was not a valid move, try again.  {tries} remaining")
            continue
        if 0 < sel < 10:  # Make sure the selection is in range
            if board[sel] == " ":
                return sel
            else:
                print(f"That square is already occupied. Try again.  {tries} remaining")
                if tries > 0: display_board(board, True)
                continue
        else:
            print(f"Input must be between 1 and 9.  Try again. {tries} remaining")
            if tries > 0: display_board(board, True)
    return 0  # Fall through if the player doesn't make a valid selection

def get_pone():
    """ Ask player one to select their symbol """
    for tries in range(2,-1,-1):   # We'll give the player 3 attempts to make a valid selection
        sym = input("Player 1, please choose your symbol - 'X' or 'O': ")
        if sym.upper() == 'X' or sym.upper() == 'O':
            return sym.upper()
        else:
            print(f"Invalid symbol, will default to 'X' in {tries} attempts")
    return 'X'

def game_loop():
    board = new_board()
    players = [' '] * 2
    players[0] = get_pone()
    if players[0] == 'X':
        players[1] = 'O'
    else:
        players[1] = 'X'

    curplayer = 0
    turncounter = 1 # Temporary turn counter until we get win detection
    playing = True
    while playing:
        display_board(board)
        selection = get_play(board, curplayer+1)
        board[selection] = players[curplayer]
        curplayer = (curplayer + 1) % 2
        turncounter += 1
        if turncounter > 10: break

    display_board(board)

"""
playing=True
while playing:
    playing = False # This forces the game to exit unless the play again select y or yes
    game_loop()

    print('') # Give an extra line before asking if we play again
    again = input("Would you like to play again (Y/N)? ")
    if again.lower() == 'y' or again.lower() == 'yes':
        playing = True
    print('')
"""        
game_loop()
