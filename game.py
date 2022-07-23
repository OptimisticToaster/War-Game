from setuptools import setup
import settings
from card import Card
from deck import Deck
from player import Player

def main():
    d = Deck()
    d.shuffle()
    d.shuffle()
    thor = Player()
    jane = Player()
    setup_cards = [Card('C', '3'), Card('D', 'Q'), Card('S', '6'), Card('H', 'A'), Card('H', '4'), Card('S', '9'), Card('D', 'A'), Card('C', '10'), Card('D', '7'), Card('S', 'J')]
    thor.add_cards(setup_cards)
    setup_cards = [Card('H', '3'), Card('C', '8'), Card('D', 'J'), Card('D', '3'), Card('D', '6'), Card('D', '7'), Card('H', 'A'), Card('S', '10'), Card('S', '7'), Card('C