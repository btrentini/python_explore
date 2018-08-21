"""
Deck for blackjack game
"""
import itertools
import random


class Deck:

    def __init__(self):
        '''Initialisation for Player'''

        self.ranks = (str(i) for i in range(1, 14))
        self.suits = ("♣", "♦", "♥", "♠")

    def shuffle(self):
        self.pack = list(map(''.join, itertools.chain(
                itertools.product(self.ranks, self.suits))))

        random.shuffle(self.pack)

        return self.pack

    def deal(self):
        pass
