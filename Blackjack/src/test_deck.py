""" Tests for deck class """
import unittest
import deck
import card

class TestDeck(unittest.TestCase):
    """ Test the Deck class """

    def setUp(self):
        """ Create a generic deck for testing """
        self.dek = deck.Deck(True)

    def tearDown(self):
        """ Cleanup our test variables """
        del self.dek

    def test_generic_card(self):
        """ We should get a two of clubs from a new generic deck """
        car = self.dek.deal_card()
        self.assertEqual(str(car), "As")

    def test_generic_card_position(self):
        """ Position 0 in the deck should be 2c """
        car = self.dek[0]
        self.assertEqual(str(car), "2c")

    def test_generic_deck_size(self):
        """ A generic deck of cards should be 52 cards """
        self.assertEqual(len(self.dek), 52)

    def test_generic_deck_size_deal(self):
        """ The deck should get smaller when we deal a card """
        self.dek.deal_card()
        self.assertEqual(len(self.dek), 51)

    def test_shuffle(self):
        """ It should be sufficiently improbable statistiscally for the entire deck
        to stay in the same order it started to use that as our test case.
        """
        dek2 = deck.Deck(True)
        dek2.shuffle_deck()
        self.assertNotEqual(self.dek.cards, dek2.cards)

    def test_append_deck(self):
        """ Try appending a second copy of the deck, we should get 104 cards """
        self.dek.append(deck.Deck(True))
        self.assertEqual(len(self.dek), 104)

    def test_append_card(self):
        """ Try appending a second copy of the deck, we should get 104 cards """
        self.dek.append(card.Card('s', 2, 2))
        self.assertEqual(len(self.dek), 53)

if __name__ == "__main__":
    unittest.main()
