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
        # Cards holding in hand.
        # Index 0-> from back/left to front/right
        self.hand = []
        # Cards showing in face up stack on the table.
        # Index 0-> from bottom of stack up
        # So [0] refers to bottom card showing
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


    def show_table_cards(self) -> list:
        """Display table cards."""
        a = ''
        for i in self.table_face_up:
            a += str(i) + ', '
        # remove the trailing comma and space from the assembled string
        return a[:-2]


    def add_cards(self, c:list) -> None:
        """Append a list of Cards to the end of the hand."""
        for i in c:
            self.hand.append(i)


    def remove_card_by_suit_rank(self, s:str, r:str) -> Card:
        """Remove card by suit and rank."""
        return True if self.hand.remove(Card(s,r)) else False


    def remove_card_by_index(self, n:int) -> Card:
        """Remove card from hand by index position
           Index 0 is back/left card, index -1 is front/right card."""
        return self.hand.pop(n)


    def play_cards_faceup(self, n:int) -> None:
        """Move card from hand to faceup stack on table.
            Index for hand has 0 is back/left card, index -1 is front/right card.
            Index for table has 0 is bottom card showing."""
        for _ in range(n):
            self.table_face_up.append(self.remove_card_by_index(0))


    def clear_cards_faceup(self) -> None:
        """Clear cards from table."""
        self.table_face_up.clear()

