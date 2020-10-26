""" Card class
Handle standard playing cards
"""

class Card():
    """ A single card from a standard deck of playing cards """
    def __init__(self, suit, num, val):
        """ We take value so the cards can be used in different games """
        self.val = val
        self.suit = suit
        self.num = num

    def __repr__(self):
        """ Instantiable representation """
        return '{}({!r}, {!r}, {!r})'.format(self.__class__.__name__, self.suit, self.num, self.val)

    def __str__(self):
        """ Plain string format """
        return '{}{}'.format(self.num, self.suit)

    def __eq__(self, other):
        """ This isn't really needed for Blackjack, but we'll add a value based version for now """
        if isinstance(other, Card):
            return self.val == other.val
        if isinstance(other, int):
            return self.val == other
        return False

    def __int__(self):
        """ Casting to int will return the value of the card """
        return self.val

    def __add__(self, other):
        if isinstance(other, Card):
            return self.val + other.val
        if isinstance(other, int):
            return self.val + other

    def __radd__(self, other):
        if isinstance(other, Card):
            return self.val + other.val
        if isinstance(other, int):
            return self.val + other
