""" Tests for deck class """
import unittest
import deck

class TestDeck(unittest.TestCase):
    """ Test the Deck class """

    def setUp(self):
        """ Create a generic deck for testing """
        self.dek = deck.Deck(True)

    def tearDown(self):
        """ Cleanup our test variables """
        self.dek = None

    def test_generic_card(self):
        """ We should get a two of clubs from a new generic deck """
        car = self.dek.deal_card()
        self.assertEqual(str(car), "As")

    def test_generic_deck_size(self):
        """ A generic deck of cards should be 52 cards """
        self.assertEqual(len(self.dek), 52)

    def test_generic_deck_size_deal(self):
        """ The deck should get smaller when we deal a card """
        self.dek.deal_card()
        self.assertEqual(len(self.dek), 51)

if __name__ == "__main__":
    unittest.main()
