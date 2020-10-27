""" Underlying player class
Players need:
* Chip balance
* a current hand (or pair of hands for split)
"""
import deck

class Player():
    """ This is our base player class """
    def __init__(self, name="Player"):
        """ Initialize a player - at Python Casino, we give new players 100 chips to play """
        self.name = name
        self.chips = 100
        self.hand1 = []
        self.hand2 = []
        self.bet = 0
        self.lastbet = 0

    def get_bet(self):
        """ Request a bet from the player """
        while newbet := input(f"{self.name}: {self.chips} chips. Last bet: {self.lastbet}.  Bet: "):
            try:
                newbet = int(newbet)
                if newbet in range(0, self.chips+1):
                    self.bet = newbet
                    self.chips -= newbet
                    return newbet
                else:
                    print("You don't have that many chips.")
            except ValueError:
                print("Bets are numbers please.")

    def get_name(self):
        """ Get a player name to join the game """
        name = input("What is your name? ")
        if len(name) > 0:
            self.name = name

    def prepare_round(self):
        """ Setup player for a new round """
        self.hand1 = []
        self.hand2 = []
        # Note, this should already be zero from having bet paid
        self.bet = 0

    def dealt_card(self, card):
        """ Receive a card dealt during the deal round """
        self.hand1.append(card)
        print(f"{self.name} was dealt a {card}")

    def hand_value(self):
        """ Return the value of the players hand.  Still need to handle split hands somehow """
        return deck.bj_hand_value(self.hand1)

    def win(self, dlr):
        """ Winning hand, pay BJ 3:2 or normal 2:1 """
        if sum(self.hand1[0:2]) == 21:
            pay = int(self.bet * 1.5)
            self.chips += pay + self.bet
            self.lastbet = self.bet
            self.bet = 0
            print(f"{self.name} has a Blackjack.  Wins {pay}")
        else:
            print(f"{self.name} has {sum(self.hand1)}, beating dealers {dlr}")
            print(f"   Wins: {self.bet}")
            # Expanding for easy viewing
            self.chips += self.bet + self.bet

    def lose(self, dlr):
        """ Lost hand, lost bet """
        print(f"Sorry {self.name}, your total of {sum(self.hand1)} didn't beat the dealers {dlr}")
        self.lastbet = self.bet
        self.bet = 0

    def push(self, dlr):
        """ Pay a push bet """
        print(f"{self.name}'s {dlr} matched the dealers hand, push")
        self.chips += self.bet
        self.lastbet = self.bet
        self.bet = 0

    def play_round(self, house):
        """ Take a turn """
