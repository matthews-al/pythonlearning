""" Tests for card class """
import unittest
from card import card

class TestDeck(unittest.TestCase):
    def test_repr(self):
        c = card('c', 2, 2)
        self.assertEqual(repr(c), "card('c', 2, 2)")

    def test_str(self):
        c = card('c', 2, 2)
        self.assertEqual(str(c), "2c")

if __name__ == "__main__":
    unittest.main()
