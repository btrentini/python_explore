"""
Defines players
"""


class Player:
    '''class player'''

    def __init__(self, player_type, balance, hand):
        '''initialises a player'''

        self.player_type = player_type
        self.balance = balance
        self.hand = hand
        self.sum_cards = 0

    def update_balance(self, balance):
        '''updates player balance'''
        self.balance += balance

    def print_hand(self):
        '''prints the player hand'''

        if self.player_type.upper() == "DEALER":
            return self.hand.cards[0]
        else:
            return self.hand.cards

    def cards_sum(self, sum_cards):
        '''shows the sum of a hand'''

        self.sum_cards = sum_cards

        if len(self.hand.cards) == 2 and self.sum_cards == 21:
            print("BALCK JACK")
        if self.sum_cards == 21:
            print("21")
        elif self.sum_cards > 21:
            print("BURST")
        else:
            pass

        return self.sum_cards
