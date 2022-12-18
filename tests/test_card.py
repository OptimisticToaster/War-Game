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


    def test_card2(self):
        """Try creating a Card with invalid suit."""
        test_card = card.Card('M', '6')
        self.assertRaises(Exception)


    def test_card3(self):
        """Try creating a Card with invalid rank."""
        test_card = card.Card('H', '87')
        self.assertRaises(Exception)


    def test_equality(self):
        """Check equality of two Cards."""
        test_card1 = card.Card('H', '6')
        test_card2 = card.Card('H', '6')
        self.assertTrue(test_card1.__eq__(test_card2))
        test_card3 = card.Card('C', '9')
        self.assertFalse(test_card1.__eq__(test_card3))


if __name__ == '__main__':
    unittest.main()
