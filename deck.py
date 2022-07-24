"""Class for Deck as collection of Cards"""

import random
import settings
from card import Card


class Deck():
    """Class for Deck as collection of Cards"""


    def __init__(self) -> None:
        """Setup Deck with initial collection of Cards"""
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


    def __len__(self) -> int:
        """Return size of deck."""
        return len(self.deck)


    def shuffle(self) -> None:
        """Rearrange the deck."""
        random.shuffle(self.deck)


    def deal_cards(self, n:int) -> None:
        """Deal n cards from the top of the deck.
           Essentially removes n cards from the deck"""
        for _ in range(n):
            self.deck.pop(0)
