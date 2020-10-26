""" Bank, including dealer play
"""
from enum import Enum, auto
from . import deck

class RoundState(Enum):
    """ Enum of round states """
    PREPARING = auto()

class Bank():
    """ This is our Bank / Dealer """
    def __init__(self):
        """ We may break this out into a separate function.  """
        self.shoe = deck.Deck(False)
        self.shuffle_shoe()
        self.hand = []
        self.roundstate = RoundState.PREPARING

    def shuffle_shoe(self, decks=6):
        """ Shuffle a new shoe of cards """
        del self.shoe
        self.shoe = deck.Deck(True)
        for _ in range(1, decks):
            self.shoe.append(deck.Deck(True))
        self.shoe.shuffle_deck()

    def deal_card(self):
        """ Deal a card from the shoe """
        return self.shoe.deal_card()

    def prepare_round(self):
        """ Make sure all players and dealer have empty hands, get bets from players
        Shuffle the shoe if there are fewer than players*8 cards remaining in the shoe
        """
        self.hand = []
        self.roundstate = RoundState.PREPARING
