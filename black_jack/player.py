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

    def update_balance(self, balance):
        '''updates player balance'''
        self.balance += balance

    def print_hand(self):
        '''prints the player hand'''
        return self.hand.cards
