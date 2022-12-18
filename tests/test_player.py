"""Test the Player class."""

import unittest

import player
import card

class TestPlayer(unittest.TestCase):
    """Test the Player class."""

    def test_player1(self):
        """Try creating a Player and check that it has valid features."""
        test_player = player.Player('Lisa')
        # Check that it is of type Player
        self.assertIsInstance(test_player, player.Player)
        # Check the __str__ representation
        self.assertEqual(str(test_player), 'Lisa has 0 points.')
        # Check that score is 0
        self.assertEqual(test_player.score, 0)
        # Check that hand is empty
        self.assertEqual(len(test_player.hand), 0)
        # Check player's name
        self.assertEqual(test_player.name, 'Lisa')


    def test_modify_hand(self):
        """Try creating a Player and modify hand."""
        test_player = player.Player('Lisa')
        # Check that hand is empty
        self.assertEqual(len(test_player.hand), 0)
        # Add some Cards to the hand and check hand
        new_cards = [card.Card('H', '6'), card.Card('S', 'Q'), card.Card('C', '9')]
        test_player.add_cards(new_cards)
        self.assertEqual(len(test_player), 3)
        self.assertEqual(test_player.show_hand(), 'H6, SQ, C9')
        # Remove a Card and check hand
        a = test_player.remove_card_by_index(2)
        self.assertEqual(a.suit, 'C')
        self.assertEqual(a.rank, '9')
        self.assertEqual(len(test_player), 2)
        self.assertEqual(test_player.show_hand(), 'H6, SQ')
        b = test_player.remove_card_by_suit_rank('H', '6')
        self.assertEqual(b.suit, 'H')
        self.assertEqual(b.rank, '6')
        self.assertEqual(len(test_player), 1)
        self.assertEqual(test_player.show_hand(), 'SQ')

if __name__ == '__main__':
    unittest.main()
