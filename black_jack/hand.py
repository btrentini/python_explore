"""
Normal User Type of Player
"""


class Hand:
    '''pass'''

    def __init__(self, player_cards):
        '''initialises the Hand'''
        self.cards = player_cards

    def add_card(self, card):
        '''adds a card to a hand'''

        self.cards.append(card)

    def show_sum(self):
        '''shows the sum of a hand'''

        pass

    def show_cards(self):
        '''shows the cards of a hand'''

        return self.cards
