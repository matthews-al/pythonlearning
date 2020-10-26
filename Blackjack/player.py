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

    def get_bet(self):
        """ Request a bet from the player """
        while newbet := input(f"{self.name} - You have {self.chips}, please enter your bet: "):
            try:
                newbet = int(newbet)
                if newbet in range(0, self.chips+1):
                    self.bet = newbet
                    self.chips -= newbet
                    return newbet
            except ValueError:
                print("Bets are numbers please.")

    def clear_hand(self):
        """ Clear our hand before a round """
        self.hand1 = []
        self.hand2 = []

    def get_name(self):
        """ Get a player name to join the game """
        name = input("What is your name? ")
        if len(name) > 0:
            self.name = name
