"""Run the War game application."""

from datetime import datetime
import time
import logging

import settings

import card
import deck
import player


# Setup logging
logger =  logging.getLogger('__name__')
logging.basicConfig(level=logging.DEBUG, filename=datetime.now().strftime('app_%Y%m%d-%H%M%s.log'), filemode='w', format='%(asctime)s : %(name)s - %(levelname)s - %(message)s', datefmt='%Y%m%d %H:%M:%S')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(name)s - %(levelname)s - %(message)s', datefmt='%y-%m-%d %H:%M:%S')


def show_status(player1, player2):
    """Return statement of current card status of each player."""
    if len(player1) == len(player2):
        return f'Both players have {len(player1)} cards.'
    else:
        return f'Player1 has {len(player1)} cards, and Player2 has {len(player2)} cards.'

def main():
    """Run application."""
    logger.debug('Starting application.')

    # Create player 1
    player1 = player.Player(input('Enter name for player 1: '))

    # Create player 2
    player2 = player.Player(input('Enter name for player 2: '))

    # Setup deck
    d = deck.Deck()
    d.shuffle()

    # Deal cards to each player until the deck is empty.
    for _ in range(int(len(d)/2)):
        # each round of dealing, give one card to each player
        player1.add_cards(d.deal_cards(1))
        player2.add_cards(d.deal_cards(1))

    logger.debug('Player 1 hand: ')
    for _ in player1.hand:
        logger.debug(_)
    logger.debug('Player 2 hand: ')
    for _ in player2.hand:
        logger.debug(_)

    # Ask for key press to start game.
    input('The game is ready to begin. Press <ENTER> to continue.')

    # Play the game by a series of rounds as long as each player has more than 0 cards.
    # Pause between each round to display the status.
    game_round = 0
    while len(player1) > 0 and len(player2) > 0:
        game_round += 1
        print(f'\n\nRound {game_round}')
        print(show_status(player1, player2))
        logger.debug(show_status(player1, player2))

        logger.debug('Player 1 cards: ')
        for _ in player1.hand:
            logger.debug(_)
        logger.debug('Player 2 cards: ')
        for _ in player2.hand:
            logger.debug(_)
        
        time.sleep(2)

        # Players play a list of cards from 1+ cards
        # In case of tie, each player plays up to 3 cards then plays again
        player1.play_cards_faceup(1)
        player2.play_cards_faceup(1)

        print(f'Player 1 showing {player1.table_face_up[-1]}')
        print(f'Player 2 showing {player2.table_face_up[-1]}')

        logger.debug('Player 1 table cards: ')
        for _ in player1.table_face_up:
            logger.debug(_)
        logger.debug('Player 2 table cards: ')
        for _ in player2.table_face_up:
            logger.debug(_)

        # Compare plays to find winner.
        if player1.table_face_up[-1].rank > player2.table_face_up[-1].rank:
            # Player 1 wins
            print('Player 1 wins the round.')
            # Add table cards to Player 1's hand
            player1.add_cards(player1.table_face_up)
            player1.add_cards(player2.table_face_up)
            # Clear table stacks
            player1.clear_cards_faceup()
            player2.clear_cards_faceup()
        elif player2.table_face_up[-1].rank > player1.table_face_up[-1].rank:
            # Player 2 wins
            print('Player 2 wins the round.')
            # Add table cards to Player 2's hand
            player2.add_cards(player2.table_face_up)
            player2.add_cards(player1.table_face_up)
            # Clear table stacks
            player1.clear_cards_faceup()
            player2.clear_cards_faceup()
        else:
            # Tie
            print('Tie')
            # Return cards to hand.
            player1.add_cards(player1.table_face_up)
            player2.add_cards(player2.table_face_up)
            # Clear table stacks
            player1.clear_cards_faceup()
            player2.clear_cards_faceup()


    # Game is over - see who won
    if len(player1) == 0:
        print("Player1 out of cards! Game Over")
        print(f"Player2 wins in {game_round} rounds!")

    if len(player2) == 0:
        print("Player2 out of cards! Game Over")
        print(f"Player1 wins in {game_round} rounds!")


if __name__ == "__main__":
    main()
