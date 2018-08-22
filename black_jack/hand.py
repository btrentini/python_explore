"""
Normal User Type of Player
"""


class Hand:
    '''pass'''

    def __init__(self, player_cards):
        '''initialises the Hand'''
        self.cards = player_cards
        self.initial_count = 4
        self.sum_cards = 0

    def add_card(self, card):
        '''adds a card to a hand'''

        self.cards.append(card)

    def show_cards(self):
        '''shows the cards of a hand'''

        return self.cards

    def hit(self, pack):
        '''When player presses hit, show another card'''

        self.pack = pack
        self.newcard = pack[self.initial_count]
        self.initial_count += 1

        self.cards.append(self.newcard)

        return self.cards
