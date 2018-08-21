"""
Defines players
"""


class Player:
#
    def __init__(self, player_type, balance, hand):

        self.player_type = player_type
        self.balance = balance
        self.hand = hand

    def update_balance(self, balance):
        self.balance += balance
