""" Blackjack game driver & input test driver """

from src import player

if __name__ == "__main__":
    human = player.Player("me")
    human.get_bet()
