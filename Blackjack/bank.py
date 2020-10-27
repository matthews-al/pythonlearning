""" Bank, including dealer play
"""
import deck

class Bank():
    """ This is our Bank / Dealer """
    def __init__(self):
        """ We may break this out into a separate function.  """
        self.shoe = deck.Deck(False)
        self.shuffle_shoe()
        self.hand = []

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

    def dealer_draw(self, card):
        """ Deal a card to the dealer.   First card is face down, second faceup """
        self.hand.append(card)
        if len(self.hand) == 1:
            print(f"Dealer's first card is a {card}")
        elif len(self.hand) == 2:
            print("Dealer takes a second card.")

    def dealer_21(self):
        """ Check for dealer blackjack """
        if sum(self.hand) == 21:
            print("Dealer has a Blackjack")
            print(f"{self.hand[0]} {self.hand[1]}")
            return True
        return False

    def dealer_hand_value(self):
        """ Return the value of the dealers hand """
        return deck.bj_hand_value(self.hand)

    def dealer_turn(self):
        """ Play the dealers turn
        Dealer stands on soft 17
        """
        val, soft, hard = deck.bj_hand_value(self.hand)
        print(f"Dealer's hand: {deck.hand_to_str(self.hand)}")
        while val < 17 or (soft and hard < 18):
            self.hand.append(self.deal_card())
            print(f"Dealer draws {self.hand[-1]}")
            print(f"Dealer's hand: {deck.hand_to_str(self.hand)}")
            val, soft, hard = deck.bj_hand_value(self.hand)
        if val > 21:
            print("Dealer Bust, players win.")
