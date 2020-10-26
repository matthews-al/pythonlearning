""" Tests for Player class """
import unittest
from ..src import bank

class TestBank(unittest.TestCase):
    """ Test the Player class """

    def setUp(self):
        """ Create a generic deck for testing """
        self.bank = bank.Bank()

    def tearDown(self):
        """ Cleanup our test variables """
        del self.bank

    def test_shoe_size_default(self):
        """ Test the default shoe deck count of 6 """
        self.bank.shuffle_shoe()
        self.assertEqual(len(self.bank.shoe), 6 * 52)

    def test_shoe_size_one(self):
        """ Test the shoe with one deck """
        self.bank.shuffle_shoe(1)
        self.assertEqual(len(self.bank.shoe), 1 * 52)
