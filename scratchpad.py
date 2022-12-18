import settings
import card
import logging

logging.basicConfig(format='%(asctime)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def main():
    logger.debug('Creating card H6')
    a = card.Card('H', '6')
    logger.debug(a)
    logger.debug('Creating card M6 (invalid)')
    b  = card.Card('M', '6')
    logger.debug(b)
    # AttributeError: 'Card' object has no attribute 'suit'
    logger.debug('Creating card H87 (invalid)')
    c  = card.Card('H', '87')
    logger.debug(c)



if __name__ == '__main__':
    main()
