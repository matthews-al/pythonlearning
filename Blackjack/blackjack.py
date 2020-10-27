""" Blackjack game driver & input test driver """

import player
import bank

# Semi-arbitrary max players
MAXPLAYERS = 2

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
        joinin = input("The table has room, any new players? ")
        if len(joinin) > 0 and joinin[0].lower() == 'y':
            join_game()
        else:
            break
    for play in players:
        play.prepare_round()

def place_bets():
    """ Allow players to place their bets """
    for play in players:
        play.get_bet()

def deal_cards():
    """ Deal cards for the round """
    for _ in range(0, 2):
        for play in players:
            if play.bet > 0:
                play.dealt_card(house.deal_card())
        house.dealer_draw(house.deal_card())

def player_turns():
    """ Allow each player to take their turn """
    for play in players:
        play.play_round(house)

def house_turn():
    """ House takes their turn """
    house.dealer_turn()

def pay_bets():
    """ Pay any winning bets, take any remaining lost bets """
    (dealer_value, _, _) = house.dealer_hand_value()
    for play in players:
        # don't report status for players without a bet
        if play.bet == 0:
            continue
        playval, _, _ = play.hand_value()
        if dealer_value > 21:
            play.win(dealer_value)
        elif playval < dealer_value:
            play.lose(dealer_value)
        elif playval == dealer_value:
            play.push(dealer_value)
        else:
            play.win(dealer_value)

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
        if not house.dealer_21():
            player_turns()
            house_turn()
        pay_bets()
        if not another_round():
            break

    # Print a final balance?
