""" Blackjack game driver & input test driver """

from src import player
from src import bank

# Semi-arbitrary max players
MAXPLAYERS = 1

def join_game():
    """ Add a player to the game """
    human = player.Player()
    human.get_name()
    if human:
        players.append(human)

def prepare_round():
    """ Setup everything for the beginning of a round
    Provide option for additional players to join
    """
    house.prepare_round()
    while len(players) < MAXPLAYERS:
        if (_ := input("The table has room, any new players? "))[0].upper() == 'Y':
            join_game()

def place_bets():
    """ Allow players to place their bets """

def deal_cards():
    """ Deal cards for the round """

def player_turns():
    """ Allow each player to take their turn """

def house_turn():
    """ House takes their turn """

def pay_bets():
    """ Pay any winning bets, take any remaining lost bets """

def another_round():
    """ Find out if we're going to play another round """
    endit = input("Are you done (enter y to exit)? ")
    if endit.upper() == 'Y':
        return False
    return True

if __name__ == "__main__":
    # Create the casino
    house = bank.Bank()
    # Our list of players - could be human or (eventually) bot
    players = []
    # We start by introducing the 'casino' and getting one player.
    print("Welcome to Blackjack")

    # Main game loop
    while True:
        prepare_round()
        place_bets()
        deal_cards()
        player_turns()
        house_turn()
        pay_bets()
        if not another_round():
            break

    # Print a final balance?
