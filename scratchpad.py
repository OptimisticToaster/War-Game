import settings
import card
import player
import logging

logging.basicConfig(format='%(asctime)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def main():
    a = card.Card('H', '4')
    b  = card.Card('S', 'Q')
    c  = card.Card('H', 'A')
    ryan = player.Player('Ryan')
    ryan.add_cards([a, b, c])
    print(ryan.show_hand())
    ryan.play_cards_faceup(1)
    print(ryan.show_hand())
    print(ryan.show_table_cards())
    ryan.play_cards_faceup(1)
    print(ryan.show_hand())
    print(ryan.show_table_cards())



if __name__ == '__main__':
    main()
