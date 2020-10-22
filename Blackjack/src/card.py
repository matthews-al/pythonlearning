""" Card class
Handle standard playing cards
"""

class card():
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