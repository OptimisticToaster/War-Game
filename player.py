"""
Class for Player
Includes collection of cards as a Hand
Includes score
"""

import settings
from card import Card

class Player():

    # initiate an empty hand as collection of Cards
    def __init__(self) -> None:
        self.score = 0
        self.hand = []

    # display Hand
    def __str__(self) -> list:
        a = ''
        for i in self.hand:
            a += str(i) + ', '
        # remove the trailing comma and space from the assembled string
        return a[:-2]

    # return how many cards are in the hand
    def __len__(self) -> int:
        return len(self.hand)

    # append a list of Cards to the end of the hand
    def add_cards(self, c:'list') -> None:
        for i in c:
            self.hand.append(i)

    # remove card by suit and rank
    def remove_card_by_suit_rank(self, s:str, r:str) -> None:
        a = Card(s, r)
        print(f'a is {a}')
        self.hand.remove(a)

    # remove card by index position
    # index 0 is top card, index -1 is bottom card
    def remove_card_by_index(self, n:int) -> None:
        self.hand.pop(n)
