""" Tests for card class """
import unittest
from card import Card

class TestCard(unittest.TestCase):
    """ Tests for Card Class """

    def test_repr(self):
        """ Repr call works as expected """
        car = Card('c', 2, 2)
        self.assertEqual(repr(car), "card('c', 2, 2)")

    def test_str(self):
        """ Str call works as expected """
        car = Card('c', 2, 2)
        self.assertEqual(str(car), "2c")

    def test_equalsimple(self):
        """  Does a card equal itself """
        car = Card('c', 2, 2)
        dcar = Card('c', 2, 2)
        self.assertEqual(car, dcar)

    def test_notequal(self):
        """ Does a card not equal a different card """
        car = Card('c', 2, 2)
        dcar = Card('s', 3, 3)
        self.assertNotEqual(car, dcar)

    def test_equalint(self):
        """ Can we check if a card equals a value """
        car = Card('c', 2, 2)
        self.assertEqual(car, 2)

if __name__ == "__main__":
    unittest.main()
