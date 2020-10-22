""" Deck class
 Represent a deck of cards.
 """

class deck():
    """ Represent a standard deck of playing cards """
    def __init__(self):
        """ Create the deck of cards.   Cards will be in "order" when created """
        for suit in ("c", "d", "h", "s"):
            for val in (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"):
                pass
