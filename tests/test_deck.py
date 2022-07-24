"""Test the Deck class."""

from random import shuffle
import unittest

import deck

class TestDeck(unittest.TestCase):
    """Test the Deck class."""

    def test_deck1(self):
        """Try creating a Deck and check that it has valid features."""
        test_deck = deck.Deck()
        # Check that it is of type Deck
        self.assertIsInstance(test_deck, deck.Deck)
        # Check its str representation
        self.assertEqual(str(test_deck), 'C2, C3, C4, C5, C6, C7, C8, C9, C10, CJ, CQ, CK, CA, D2, D3, D4, D5, D6, D7, D8, D9, D10, DJ, DQ, DK, DA, H2, H3, H4, H5, H6, H7, H8, H9, H10, HJ, HQ, HK, HA, S2, S3, S4, S5, S6, S7, S8, S9, S10, SJ, SQ, SK, SA')
        # Check length
        self.assertEqual(len(test_deck), 52)
        # Check that shuffle changes the order
        self.assertNotEqual(test_deck.shuffle(), 'C2, C3, C4, C5, C6, C7, C8, C9, C10, CJ, CQ, CK, CA, D2, D3, D4, D5, D6, D7, D8, D9, D10, DJ, DQ, DK, DA, H2, H3, H4, H5, H6, H7, H8, H9, H10, HJ, HQ, HK, HA, S2, S3, S4, S5, S6, S7, S8, S9, S10, SJ, SQ, SK, SA')
        # Check that dealing cards reduces the deck card-count
        self.assertEqual(len(test_deck), 52)
        test_deck.deal_cards(12)
        self.assertEqual(len(test_deck), 40)
        test_deck.deal_cards(30)
        self.assertEqual(len(test_deck), 10)


if __name__ == '__main__':
    unittest.main()
