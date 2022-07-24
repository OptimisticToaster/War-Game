"""Test the Card class."""

import unittest

import card

class TestCard(unittest.TestCase):
    """Test the Card class."""

    def test_card1(self):
        """Try creating a Card and check that it has valid features."""
        test_card = card.Card('H', '6')
        # Check that it is of type Card
        self.assertIsInstance(test_card, card.Card)
        # Check its str representation
        self.assertEqual(str(test_card), 'H6')
        # Check full label
        self.assertEqual(test_card.get_full(), '6 of Hearts')
        # Check equality
        test_card2 = card.Card('H', '6')
        self.assertTrue(test_card.__eq__(test_card2))
        test_card3 = card.Card('C', '9')
        self.assertFalse(test_card.__eq__(test_card3))


if __name__ == '__main__':
    unittest.main()
