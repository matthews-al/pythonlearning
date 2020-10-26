""" Underlying player class
Players need:
* Chip balance
* a current hand (or pair of hands for split)
"""

class Player():
    """ This is our base player class """
    def __init__(self, name="Player"):
        """ Initialize a player - at Python Casino, we give new players 100 chips to play """
        self.name = name
        self.chips = 100
        self.hand1 = []
        self.hand2 = []
        self.bet = 0
        self.lastbet = 0

    def get_bet(self):
        """ Request a bet from the player """
        while newbet := input(f"{self.name}: {self.lastbet} chips. Last bet: {self.chips}.  Bet: "):
            try:
                newbet = int(newbet)
                if newbet in range(0, self.chips+1):
                    self.bet = newbet
                    self.chips -= newbet
                    return newbet
                else:
                    print("You don't have that many chips.")
            except ValueError:
                print("Bets are numbers please.")

    def get_name(self):
        """ Get a player name to join the game """
        name = input("What is your name? ")
        if len(name) > 0:
            self.name = name

    def prepare_round(self):
        """ Setup player for a new round """
        self.hand1 = []
        self.hand2 = []
        # Note, this should already be zero from having bet paid
        self.bet = 0

    def dealt_card(self, card):
        """ Receive a card dealt during the deal round """
        self.hand1.append(card)
        print(f"{self.name} was dealt a {card}")
