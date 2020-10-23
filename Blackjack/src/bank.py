""" Bank, including dealer play
"""

from deck import Deck

class Bank():
    """ This is our Bank / Dealer """
    def __init__(self):
        """ We may break this out into a separate function.  """
        self.shoe = Deck(False)
        self.shuffle_shoe()
        self.hand = []

    def shuffle_shoe(self, decks=6):
        """ Shuffle a new shoe of cards """
        del self.shoe
        self.shoe = Deck(True)
        for _ in range(1, decks):
            self.shoe.append(Deck(True))
        self.shoe.shuffle_deck()

    def deal_card(self):
        """ Deal a card from the shoe """
        return self.shoe.deal_card()

    def prepare_round(self, players):
        """ Make sure all players and dealer have empty hands, get bets from players
        Shuffle the shoe if there are fewer than players*8 cards remaining in the shoe
        """
        self.hand = []
        for ply in players:
            ply.clear_hand()
            ply.get_bet()
