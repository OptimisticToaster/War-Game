"""Class for Player
   Includes collection of cards as a Hand
   Includes score"""

from card import Card

class Player():
    """Player class to manage player's features, primarily their cards"""


    def __init__(self) -> None:
        """Initiate an empty hand as collection of Cards."""
        self.score = 0
        self.hand = []


    def __str__(self) -> list:
        """Display hand."""
        a = ''
        for i in self.hand:
            a += str(i) + ', '
        # remove the trailing comma and space from the assembled string
        return a[:-2]


    def __len__(self) -> int:
        """Return how many cards are in the hand."""
        return len(self.hand)


    def add_cards(self, c:'list') -> None:
        """Append a list of Cards to the end of the hand."""
        for i in c:
            self.hand.append(i)

    def remove_card_by_suit_rank(self, s:str, r:str) -> None:
        """Remove card by suit and rank."""
        a = Card(s, r)
        self.hand.remove(a)


    def remove_card_by_index(self, n:int) -> None:
        """Remove card by index position
           Index 0 is top card, index -1 is bottom card."""
        self.hand.pop(n)
