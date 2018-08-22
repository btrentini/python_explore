"""
Deck for blackjack game
"""
import itertools
import random


class Deck:
    '''Deck class containing methods for playing blackjack'''

    def __init__(self):
        '''Deck initialisation'''

        self.ranks = (str(i) for i in range(1, 14))
        self.suits = ("♣", "♦", "♥", "♠")
        self.pack = list(map(''.join, itertools.chain(
            itertools.product(self.ranks, self.suits))))

    def shuffle(self):
        '''Defines a new pack and shuffles it'''

        self.pack = [w.replace(' 1', 'A').replace('11', 'J').replace(
            '12', 'Q').replace('13', 'K') for w in self.pack]

        self.pack = [w.strip() for w in self.pack]

        random.shuffle(self.pack)

        return self.pack
