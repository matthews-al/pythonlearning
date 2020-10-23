""" Tests for Player class """
import unittest
import player

class TestPlayer(unittest.TestCase):
    """ Test the Player class """

    def setUp(self):
        """ Create a generic deck for testing """
        self.player = player.Player(name="Fred")

    def tearDown(self):
        """ Cleanup our test variables """
        del self.player

    def test_new_player(self):
        """ We should have the proper name assigned and a balance of 100 """
        self.assertEqual(self.player.name, "Fred")
        self.assertEqual(self.player.chips, 100)
