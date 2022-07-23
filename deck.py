"""
Class for Deck as collection of Cards
"""

import settings
import random
from card import Card

class Deck():

    # setup Deck with initial collection of Cards
    def __init__(self) -> None:
        self.deck = []
        for s in settings.SUITS:
            for r in settings.RANKS:
                self.deck.append(Card(s, r))

    # display Deck
    def __str__(self) -> list:
        a = ''
        for i in self.deck:
            a += str(i) + ', '
        # remove the trailing comma and space from the assembled string
        return a[:-2]

    # return size of Deck
    def __len__(self) -> int:
        return len(self.deck)

    # rearrange the deck
    def shuffle(self) -> None:
        random.shuffle(self.deck)

    # deal n cards from the top of the deck
    # essentially removes n cards from the deck
    def deal_cards(self, n:int) -> None:
        for i in range(n):
            self.deck.pop(0)
