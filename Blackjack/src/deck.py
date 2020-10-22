""" Deck class
 Represent a deck of cards.
 """
import card

class Deck():
    """ Represent a standard deck of playing cards """
    def __init__(self, generic=True):
        """ Deck can be used to handle draw piles, discard piles, etc.
        Generic == True will create a 'standard' deck of playing cards with no jokers
        """
        if generic:
            self.create_std_deck()

    def create_std_deck(self, face_card_ten=True):
        """ Create the deck of cards.   Cards will be in "order" when created
        faceCardTen == True means that J/Q/K will have value of 10, and A == 11
        faceCardTen == False means that J/Q/K/A will have values 11/12/13/14
        """
        card_vals = []
        for i in range(2, 11):
            card_vals.append((i, i))
        if face_card_ten:
            card_vals.append(("J", 10))
            card_vals.append(("Q", 10))
            card_vals.append(("K", 10))
            card_vals.append(("A", 11))
        else:
            card_vals.append(("J", 11))
            card_vals.append(("Q", 12))
            card_vals.append(("K", 13))
            card_vals.append(("A", 14))

        self.cards = []

        for suit in ("c", "d", "h", "s"):
            for num, val in card_vals:
                self.cards.append(card.Card(suit, num, val))

    def deal_card(self):
        """ Deal a card """
        return self.cards.pop()

    def __len__(self):
        """ How many cards are currently in the deck """
        return len(self.cards)
