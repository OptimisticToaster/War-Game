"""
Class for individual Cards
"""

import settings

class Card():
    """Manage instance of a Card in a Deck."""

    def __init__(self, suit: str, rank: str) -> None:
        """Initiate instance of a Card."""
        try:
            self.suit: str = suit
        except Exception as e:
            print(e)
            exit
        try:
            self.rank: int = rank
        except Exception as e:
            print(e)
            exit
        self.value = settings.RANKS[self.rank]

    def __str__(self) -> str:
        """Human-friendly display of Card object."""
        return self.suit + self.rank

    def get_full(self) -> str:
        """More casual display of Card object."""
        return self.rank + ' of ' + settings.SUITS[self.suit]

    # https://stackoverflow.com/questions/48513729/remove-an-object-from-a-list-of-objects
    def __eq__(self, other):
        """Compare equality of two Card objects."""
        return self.suit == other.suit and self.rank == other.rank
