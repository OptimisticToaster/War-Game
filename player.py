"""Class for Player
   Includes collection of cards as a Hand
   Includes score"""

from card import Card

class Player():
    """Player class to manage player's features, primarily their cards"""


    def __init__(self, player_name) -> None:
        """Initiate an empty hand as collection of Cards."""
        self.name = player_name
        self.score = 0
        # Cards holding in hand
        self.hand = []
        # Cards showing in face up stack on the table
        self.table_face_up = []


    def __str__(self) -> str:
        """Display player name and score."""
        return f'{self.name} has {self.score} points.'


    def __len__(self) -> int:
        """Return how many cards are in the hand."""
        return len(self.hand)


    def show_hand(self) -> list:
        """Display hand."""
        a = ''
        for i in self.hand:
            a += str(i) + ', '
        # remove the trailing comma and space from the assembled string
        return a[:-2]


    def add_cards(self, c:list) -> None:
        """Append a list of Cards to the end of the hand."""
        for i in c:
            self.hand.append(i)


    def remove_card_by_suit_rank(self, s:str, r:str) -> Card:
        """Remove card by suit and rank."""
        a = Card(s, r)
        self.hand.remove(a)
        return a


    def remove_card_by_index(self, n:int) -> Card:
        """Remove card by index position
           Index 0 is top card, index -1 is bottom card."""
        return self.hand.pop(n)


    def play_cards_faceup(self, n:int) -> None:
        """Move card from hand to faceup stack on table."""
        for _ in range(n):
            self.table_face_up.append(self.remove_card_by_index(0))
